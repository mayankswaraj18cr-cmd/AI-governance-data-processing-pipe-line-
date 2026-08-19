# AI Orbit — Data Ingestion Pipeline (Complete Synthetic Deliverable)

This repository is a production-oriented scaffold for collecting, normalizing, deduplicating, classifying, and linking entities from the AI ecosystem. For this deliverable, I generate a curated, synthetic dataset (256 records) to demonstrate the full pipeline end-to-end without requiring external API keys.

What you get
- Full modular pipeline (src/) covering discovery (synthetic), cleaning, normalization, deduplication, classification, relationships, and validation.
- A deterministic synthetic dataset generator that produces candidate entities (data/generated_candidates.json).
- The pipeline writes final cleaned, normalized records to data/records.json and relationships.json.
- run.py orchestrates generation + pipeline run.

Quick start
1. Create virtualenv and install deps:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2. Generate dataset and run pipeline:
   python run.py

Outputs:
- data/generated_candidates.json  (raw candidates)
- data/records.json               (final cleaned & deduped records)
- data/relationships.json         (graph edges)

Design choices & notes
- API-first connectors can be added by implementing real discovery modules and toggling out of synthetic mode.
- Stable, deterministic UUID generation is used (uuid5 namespace "ai-orbit") so identical names map to same IDs across runs.
- Deduplication uses fuzzy matching (rapidfuzz) with a high threshold to avoid false merges.
- Relationships are created by deterministic assignment rules to demonstrate graph connectivity: company->develops->tool/model, tool->solves->task, mcp->integrates_with->tool, device->runs->model, repo->references_model, etc.
- The dataset is curated and intentionally not exhaustive — it emphasizes relationship density, metadata richness, normalization, and reproducibility.

How to extend to real data / 250–300+ real records
- Replace synthetic_loader with real API connectors (GitHubDiscovery, HuggingFaceExtractor, YouTubeExtractor, RSS fetchers).
- Respect rate limits and add retries/backoff.
- Use external knowledge bases (Wikidata) to improve entity resolution and canonicalization.
- Enhance relationship extraction with site scraping for "About" pages and repo owner metadata.

If you want:
- I can push this project to a GitHub repo (you provide owner/repo).
- I can add live connectors for GitHub/HuggingFace/YouTube and run a real ingest if you provide API keys or configure them as secrets.

License: MIT
