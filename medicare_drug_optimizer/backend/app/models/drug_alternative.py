# backend/app/models/drug_alternative.py

from pydantic import BaseModel
from typing import Optional

class DrugAlternative(BaseModel):
    name: str
    category: str # Enum: "Brand", "Generic", "Branded Generic", "Biosimilar", "Interchangeable Biologic"
    estimated_annual_cost: float
    plan_id: Optional[str] = None
