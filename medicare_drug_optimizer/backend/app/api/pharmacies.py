from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.app.services.medicare_api_client import MedicareAPIClient
from backend.app.models.medicare_api_models import Pharmacy

router = APIRouter()

def get_medicare_client():
    return MedicareAPIClient()

@router.get("/pharmacies", response_model=List[Pharmacy])
async def get_pharmacies(plan_id: str, zip_code: str, medicare_client: MedicareAPIClient = Depends(get_medicare_client)):
    pharmacies = medicare_client.get_pharmacies(plan_id, zip_code)
    if not pharmacies:
        raise HTTPException(status_code=404, detail="Pharmacies not found for the given plan and zip code.")
    return pharmacies
