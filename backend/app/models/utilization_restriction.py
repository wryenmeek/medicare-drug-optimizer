# backend/app/models/utilization_restriction.py

from pydantic import BaseModel
from typing import Optional

class UtilizationRestriction(BaseModel):
    type: str # e.g., QL, PA, ST
    description: str
    raw_text: Optional[str] = None
