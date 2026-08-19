import os
from dotenv import load_dotenv
from types import SimpleNamespace

def load_config():
    load_dotenv()
    cfg = SimpleNamespace()
    cfg.github_token = os.getenv("GITHUB_TOKEN")
    cfg.huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
    cfg.youtube_api_key = os.getenv("YOUTUBE_API_KEY")
    cfg.max_records = int(os.getenv("MAX_RECORDS", "300"))
    cfg.output_dir = os.getenv("OUTPUT_DIR", "data")
    cfg.log_level = os.getenv("LOG_LEVEL", "INFO")
    cfg.user_agent = os.getenv("USER_AGENT", "ai-orbit-ingest/1.0")
    return cfg
