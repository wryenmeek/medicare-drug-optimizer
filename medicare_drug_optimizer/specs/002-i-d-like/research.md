# Research: Covered Drug Alternatives Discovery

**Date**: 2025-10-09

## Summary
This research phase was conducted to identify the best approach for finding covered drug alternatives as required by the feature specification. The primary goal was to find a reliable data source or API that can provide relationships between drugs, which can then be used to find alternatives on a user's Part D plan.

## Findings
The research revealed that there is no single, dedicated "drug alternatives" API provided by medicare.gov. However, several APIs and data sources can be combined to achieve the desired functionality.

The most promising data source is the **RxNav APIs** provided by the National Library of Medicine (NLM). Specifically, the **RxClass API** allows for the retrieval of drug classes and their members. This is a powerful tool for identifying not only generic/brand relationships but also therapeutic alternatives.

Other considered options included:
- **Picwell's Medicare API**: This is a commercial API that provides some drug search capabilities, but it is not a free/public government source.
- **Medicare Claims Data to Prescription Drug Plan Sponsors (AB2D) API**: This API is restricted to Prescription Drug Plan (PDP) sponsors and not available for general use.
- **Marketplace API**: This API is for checking drug coverage on health insurance plans, but does not provide information about alternatives.

## Decision
Based on the research, the implementation will leverage the **RxClass API** from the RxNav suite of APIs. This API provides the necessary information to identify drug relationships, which can then be filtered against the user's plan formulary to determine coverage.

This approach aligns with the technical context of the project (Python backend making API calls) and provides a reliable, government-maintained data source.