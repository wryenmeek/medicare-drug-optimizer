# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.services.medicare_api_client import MedicareAPIClient
from backend.app.api.drugs import get_medicare_client
from backend.app.api import plans, drugs, pharmacies

def create_app(medicare_client=None):
    app = FastAPI()

    # Configure CORS
    origins = [
        "http://localhost:5173",  # Frontend development server
        # Add other frontend origins as needed for deployment
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    if medicare_client is None:
        medicare_client = MedicareAPIClient()

    app.dependency_overrides[get_medicare_client] = lambda: medicare_client

    app.include_router(plans.router, prefix="/api")
    app.include_router(drugs.router, prefix="/api")
    app.include_router(pharmacies.router, prefix="/api")

    return app

app = create_app()
