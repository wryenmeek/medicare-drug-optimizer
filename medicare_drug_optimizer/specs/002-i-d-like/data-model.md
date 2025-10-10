# Data Model: Covered Drug Alternatives Discovery

**Date**: 2025-10-09

## Summary
This document outlines the data models that will be used to implement the covered drug alternatives feature. These models are based on the feature specification and the research conducted in Phase 0.

## Data Models

### Drug
Represents a drug from the user's list.

**Source**: User's drug list from medicare.gov.

| Attribute | Type | Description |
|---|---|---|
| `name` | string | The brand or generic name of the drug. |
| `rxcui` | string | The RxNorm Concept Unique Identifier for the drug. |
| `ndcs` | list[string] | A list of National Drug Codes (NDCs) associated with the drug. |

### DrugAlternative
Represents a covered alternative for a drug.

**Source**: RxClass API and the user's Part D plan formulary.

| Attribute | Type | Description |
|---|---|---|
| `name` | string | The brand or generic name of the alternative drug. |
| `rxcui` | string | The RxNorm Concept Unique Identifier for the alternative drug. |
| `category` | string | The category of the alternative (e.g., "Generic", "Biosimilar"). |
| `tier` | string | The drug tier of the alternative on the user's plan. |
| `estimated_annual_cost` | float | The estimated annual cost of the alternative. |

### RxClass
Represents a drug class from the RxClass API.

**Source**: RxClass API.

| Attribute | Type | Description |
|---|---|---|
| `class_id` | string | The ID of the drug class. |
| `class_name` | string | The name of the drug class. |
| `class_type` | string | The type of the drug class. |
| `members` | list[Drug] | A list of drugs that are members of this class. |

## API Contracts

### Backend API

The backend will expose a new endpoint to retrieve the covered alternatives for a given drug.

**Endpoint**: `GET /api/drugs/{rxcui}/alternatives`

**Request Parameters**:
- `rxcui` (path): The RxCUI of the drug to find alternatives for.

**Response Body**:
A list of `DrugAlternative` objects.

```json
[
  {
    "name": "Simvastatin",
    "rxcui": "36567",
    "category": "Generic",
    "tier": "Tier 1",
    "estimated_annual_cost": 150.00
  },
  {
    "name": "Zocor",
    "rxcui": "153165",
    "category": "Brand",
    "tier": "Tier 3",
    "estimated_annual_cost": 600.00
  }
]
```
