#!/usr/bin/env python3
"""
Run the AI Orbit ingestion pipeline (synthetic-data mode).
This script will:
 - generate a curated synthetic dataset (data/generated_candidates.json)
 - run the modular pipeline (cleaning, normalization, dedup, classification, relationships, validation)
 - output final cleaned records to data/records.json and relationships.json
"""
import logging
import os
from src.config import load_config
from src.pipeline import AIOOrbitPipeline
from src.data_generator.generator import generate_and_write_dataset

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    cfg = load_config()
    os.makedirs(cfg.output_dir, exist_ok=True)

    # Generate a curated synthetic candidate set (256 records)
    generate_and_write_dataset(cfg.output_dir, seed=42, total=256)

    # Run pipeline which reads candidates and creates final records.json + relationships.json
    pipeline = AIOOrbitPipeline(cfg, use_synthetic=True)
    pipeline.run()

if __name__ == "__main__":
    main()
