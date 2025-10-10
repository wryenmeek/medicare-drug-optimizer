from pydantic import BaseModel

class Recommendation(BaseModel):
    recommendation_type: str # e.g., "SWITCH_TO_GENERIC", "USE_PREFERRED_PHARMACY"
    description: str
    estimated_savings: float