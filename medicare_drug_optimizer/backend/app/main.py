# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.services.medicare_api_client import MedicareAPIClient
from backend.app.api import plans, drugs, pharmacies # New import

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

medicare_client = MedicareAPIClient()

app.include_router(plans.router, prefix="/api")
app.include_router(drugs.router, prefix="/api")
app.include_router(pharmacies.router, prefix="/api") # New line

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI!"}

# API endpoints for plans, drugs, pharmacies will be added here in later tasks
