from pydantic import BaseModel
from typing import Optional

class Drug(BaseModel):
    drug_name: str
    dosage: Optional[str] = None
    quantity: Optional[int] = None
    frequency: Optional[str] = None