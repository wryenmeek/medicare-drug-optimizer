# Data Model

This feature introduces new entities to represent pharmacies, user preferences for pharmacy selection, and the resulting pharmacy recommendations.

## Entities

### Pharmacy
Represents a retail or mail-order pharmacy.

- **pharmacy_id**: Unique identifier for the pharmacy.
- **name**: The name of the pharmacy (e.g., "CVS Pharmacy").
- **address**: Full street address.
- **latitude**: Geographic latitude coordinate.
- **longitude**: Geographic longitude coordinate.
- **contact_info**: Phone number, website, etc.
- **network_status**: Status within the user's Part D plan (e.g., "In-Network", "Preferred", "Mail-Order").
- **hours_of_operation**: (Optional) Daily operating hours.

### UserPharmacyPreferences
Represents a user's saved criteria for pharmacy selection.

- **user_id**: Identifier for the user.
- **max_travel_distance_miles**: Maximum distance in miles the user is willing to travel.
- **max_num_pharmacies**: Maximum number of distinct pharmacies the user is willing to use.
- **excluded_pharmacies**: A list of `pharmacy_id`s that the user wishes to exclude from recommendations.

### PharmacyRecommendation
Represents a suggested pharmacy or combination of pharmacies that optimizes cost based on user preferences.

- **recommendation_id**: Unique identifier for the recommendation.
- **pharmacy_ids**: A list of `pharmacy_id`s included in this recommendation.
- **estimated_cost_savings**: The estimated annual cost savings if this recommendation is followed.
- **reason**: Explanation for why this recommendation is optimal (e.g., "Preferred network pharmacy").
