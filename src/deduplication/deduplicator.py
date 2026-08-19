from rapidfuzz import fuzz, process
import logging

logger = logging.getLogger(__name__)

class Deduplicator:
    def __init__(self, threshold=92):
        self.threshold = threshold
        self.name_index = {}

    def is_duplicate(self, name, existing_names):
        if not existing_names:
            return None
        match = process.extractOne(name, existing_names, scorer=fuzz.token_sort_ratio)
        if not match:
            return None
        matched_name, score, _ = match
        if score >= self.threshold:
            return matched_name
        return None

    def deduplicate_batch(self, entities):
        canonical = {}
        existing_names = []
        deduped = []
        for e in entities:
            name = e.get("name", "")
            dup = self.is_duplicate(name, existing_names)
            if dup:
                # find canonical entry and merge light metadata
                found = next((x for x in deduped if x["name"] == dup), None)
                if found:
                    found["categories"] = list(set(found.get("categories", []) + e.get("categories", [])))
                    # prefer longer description if canonical missing
                    if not found.get("description") and e.get("description"):
                        found["description"] = e.get("description")
                    canonical[name] = found["id"]
                else:
                    canonical[name] = None
            else:
                existing_names.append(name)
                deduped.append(e)
                canonical[name] = e["id"]
        return deduped, canonical
