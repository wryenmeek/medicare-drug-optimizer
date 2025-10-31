from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.app.services.medicare_api_client import MedicareAPIClient
from backend.app.models.medicare_api_models import Plan

router = APIRouter()

def get_medicare_client():
    return MedicareAPIClient()

@router.get("/plans", response_model=List[Plan])
async def get_plans(zip_code: str, county: str, medicare_client: MedicareAPIClient = Depends(get_medicare_client)):
    plans = medicare_client.get_plans(zip_code, county)
    if not plans:
        raise HTTPException(status_code=404, detail="Plans not found for the given zip code and county.")
    return plans
