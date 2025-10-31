# backend/app/models/medicare_api_models.py

from pydantic import BaseModel, Field
from typing import List, Optional

class Plan(BaseModel):
    id: str
    name: str
    issuer: str
    formularyUrl: Optional[str] = None

class DrugAlternative(BaseModel):
    name: str
    category: str # Enum: "Brand", "Generic", "Branded Generic", "Biosimilar", "Interchangeable Biologic"
    estimatedAnnualCost: float

class DrugRestriction(BaseModel):
    type: str # Enum: "QL", "PA", "ST"
    simplifiedText: str
    rawText: str

class DrugInfo(BaseModel):
    drugName: str
    alternatives: List[DrugAlternative]
    restrictions: List[DrugRestriction]

class Pharmacy(BaseModel):
    id: str
    name: str
    address: str
    latitude: float
    longitude: float
    networkStatus: str # Enum: "In-Network", "Preferred", "Mail-Order"
