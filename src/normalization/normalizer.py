from src.utils.http import normalize_url
import unicodedata

def normalize_text(s: str) -> str:
    if not s:
        return ""
    s = unicodedata.normalize("NFKC", s)
    return " ".join(s.split())

def normalize_entity(entity: dict) -> dict:
    if "name" in entity:
        entity["name"] = normalize_text(entity["name"])
    if "description" in entity and entity["description"]:
        entity["description"] = normalize_text(entity["description"])
    if "url" in entity and entity["url"]:
        entity["url"] = normalize_url(entity["url"])
    if "source" in entity and isinstance(entity["source"], dict) and entity["source"].get("url"):
        entity["source"]["url"] = normalize_url(entity["source"]["url"])
    return entity
