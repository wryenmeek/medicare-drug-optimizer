from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from backend.app.services.medicare_api_client import MedicareAPIClient
from backend.app.models.medicare_api_models import DrugInfo

router = APIRouter()

def get_medicare_client():
    return MedicareAPIClient()

@router.get("/drugs", response_model=DrugInfo)
async def get_drugs(plan_id: str, drug_name: str, medicare_client: MedicareAPIClient = Depends(get_medicare_client)):
    drug_info = medicare_client.get_drugs(plan_id, drug_name)
    if not drug_info:
        raise HTTPException(status_code=404, detail="Drug information not found for the given plan and drug.")
    return drug_info