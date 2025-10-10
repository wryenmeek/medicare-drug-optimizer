from pydantic import BaseModel, Field
from typing import Optional

class PartDPlan(BaseModel):
    plan_id: str
    plan_name: str
    issuer: str
    formulary_url: Optional[str] = None
    annual_deductible: Optional[str] = None
    drug_plan_deductible: Optional[int] = None
    partb_premium_reduction: Optional[float] = None
    partc_premium: Optional[int] = None
    monthly_premium: Optional[float] = Field(None, alias='partd_premium')
    annual_drugs_total: Optional[int] = None
    maximum_oopc: Optional[str] = None
    calculated_monthly_premium: Optional[float] = None