import { rest } from 'msw';

import { http, HttpResponse } from 'msw';

export const handlers = [
  http.get('/api/drugs/:rxcui/alternatives', () => {
    return HttpResponse.json([
        {
          name: 'Simvastatin',
          rxcui: '36567',
          category: 'Generic',
          tier: 'Tier 1',
          estimated_annual_cost: 150.0,
        },
        {
          name: 'Zocor',
          rxcui: '153165',
          category: 'Brand',
          tier: 'Tier 3',
          estimated_annual_cost: 600.0,
        },
      ])
  }),
];
