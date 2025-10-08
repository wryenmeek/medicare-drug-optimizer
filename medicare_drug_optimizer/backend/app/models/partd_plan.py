# backend/app/models/partd_plan.py

from pydantic import BaseModel
from typing import Optional

class PartDPlan(BaseModel):
    plan_id: str
    plan_name: str
    carrier_name: str
    monthly_premium: float
    deductible: float
    out_of_pocket_max: float
    formulary_url: Optional[str] = None
