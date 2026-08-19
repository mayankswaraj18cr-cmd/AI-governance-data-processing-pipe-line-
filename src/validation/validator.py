import logging

logger = logging.getLogger(__name__)

REQUIRED_FIELDS = ["id", "entity_type", "name", "source", "created_at"]

def validate_entity(e: dict) -> (bool, list):
    errs = []
    for f in REQUIRED_FIELDS:
        if f not in e or e[f] in (None, "", []):
            errs.append(f"missing:{f}")
    return (len(errs) == 0, errs)
