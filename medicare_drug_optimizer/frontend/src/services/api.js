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


};

export default api;
