from pydantic import BaseModel
from typing import Optional

class PartDPlan(BaseModel):
    plan_id: str
    plan_name: str
    issuer: str
    formulary_url: Optional[str] = None