"""
Generate a curated synthetic dataset of AI ecosystem entities.
 - deterministic UUIDs based on name (stable)
 - writes data/generated_candidates.json
 - writes data/seed_meta.json (optional)
"""
import json
import random
import os
from datetime import datetime
import uuid

NAMESPACE = uuid.uuid5(uuid.NAMESPACE_DNS, "ai-orbit")

def stable_uuid(name: str):
    return str(uuid.uuid5(NAMESPACE, name.lower().strip()))

def make_source(name, url):
    return {"name": name, "url": url}

def make_entity(name, entity_type, description, url, source, categories, created_at):
    return {
        "id": stable_uuid(name),
        "entity_type": entity_type,
        "name": name,
        "description": description,
        "url": url,
        "categories": categories,
        "source": source,
        "created_at": created_at
    }

def generate_and_write_dataset(output_dir="data", seed=0, total=256):
    random.seed(seed)
    os.makedirs(output_dir, exist_ok=True)
    created_at = datetime.utcnow().isoformat()
    records = []

    # curated lists
    companies = [
        "Aether Labs", "NeuroForge", "OpenAI", "DeepVision Inc", "Sage Systems", "CoreML Co.",
        "RoboDynamics", "HorizonAI", "CortexWorks", "Lumen Labs", "EdgeAI Solutions", "VectorSense",
        "MCPify", "ModelHub LLC", "CreativeMinds", "GenerativeWorks"
    ]
    tasks = [
        "Text Summarization", "Image Generation", "Automatic Translation", "Question Answering",
        "Object Detection", "Semantic Segmentation", "Speech-to-Text", "Text-to-Speech",
        "Anomaly Detection", "Time Series Forecasting", "Code Generation", "Recommendation",
        "Data Labeling", "Information Retrieval", "Sentiment Analysis", "Document OCR"
    ]
    tools = [
        "OrbitStudio", "PromptForge", "DataRefine", "VisionSuite", "AudioWorks", "AnnotatePro",
        "VectorSearchX", "AutoLabeler", "PipelineFlow", "InsightDashboard", "EdgeDeploy", "MCP Control",
        "ModelOpsHub", "StreamAnalyzer", "CreativeStudio", "AssistantCore"
    ]
    models = [
        "gpt-mini", "gpt-base", "gpt-large", "vis-bert", "audio-net", "clip-slim", "clip-large",
        "detectnet", "segformer-lite", "wav2vec-small", "tts-lite", "time-series-rnn",
        "recommender-transformer", "codex-lite", "stable-image-1", "creative-diffusion"
    ]
    repos = [
        "aetherlabs/edge-ml", "neuroforge/model-zoo", "openai/example-integration", "deepvision/detect",
        "sagesystems/translate-core", "coreml/edge-runtime", "robodynamics/robot-stack", "horizonnn/research",
        "cortexworks/pipeline", "lumenlabs/vision-utils", "edgeai/deploy", "vectorsense/vecdb",
        "mcpify/installer", "modelhub/registry", "creativeminds/assets", "generativeworks/studio"
    ]
    videos = [
        "Intro to OrbitStudio", "Deploying Models on EdgeAI", "Building with PromptForge", "VisionSuite Tutorial",
        "How MCP Control Works", "ModelOps Best Practices", "CreativeStudio Walkthrough", "VectorSearchX Explained",
    ]
    robots = [
        "RoboArm v1", "DeliveryBot Pro", "HomeAssist 2", "Surveyor Rover", "WarehouseMover", "Scout Drone",
        "SurgicalAssist", "Companion Bot"
    ]
    devices = [
        "Edge TPU A1", "NPU Board X", "Jetson Nano Pro", "QuantumAI Module", "VisionEdge Camera", "Studio GPU-8",
        "Mobile AI SoC", "Robotics Controller V2"
    ]
    mcps = [
        "MCP Server Lite", "MCP Server Pro", "MCP Edge", "MCP Control Panel"
    ]
    collections = [
        "Top-LLMs-2026", "Robotics-Kit-Index", "Edge-Deploy-Tools", "Creative-Generators-Collection"
    ]
    personal = [
        "Alice Assistant", "BobBot", "Clara AI", "DevAssist", "NoteKeeper", "MailAgent", "SchedulerPro", "ResearchBuddy"
    ]
    creative = [
        "ImagePainter", "SongComposer", "VideoRemixer", "StyleGANx", "MuseSketch", "StoryWeaver", "AdCopyGen", "LogoForge"
    ]
    news = [
        "AI Startup Raises Series B", "Major Model Release", "New MCP Integration Announced", "Breakthrough in RL",
        "AI Hardware Launch", "Important Security Patch", "Industry Standards Released", "Acquisition Announcement"
    ]
    new_added = [
        "NovaModel", "EdgeSynth", "TinyML Toolkit", "ZeroShotSearch", "MindMap AI", "SketchGen", "Speech2Code", "MicroMCP"
    ]

    # helper to build url
    def make_url(prefix, name):
        slug = name.lower().replace(" ", "-").replace("/", "-")
        return f"https://{prefix}.example/{slug}"

    # create entities by category, 16 each -> total 256
    categories_buckets = [
        ("Company", companies),
        ("Task", tasks),
        ("Tool", tools),
        ("Model", models),
        ("Repository", repos),
        ("Video", videos),
        ("Robot", robots),
        ("Device", devices),
        ("MCP", mcps),
        ("Collection", collections),
        ("Personal", personal),
        ("Creative", creative),
        ("News", news),
        ("New", new_added),
        # Add two extra buckets to reach 16 categories total (we already have 14)
        ("Dataset", [f"Dataset-{i}" for i in range(1,17)]),
        ("Service", [f"Service-{i}" for i in range(1,17)])
    ]

    # ensure we have 16 items in each bucket
    for i, (etype, source_list) in enumerate(categories_buckets):
        # if list shorter than 16, duplicate with suffix
        entries = []
        for idx in range(16):
            if idx < len(source_list):
                base = source_list[idx]
            else:
                base = f"{source_list[idx % len(source_list)]} {idx}"
            name = f"{base}" if etype not in ("Repository",) else base
            desc = f"{etype} - {name} (curated synthetic record)"
            url = make_url(etype.lower(), name.replace(" ", "-"))
            source = {"name": "SyntheticCurator", "url": "https://ai-orbit.example"}
            categories = [etype]
            rec = make_entity(name=name, entity_type=etype, description=desc, url=url, source=source, categories=categories, created_at=datetime.utcnow().isoformat())
            # add specialized metadata
            if etype == "Model":
                rec["license"] = random.choice(["Apache-2.0", "MIT", "CC-BY-4.0", "proprietary"])
                rec["modalities"] = random.choice([["text"], ["image"], ["text","image"], ["audio"], ["vision","text"]])
                rec["provider"] = random.choice(companies + ["Hugging Face", "OpenAI", "Community"])
            if etype == "Repository":
                rec["stars"] = random.randint(0, 120000)
                rec["language"] = random.choice(["Python", "C++", "Rust", "Go", "JavaScript"])
                rec["last_updated"] = datetime.utcnow().isoformat()
            if etype == "MCP":
                rec["install"] = random.choice(["pip install mcp", "docker run mcp:latest", "apt-get install mcp"])
                rec["runtime"] = random.choice(["python3.10", "node16", "docker"])
            if etype == "Company":
                rec["founding_year"] = random.randint(2008, 2025)
                rec["industry_sector"] = random.choice(["Robotics", "NLP", "Computer Vision", "Edge AI", "MLOps", "Creative AI"])
                rec["headquarters"] = random.choice(["San Francisco, USA", "Berlin, Germany", "Beijing, China", "Bengaluru, India", "London, UK"])
            records.append(rec)

    # Sanity: trim to requested total if needed
    if total and len(records) > total:
        records = records[:total]

    # write generated_candidates.json
    path = os.path.join(output_dir, "generated_candidates.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(records)} synthetic candidate records to {path}")
    # also write a simple seed file
    meta = {"generated_at": datetime.utcnow().isoformat(), "count": len(records)}
    with open(os.path.join(output_dir, "generated_meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
