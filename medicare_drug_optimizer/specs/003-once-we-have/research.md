# Research: Parsing Complex Drug Restrictions

## Decision
The application will primarily rely on the `medicare.gov/api/v1/data/plan-compare/` API (Feature 007) to provide drug restrictions in a structured and simplified format. This significantly reduces the need for complex in-house parsing.

## Rationale
The user has clarified that the Medicare API provides restrictions in a structured/simplified format, making a dedicated NLP/rule-based parsing engine less critical or entirely unnecessary.

- **API as Source of Truth**: Leveraging the API directly ensures consistency with the official Medicare data and reduces the risk of misinterpretation.
- **Reduced Complexity**: Receiving structured data eliminates the need for complex NLP or rule-based parsing, simplifying the backend logic and reducing development effort.
- **Improved Maintainability**: Less custom parsing logic means fewer points of failure due to changes in formulary text formats.

## Alternatives Considered
- **Implement a Rule-Based Parsing Engine**: This was initially considered but is now **rejected** as the primary approach because the Medicare API (Feature 007) provides restrictions in a structured/simplified format. A minimal parsing component might still be needed for any remaining free-form text, but the core complexity is removed.
- **External NLP API/Service**: This was previously rejected and remains so.
- **Manual Curation**: This was previously rejected and remains so.