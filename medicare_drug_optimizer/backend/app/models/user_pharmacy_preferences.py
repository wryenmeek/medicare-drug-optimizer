# backend/app/models/user_pharmacy_preferences.py

from pydantic import BaseModel
from typing import List, Optional

class UserPharmacyPreferences(BaseModel):
    preferred_pharmacy_ids: List[str] = []
    max_travel_distance: Optional[float] = None # in miles
    allow_mail_order: bool = False
