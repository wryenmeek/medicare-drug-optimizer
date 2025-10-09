# backend/app/models/user_session.py

from datetime import datetime

from pydantic import BaseModel


class UserSession(BaseModel):
    session_id: str
    zip_code: str
    county: str
    drugs: list[str] = []
    pharmacy_preferences: dict | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
