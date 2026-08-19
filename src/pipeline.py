import os
import json
import logging
from datetime import datetime
from src.config import load_config
from src.models.schema import BaseEntity
from src.discovery.synthetic_loader import load_candidates
from src.cleaning.cleaner import clean_html
from src.normalization.normalizer import normalize_entity
from src.deduplication.deduplicator import Deduplicator
from src.classification.classifier import classify_entity
from src.relationships.relationship_extractor import RelationshipGraph
from src.validation.validator import validate_entity

logger = logging.getLogger(__name__)

class AIOOrbitPipeline:
    def __init__(self, cfg=None, use_synthetic=False):
        self.cfg = cfg or load_config()
        self.dedup = Deduplicator()
        self.graph = RelationshipGraph()
        self.records = []
        self.canonical_map = {}
        self.use_synthetic = use_synthetic

    def _to_entity(self, record: dict):
        # Ensure required keys and stable id already present
        return {
            "id": record.get("id") or BaseEntity.stable_uuid(record.get("name", "unknown")),
            "entity_type": record.get("entity_type", "Unknown"),
            "name": record.get("name"),
            "description": record.get("description"),
            "url": record.get("url"),
            "categories": record.get("categories", []),
            "source": record.get("source", {"name": "unknown", "url": None}),
            "created_at": record.get("created_at", datetime.utcnow().isoformat()),
            # include any specialized metadata transparently
            **{k:v for k,v in record.items() if k not in {"id","entity_type","name","description","url","categories","source","created_at"}}
        }

    def discovery(self):
        logger.info("Discovery stage (synthetic=%s)", self.use_synthetic)
        if self.use_synthetic:
            candidates = load_candidates(self.cfg.output_dir)
        else:
            # Placeholder for real connectors (GitHub/HF/YouTube/News)
            candidates = []
        self.records = [self._to_entity(r) for r in candidates][:self.cfg.max_records]
        logger.info("Discovered %d candidate records", len(self.records))

    def cleaning(self):
        logger.info("Cleaning stage")
        for r in self.records:
            if r.get("description") and ("<" in r["description"] or ">" in r["description"]):
                r["description"] = clean_html(r["description"])

    def normalization(self):
        logger.info("Normalization stage")
        for i, r in enumerate(self.records):
            self.records[i] = normalize_entity(r)

    def deduplication(self):
        logger.info("Deduplication stage")
        deduped, mapping = self.dedup.deduplicate_batch(self.records)
        self.records = deduped
        self.canonical_map = mapping
        logger.info("Deduplication reduced to %d records", len(self.records))

    def classification(self):
        logger.info("Classification stage")
        for i, e in enumerate(self.records):
            self.records[i] = classify_entity(e)

    def relationships(self):
        logger.info("Relationship extraction stage")
        # Build sample relationships programmatically:
        # - Company -> develops -> some Tools and Models where company name appears in provider or repo owner
        name_to_id = {r["name"]: r["id"] for r in self.records}
        # map first 20 companies
        companies = [r for r in self.records if r["entity_type"] == "Company"]
        tools = [r for r in self.records if r["entity_type"] == "Tool"]
        models = [r for r in self.records if r["entity_type"] == "Model"]
        tasks = [r for r in self.records if r["entity_type"] == "Task"]
        mcps = [r for r in self.records if r["entity_type"] == "MCP"]
        devices = [r for r in self.records if r["entity_type"] == "Device"]
        repos = [r for r in self.records if r["entity_type"] == "Repository"]
        # companies develop -> tools/models/repos
        for i, comp in enumerate(companies):
            # assign up to 3 tools/models each deterministically
            for t in tools[i::len(companies)][:2]:
                self.graph.add(comp["id"], "develops", t["id"], {"reason": "synthetic_assignment"})
            for m in models[i::len(companies)][:2]:
                self.graph.add(comp["id"], "develops", m["id"], {"reason": "synthetic_assignment"})
            for r in repos[i::len(companies)][:1]:
                self.graph.add(comp["id"], "maintains", r["id"], {"repo_name": r["name"]})
        # tools solve tasks (one-to-many)
        for i, tool in enumerate(tools):
            task = tasks[i % max(1, len(tasks))]
            self.graph.add(tool["id"], "solves", task["id"], {})
        # MCP integrates with a subset of tools
        for i, mcp in enumerate(mcps):
            for t in tools[i::len(mcps)][:3]:
                self.graph.add(mcp["id"], "integrates_with", t["id"], {})
        # devices run some models
        for i, dev in enumerate(devices):
            for m in models[i::len(devices)][:3]:
                self.graph.add(dev["id"], "runs", m["id"], {})
        # repos reference models (sample)
        for i, repo in enumerate(repos):
            if models:
                self.graph.add(repo["id"], "references_model", models[i % len(models)]["id"], {})
        # link videos to tools/models they discuss (simple mapping)
        videos = [r for r in self.records if r["entity_type"] == "Video"]
        for i, vid in enumerate(videos):
            if tools:
                self.graph.add(vid["id"], "about", tools[i % len(tools)]["id"], {})
            elif models:
                self.graph.add(vid["id"], "about", models[i % len(models)]["id"], {})

    def validation(self):
        logger.info("Validation stage")
        valid = []
        for e in self.records:
            ok, errs = validate_entity(e)
            if not ok:
                logger.warning("Entity %s failed validation: %s", e.get("name"), errs)
            else:
                valid.append(e)
        self.records = valid
        logger.info("Validation passed for %d records", len(self.records))

    def persist(self):
        out_dir = self.cfg.output_dir
        os.makedirs(out_dir, exist_ok=True)
        records_path = os.path.join(out_dir, "records.json")
        rel_path = os.path.join(out_dir, "relationships.json")
        with open(records_path, "w", encoding="utf-8") as f:
            json.dump(self.records, f, indent=2, ensure_ascii=False, default=str)
        with open(rel_path, "w", encoding="utf-8") as f:
            json.dump(self.graph.export(), f, indent=2, ensure_ascii=False, default=str)
        logger.info("Wrote %d final records to %s", len(self.records), records_path)

    def run(self):
        logger.info("Starting pipeline")
        try:
            self.discovery()
            self.cleaning()
            self.normalization()
            self.deduplication()
            self.classification()
            self.relationships()
            self.validation()
            self.persist()
        except Exception as e:
            logger.exception("Pipeline failed: %s", e)
