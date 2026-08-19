from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime
import uuid

class SourceInfo(BaseModel):
    name: str
    url: Optional[HttpUrl]

class BaseEntity(BaseModel):
    id: str
    entity_type: str
    name: str
    description: Optional[str]
    url: Optional[str]
    categories: List[str] = []
    source: SourceInfo
    created_at: str

    @classmethod
    def stable_uuid(cls, name: str, namespace: str = "ai-orbit"):
        ns = uuid.uuid5(uuid.NAMESPACE_DNS, namespace)
        return str(uuid.uuid5(ns, name.lower().strip()))
