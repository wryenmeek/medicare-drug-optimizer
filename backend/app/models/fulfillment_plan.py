# backend/app/models/fulfillment_plan.py

from pydantic import BaseModel
from typing import List, Optional
from backend.app.models.partd_plan import PartDPlan
from backend.app.models.pharmacy import Pharmacy
from backend.app.models.drug import Drug

class FulfillmentPlan(BaseModel):
    plan: PartDPlan
    pharmacy: Pharmacy
    drugs_covered: List[Drug]
    estimated_annual_cost: float
    notes: Optional[str] = None
