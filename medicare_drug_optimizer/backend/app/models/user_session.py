from pydantic import BaseModel
from typing import List, Optional
from backend.app.models.partd_plan import PartDPlan
from backend.app.models.drug import Drug

class UserSession(BaseModel):
    session_id: str
    part_d_plan: Optional[PartDPlan] = None
    drug_list: List[Drug] = []
    lifecycle_state: str = "Created" # e.g., "Created", "Active", "Saved", "Loaded", "Expired"