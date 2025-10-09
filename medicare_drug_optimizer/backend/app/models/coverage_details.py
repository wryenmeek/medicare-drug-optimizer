# backend/app/models/coverage_details.py

from pydantic import BaseModel
from typing import List, Optional

class CoverageDetails(BaseModel):
    plan_id: str
    drug_name: str
    is_covered: bool
    tier: Optional[str] = None
    cost_sharing: Optional[str] = None
    restrictions: List[str] = [] # Simplified list of restriction descriptions
