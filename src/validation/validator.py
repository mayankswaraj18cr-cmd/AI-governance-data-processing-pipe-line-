import logging

logger = logging.getLogger(__name__)

class RelationshipGraph:
    def __init__(self):
        self.edges = []

    def add(self, a_id, relation, b_id, metadata=None):
        self.edges.append({
            "from": a_id,
            "relation": relation,
            "to": b_id,
            "metadata": metadata or {}
        })

    def export(self):
        return {"relationships": self.edges}
