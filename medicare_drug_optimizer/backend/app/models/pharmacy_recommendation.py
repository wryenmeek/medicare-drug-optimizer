# backend/app/models/pharmacy_recommendation.py

from pydantic import BaseModel
from typing import Optional
from backend.app.models.pharmacy import Pharmacy

class PharmacyRecommendation(BaseModel):
    pharmacy: Pharmacy
    reason: str
    estimated_cost_impact: Optional[float] = None
