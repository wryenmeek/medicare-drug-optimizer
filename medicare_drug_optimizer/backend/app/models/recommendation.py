# backend/app/models/recommendation.py

from pydantic import BaseModel
from typing import List, Optional

class Recommendation(BaseModel):
    plan_id: str
    pharmacy_id: str
    estimated_annual_cost: float
    notes: Optional[str] = None
