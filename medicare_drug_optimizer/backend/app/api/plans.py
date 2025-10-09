# backend/app/api/plans.py

from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from backend.app.services.medicare_api_client import MedicareAPIClient
from backend.app.services.optimization_service import OptimizationService # New import
from backend.app.models.medicare_api_models import Plan
from backend.app.models.partd_plan import PartDPlan # New import
from backend.app.models.drug import Drug # New import
from backend.app.models.fulfillment_plan import FulfillmentPlan # New import

router = APIRouter()

def get_medicare_client():
    return MedicareAPIClient()

def get_optimization_service(): # New dependency
    return OptimizationService()

@router.get("/plans", response_model=List[Plan])
async def get_plans(zip_code: str, county: str, medicare_client: MedicareAPIClient = Depends(get_medicare_client)):
    plans = medicare_client.get_plans(zip_code, county)
    if not plans:
        raise HTTPException(status_code=404, detail="Plans not found for the given zip code and county.")
    return plans

@router.get("/plans/optimized", response_model=List[FulfillmentPlan])
async def get_optimized_plans(
    zip_code: str,
    county: str,
    drug_names: List[str] = Query(None), # Assuming drug names are passed as a list
    medicare_client: MedicareAPIClient = Depends(get_medicare_client),
    optimizer: OptimizationService = Depends(get_optimization_service)
):
    # Fetch all plans and pharmacies for the given zip code and county
    all_plans = medicare_client.get_plans(zip_code, county)
    if not all_plans:
        raise HTTPException(status_code=404, detail="No plans found for the given zip code and county.")

    all_pharmacies = medicare_client.get_pharmacies(all_plans[0].id, zip_code) # Using first plan's ID for pharmacies
    if not all_pharmacies:
        raise HTTPException(status_code=404, detail="No pharmacies found for the given plan and zip code.")

    # Create dummy Drug objects for now
    drugs = [Drug(drug_name=name) for name in drug_names]

    optimized_plans = optimizer.optimize_plans(all_plans, drugs, all_pharmacies)
    if not optimized_plans:
        raise HTTPException(status_code=404, detail="No optimized plans found.")
    return optimized_plans