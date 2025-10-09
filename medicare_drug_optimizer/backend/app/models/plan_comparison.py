# backend/app/models/plan_comparison.py

from pydantic import BaseModel
from typing import List
from backend.app.models.fulfillment_plan import FulfillmentPlan

class PlanComparison(BaseModel):
    optimized_plans: List[FulfillmentPlan]
    comparison_notes: str
