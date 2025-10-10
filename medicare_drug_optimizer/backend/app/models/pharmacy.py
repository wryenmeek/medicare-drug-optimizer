# backend/app/models/pharmacy.py

from pydantic import BaseModel
from typing import Optional

class Pharmacy(BaseModel):
    id: str
    name: str
    address: str
    latitude: float
    longitude: float
    network_status: str # e.g., "In-Network", "Preferred", "Mail-Order"
    distance: Optional[float] = None # Distance from user, if applicable
