import logging

logger = logging.getLogger(__name__)

TASK_KEYWORDS = ["summarize", "translate", "classify", "generate", "detect", "segment", "qa", "search", "annotate"]
TOOL_KEYWORDS = ["studio", "platform", "app", "service", "tool", "dashboard"]
COMPANY_KEYWORDS = ["inc", "llc", "labs", "systems", "corporation", "company", "co."]

def classify_entity(entity):
    name = (entity.get("name") or "").lower()
    desc = (entity.get("description") or "").lower()
    categories = set(entity.get("categories") or [])
    if any(k in name or k in desc for k in TASK_KEYWORDS):
        categories.add("Task")
    if any(k in name or k in desc for k in TOOL_KEYWORDS):
        categories.add("Tool")
    if any(k in name or k in desc for k in COMPANY_KEYWORDS):
        categories.add("Company")
    if entity.get("entity_type"):
        categories.add(entity["entity_type"])
    entity["categories"] = sorted(categories)
    return entity
