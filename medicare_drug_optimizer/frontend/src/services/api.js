// frontend/src/services/api.js

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export const fetchPlans = async (zip, county) => {
  const response = await fetch(`${API_BASE_URL}/api/plans?zip=${zip}&county=${county}`);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
};

export const fetchDrugs = async (planId, drugName) => {
  const response = await fetch(`${API_BASE_URL}/api/drugs?planId=${planId}&drugName=${drugName}`);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
};

export const fetchPharmacies = async (planId, zip) => {
  const response = await fetch(`${API_BASE_URL}/api/pharmacies?planId=${planId}&zip=${zip}`);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
};

export const fetchDrugAlternatives = async (planId, drugName) => {
  const response = await fetch(`${API_BASE_URL}/api/drugs/alternatives?planId=${planId}&drugName=${drugName}`);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
};

export const fetchDrugCoverage = async (planId, drugName) => {
  const response = await fetch(`${API_BASE_URL}/api/drugs/coverage?planId=${planId}&drugName=${drugName}`);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
};

export const fetchPharmacyPreferences = async (userId) => {
  const response = await fetch(`${API_BASE_URL}/api/pharmacies/preferences?user_id=${userId}`);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
};

export const updatePharmacyPreferences = async (userId, preferences) => {
  const response = await fetch(`${API_BASE_URL}/api/pharmacies/preferences?user_id=${userId}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(preferences),
  });
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
};

export const fetchPharmacyRecommendations = async (userId, planId, zipCode, userLatitude, userLongitude) => {
  const response = await fetch(`${API_BASE_URL}/api/pharmacies/recommendations?user_id=${userId}&plan_id=${planId}&zip_code=${zipCode}&user_latitude=${userLatitude}&user_longitude=${userLongitude}`);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
};

export const fetchOptimizedPlans = async (zipCode, county, drugNames) => {
  const response = await fetch(`${API_BASE_URL}/api/plans/optimized?zip_code=${zipCode}&county=${county}&drug_names=${drugNames.join(',')}`);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
};
