import requests
from typing import List, Optional
from backend.app.models.medicare_api_models import Plan, DrugInfo, Pharmacy

class MedicareAPIClient:
    BASE_URL = "https://www.medicare.gov/api/v1/data/plan-compare/"
    HEADERS = {"Referer": "https://www.medicare.gov/plan-compare/"}

    def _make_request(self, endpoint: str, params: dict) -> Optional[dict]:
        try:
            response = requests.get(f"{self.BASE_URL}{endpoint}", params=params, headers=self.HEADERS, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request to {endpoint} failed: {e}")
            return None

    def get_plans(self, zip_code: str, county: str) -> Optional[List[Plan]]:
        params = {"zip": zip_code, "county": county}
        data = self._make_request("plans", params)
        if data and "plans" in data:
            return [Plan(**p) for p in data["plans"]]
        return None

    def get_drugs(self, plan_id: str, drug_name: str) -> Optional[DrugInfo]:
        params = {"planId": plan_id, "drugName": drug_name}
        data = self._make_request("drugs", params)
        if data and "drugInfoList" in data and data["drugInfoList"]:
            return DrugInfo(**data["drugInfoList"][0])
        return None

    def get_pharmacies(self, plan_id: str, zip_code: str) -> Optional[List[Pharmacy]]:
        params = {"planId": plan_id, "zip": zip_code}
        data = self._make_request("pharmacies", params)
        if data and "pharmacies" in data:
            return [Pharmacy(**p) for p in data["pharmacies"]]
        return None
