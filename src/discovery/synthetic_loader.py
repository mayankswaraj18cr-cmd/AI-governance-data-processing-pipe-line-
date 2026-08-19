import json
import os
import logging

logger = logging.getLogger(__name__)

def load_candidates(output_dir):
    path = os.path.join(output_dir, "generated_candidates.json")
    if not os.path.exists(path):
        logger.warning("Synthetic candidates file not found: %s", path)
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
