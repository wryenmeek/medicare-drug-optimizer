# backend/app/models/drug.py

from pydantic import BaseModel
from typing import Optional

class Drug(BaseModel):
    drug_name: str
    ndc_code: Optional[str] = None
    dosage: Optional[str] = None
    quantity: Optional[int] = None
    frequency: Optional[str] = None
