const BASE_URL = '/api';

export const getDrugAlternatives = async (rxcui) => {
  const response = await fetch(`${BASE_URL}/drugs/${rxcui}/alternatives`);
  if (!response.ok) {
    throw new Error('Failed to fetch drug alternatives');
  }
  return response.json();
};
