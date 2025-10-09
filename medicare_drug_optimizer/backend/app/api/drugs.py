# backend/app/api/drugs.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from backend.app.services.medicare_api_client import MedicareAPIClient
from backend.app.services.drug_alternatives_processor import DrugAlternativesProcessor
from backend.app.services.drug_coverage_processor import DrugCoverageProcessor # New import
from backend.app.models.medicare_api_models import DrugInfo
from backend.app.models.drug_alternative import DrugAlternative
from backend.app.models.coverage_details import CoverageDetails # New import

router = APIRouter()

def get_medicare_client():
    return MedicareAPIClient()

def get_drug_alternatives_processor():
    return DrugAlternativesProcessor()

def get_drug_coverage_processor(): # New dependency
    return DrugCoverageProcessor()

@router.get("/drugs", response_model=DrugInfo)
async def get_drugs(plan_id: str, drug_name: str, medicare_client: MedicareAPIClient = Depends(get_medicare_client)):
    drug_info = medicare_client.get_drugs(plan_id, drug_name)
    if not drug_info:
        raise HTTPException(status_code=404, detail="Drug information not found for the given plan and drug.")
    return drug_info

@router.get("/drugs/alternatives", response_model=List[DrugAlternative])
async def get_drug_alternatives(
    plan_id: str,
    drug_name: str,
    medicare_client: MedicareAPIClient = Depends(get_medicare_client),
    processor: DrugAlternativesProcessor = Depends(get_drug_alternatives_processor)
):
    drug_info = medicare_client.get_drugs(plan_id, drug_name)
    if not drug_info:
        raise HTTPException(status_code=404, detail="Drug information not found for the given plan and drug to find alternatives.")
    
    alternatives = processor.process_alternatives(drug_info)
    if not alternatives:
        raise HTTPException(status_code=404, detail="No drug alternatives found for the given drug.")
    return alternatives

@router.get("/drugs/coverage", response_model=CoverageDetails) # New endpoint
async def get_drug_coverage(
    plan_id: str,
    drug_name: str,
    medicare_client: MedicareAPIClient = Depends(get_medicare_client),
    processor: DrugCoverageProcessor = Depends(get_drug_coverage_processor)
):
    drug_info = medicare_client.get_drugs(plan_id, drug_name)
    if not drug_info:
        raise HTTPException(status_code=404, detail="Drug information not found for the given plan and drug to check coverage.")
    
    coverage_details = processor.process_coverage(drug_info, plan_id)
    if not coverage_details:
        raise HTTPException(status_code=404, detail="Drug coverage details not found for the given drug.")
    return coverage_details
