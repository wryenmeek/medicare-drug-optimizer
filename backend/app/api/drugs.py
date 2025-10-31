from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from backend.app.services.medicare_api_client import MedicareAPIClient
from backend.app.models.medicare_api_models import DrugInfo
from backend.app.services.rxclass_api_client import RxClassAPIClient
from backend.app.services.drug_alternatives_service import DrugAlternativesService
from backend.app.models.drug_alternative import DrugAlternative

router = APIRouter()

def get_medicare_client():
    return MedicareAPIClient()

def get_rxclass_client():
    return RxClassAPIClient()

def get_drug_alternatives_service(rxclass_client: RxClassAPIClient = Depends(get_rxclass_client)):
    return DrugAlternativesService(rxclass_client)

@router.get("/drugs", response_model=DrugInfo)
async def get_drugs(plan_id: str, drug_name: str, medicare_client: MedicareAPIClient = Depends(get_medicare_client)):
    drug_info = medicare_client.get_drugs(plan_id, drug_name)
    if not drug_info:
        raise HTTPException(status_code=404, detail="Drug information not found for the given plan and drug.")
    return drug_info

@router.get("/drugs/{rxcui}/alternatives", response_model=List[DrugAlternative])
async def get_drug_alternatives(rxcui: str, alternatives_service: DrugAlternativesService = Depends(get_drug_alternatives_service)):
    alternatives = alternatives_service.get_alternatives(rxcui)
    if not alternatives:
        raise HTTPException(status_code=404, detail="No alternatives found for the given drug.")
    return alternatives