# backend/app/services/medicare_api_client.py

import requests
import logging # New import
from typing import List, Optional, Dict, Any
from backend.app.models.medicare_api_models import Plan, DrugInfo, Pharmacy

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MedicareAPIClient:
    BASE_URL = "https://www.medicare.gov/api/v1/data/plan-compare/"
    REFERER_HEADER = {"Referer": "https://www.medicare.gov/plan-compare/"}

    def _make_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        url = f"{self.BASE_URL}{endpoint}"
        try:
            logging.info(f"Making API request to: {url} with params: {params}")
            response = requests.get(url, headers=self.REFERER_HEADER, params=params, timeout=10) # Added timeout
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            logging.info(f"API request to {endpoint} successful.")
            return response.json()
        except requests.exceptions.Timeout:
            logging.error(f"API request to {endpoint} timed out after 10 seconds.")
            return None
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err} - Response: {response.text}")
            return None
        except requests.exceptions.ConnectionError as conn_err:
            logging.error(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            logging.error(f"An unexpected request error occurred: {req_err}")
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred during API request: {e}")
            return None

    def get_plans(self, zip_code: str, county: str) -> Optional[List[Plan]]:
        endpoint = "plans"
        params = {"zip": zip_code, "county": county}
        raw_data = self._make_request(endpoint, params)
        return self._map_plans(raw_data)

    def get_drugs(self, plan_id: str, drug_name: str) -> Optional[DrugInfo]:
        endpoint = "drugs"
        params = {"planId": plan_id, "drugName": drug_name}
        raw_data = self._make_request(endpoint, params)
        return self._map_drug_info(raw_data)

    def get_pharmacies(self, plan_id: str, zip_code: str) -> Optional[List[Pharmacy]]:
        endpoint = "pharmacies"
        params = {"planId": plan_id, "zip": zip_code}
        raw_data = self._make_request(endpoint, params)
        return self._map_pharmacies(raw_data)

    # Data mapping methods (new for T016)
    def _map_plans(self, raw_data: Dict[str, Any]) -> Optional[List[Plan]]:
        if raw_data and 'plans' in raw_data:
            return [Plan(**plan_data) for plan_data in raw_data['plans']]
        logging.warning("No 'plans' data found in raw API response for plans.")
        return None

    def _map_drug_info(self, raw_data: Dict[str, Any]) -> Optional[DrugInfo]:
        if raw_data and 'drugInfoList' in raw_data and raw_data['drugInfoList']:
            # Assuming drugInfoList contains a single DrugInfo object or we take the first
            return DrugInfo(**raw_data['drugInfoList'][0])
        logging.warning("No 'drugInfoList' data found in raw API response for drugs.")
        return None

    def _map_pharmacies(self, raw_data: Dict[str, Any]) -> Optional[List[Pharmacy]]:
        if raw_data and 'pharmacies' in raw_data and 'features' in raw_data['pharmacies']:
            # Assuming pharmacies are within 'features' list and properties contain the data
            return [Pharmacy(**feature['properties']) for feature in raw_data['pharmacies']['features']]
        return None