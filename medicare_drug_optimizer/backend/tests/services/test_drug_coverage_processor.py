# backend/tests/services/test_drug_coverage_processor.py

import pytest
from backend.app.services.drug_coverage_processor import DrugCoverageProcessor
from backend.app.models.medicare_api_models import DrugInfo, DrugRestriction
from backend.app.models.coverage_details import CoverageDetails

def test_processor_initialization():
    processor = DrugCoverageProcessor()
    assert isinstance(processor, DrugCoverageProcessor)

def test_process_coverage_returns_coverage_details():
    processor = DrugCoverageProcessor()
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[],
        restrictions=[
            DrugRestriction(type="QL", simplifiedText="Limit 30 per month", rawText="Limit 30 per month"),
        ]
    )
    plan_id = "test_plan"
    coverage = processor.process_coverage(mock_drug_info, plan_id)
    assert isinstance(coverage, CoverageDetails)
    assert coverage.plan_id == plan_id
    assert coverage.drug_name == "TestDrug"
    assert coverage.is_covered == True
    assert "Limit 30 per month" in coverage.restrictions

def test_process_coverage_no_restrictions():
    processor = DrugCoverageProcessor()
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[],
        restrictions=[]
    )
    plan_id = "test_plan"
    coverage = processor.process_coverage(mock_drug_info, plan_id)
    assert isinstance(coverage, CoverageDetails)
    assert len(coverage.restrictions) == 0
