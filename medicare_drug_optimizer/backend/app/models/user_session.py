# backend/app/models/user_session.py

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserSession(BaseModel):
    session_id: str
    zip_code: str
    county: str
    drugs: List[str] = []
    pharmacy_preferences: Optional[dict] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
