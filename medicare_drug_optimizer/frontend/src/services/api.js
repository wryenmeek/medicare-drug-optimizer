const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';

const api = {
  getPlans: async (zipCode, county) => {
    try {
      const response = await fetch(`${API_BASE_URL}/plans?zip_code=${zipCode}&county=${county}`);
      if (!response.ok) {
        const errorData = await response.json();
        console.error(`Error fetching plans: ${response.status} - ${errorData.detail}`);
        throw new Error(errorData.detail || `Error fetching plans: ${response.statusText}`);
      }
      return response.json();
    } catch (error) {
      console.error("Network error or unexpected issue fetching plans:", error);
      throw error;
    }
  },

  getDrugs: async (planId, drugName) => {
    try {
      const response = await fetch(`${API_BASE_URL}/drugs?plan_id=${planId}&drug_name=${drugName}`);
      if (!response.ok) {
        const errorData = await response.json();
        console.error(`Error fetching drug info: ${response.status} - ${errorData.detail}`);
        throw new Error(errorData.detail || `Error fetching drug info: ${response.statusText}`);
      }
      return response.json();
    } catch (error) {
      console.error("Network error or unexpected issue fetching drug info:", error);
      throw error;
    }
  },

  getPharmacies: async (planId, zipCode) => {
    try {
      const response = await fetch(`${API_BASE_URL}/pharmacies?plan_id=${planId}&zip_code=${zipCode}`);
      if (!response.ok) {
        const errorData = await response.json();
        console.error(`Error fetching pharmacies: ${response.status} - ${errorData.detail}`);
        throw new Error(errorData.detail || `Error fetching pharmacies: ${response.statusText}`);
      }
      return response.json();
    } catch (error) {
      console.error("Network error or unexpected issue fetching pharmacies:", error);
      throw error;
    }
  },

  getOptimizedPlans: async (zipCode, county, drugNames) => {
    try {
      const drugNamesQuery = drugNames.map(name => `drug_names=${encodeURIComponent(name)}`).join('&');
      const response = await fetch(`${API_BASE_URL}/plans/optimized?zip_code=${zipCode}&county=${county}&${drugNamesQuery}`);
      if (!response.ok) {
        const errorData = await response.json();
        console.error(`Error fetching optimized plans: ${response.status} - ${errorData.detail}`);
        throw new Error(errorData.detail || `Error fetching optimized plans: ${response.statusText}`);
      }
      return response.json();
    } catch (error) {
      console.error("Network error or unexpected issue fetching optimized plans:", error);
      throw error;
    }
  },

  getDrugAlternatives: async (planId, drugName) => {
    try {
      const response = await fetch(`${API_BASE_URL}/drugs/alternatives?plan_id=${planId}&drug_name=${drugName}`);
      if (!response.ok) {
        const errorData = await response.json();
        console.error(`Error fetching drug alternatives: ${response.status} - ${errorData.detail}`);
        throw new Error(errorData.detail || `Error fetching drug alternatives: ${response.statusText}`);
      }
      return response.json();
    } catch (error) {
      console.error("Network error or unexpected issue fetching drug alternatives:", error);
      throw error;
    }
  },

  getDrugCoverage: async (planId, drugName) => {
    try {
      const response = await fetch(`${API_BASE_URL}/drugs/coverage?plan_id=${planId}&drug_name=${drugName}`);
      if (!response.ok) {
        const errorData = await response.json();
        console.error(`Error fetching drug coverage: ${response.status} - ${errorData.detail}`);
        throw new Error(errorData.detail || `Error fetching drug coverage: ${response.statusText}`);
      }
      return response.json();
    } catch (error) {
      console.error("Network error or unexpected issue fetching drug coverage:", error);
      throw error;
    }
  },

  getPharmacyPreferences: async (userId) => {
    try {
      const response = await fetch(`${API_BASE_URL}/pharmacies/preferences?user_id=${userId}`);
      if (!response.ok) {
        const errorData = await response.json();
        console.error(`Error fetching pharmacy preferences: ${response.status} - ${errorData.detail}`);
        throw new Error(errorData.detail || `Error fetching pharmacy preferences: ${response.statusText}`);
      }
      return response.json();
    } catch (error) {
      console.error("Network error or unexpected issue fetching pharmacy preferences:", error);
      throw error;
    }
  },

  updatePharmacyPreferences: async (userId, preferences) => {
    try {
      const response = await fetch(`${API_BASE_URL}/pharmacies/preferences?user_id=${userId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(preferences),
      });
      if (!response.ok) {
        const errorData = await response.json();
        console.error(`Error updating pharmacy preferences: ${response.status} - ${errorData.detail}`);
        throw new Error(errorData.detail || `Error updating pharmacy preferences: ${response.statusText}`);
      }
      return response.json();
    } catch (error) {
      console.error("Network error or unexpected issue updating pharmacy preferences:", error);
      throw error;
    }
  },

  getPharmacyRecommendations: async (userId, planId, zipCode, userLatitude, userLongitude) => {
    try {
      const response = await fetch(`${API_BASE_URL}/pharmacies/recommendations?user_id=${userId}&plan_id=${planId}&zip_code=${zipCode}&user_latitude=${userLatitude}&user_longitude=${userLongitude}`);
      if (!response.ok) {
        const errorData = await response.json();
        console.error(`Error fetching pharmacy recommendations: ${response.status} - ${errorData.detail}`);
        throw new Error(errorData.detail || `Error fetching pharmacy recommendations: ${response.statusText}`);
      }
      return response.json();
    } catch (error) {
      console.error("Network error or unexpected issue fetching pharmacy recommendations:", error);
      throw error;
    }
  },
};

export default api;
