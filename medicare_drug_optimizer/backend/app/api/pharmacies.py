# backend/app/api/pharmacies.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.app.services.medicare_api_client import MedicareAPIClient
from backend.app.services.pharmacy_optimizer import PharmacyOptimizer # New import
from backend.app.models.medicare_api_models import Pharmacy
from backend.app.models.user_pharmacy_preferences import UserPharmacyPreferences
from backend.app.models.pharmacy_recommendation import PharmacyRecommendation # New import

router = APIRouter()

def get_medicare_client():
    return MedicareAPIClient()

def get_pharmacy_optimizer(): # New dependency
    return PharmacyOptimizer()

# Placeholder for user preferences storage (e.g., database, session)
# For now, we'll use a simple in-memory store
user_pharmacy_preferences_db = {}

@router.get("/pharmacies", response_model=List[Pharmacy])
async def get_pharmacies(plan_id: str, zip_code: str, medicare_client: MedicareAPIClient = Depends(get_medicare_client)):
    pharmacies = medicare_client.get_pharmacies(plan_id, zip_code)
    if not pharmacies:
        raise HTTPException(status_code=404, detail="Pharmacies not found for the given plan and zip code.")
    return pharmacies

@router.get("/pharmacies/preferences", response_model=UserPharmacyPreferences)
async def get_pharmacy_preferences(user_id: str):
    if user_id not in user_pharmacy_preferences_db:
        # Return default preferences if not found
        return UserPharmacyPreferences()
    return user_pharmacy_preferences_db[user_id]

@router.post("/pharmacies/preferences", response_model=UserPharmacyPreferences)
async def update_pharmacy_preferences(user_id: str, preferences: UserPharmacyPreferences):
    user_pharmacy_preferences_db[user_id] = preferences
    return preferences

@router.get("/pharmacies/recommendations", response_model=List[PharmacyRecommendation])
async def get_pharmacy_recommendations(
    user_id: str,
    plan_id: str,
    zip_code: str,
    user_latitude: float,
    user_longitude: float,
    medicare_client: MedicareAPIClient = Depends(get_medicare_client),
    optimizer: PharmacyOptimizer = Depends(get_pharmacy_optimizer)
):
    user_preferences = user_pharmacy_preferences_db.get(user_id, UserPharmacyPreferences())
    all_pharmacies = medicare_client.get_pharmacies(plan_id, zip_code)
    if not all_pharmacies:
        raise HTTPException(status_code=404, detail="No pharmacies found for the given plan and zip code.")
    
    recommendations = optimizer.get_recommended_pharmacies(
        all_pharmacies,
        user_preferences,
        user_latitude,
        user_longitude
    )
    if not recommendations:
        raise HTTPException(status_code=404, detail="No pharmacy recommendations found based on your preferences.")
    return recommendations