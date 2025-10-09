# backend/tests/services/test_drug_alternatives_processor.py

import pytest
from backend.app.services.drug_alternatives_processor import DrugAlternativesProcessor
from backend.app.models.medicare_api_models import DrugInfo, DrugAlternative, DrugRestriction

def test_processor_initialization():
    processor = DrugAlternativesProcessor()
    assert isinstance(processor, DrugAlternativesProcessor)

def test_process_alternatives_returns_existing_alternatives():
    processor = DrugAlternativesProcessor()
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[
            DrugAlternative(name="Alt1", category="Generic", estimatedAnnualCost=50.0),
            DrugAlternative(name="Alt2", category="Brand", estimatedAnnualCost=100.0),
        ],
        restrictions=[]
    )
    alternatives = processor.process_alternatives(mock_drug_info)
    assert isinstance(alternatives, list)
    assert len(alternatives) == 2
    assert alternatives[0].name == "Alt1"

def test_process_alternatives_no_alternatives():
    processor = DrugAlternativesProcessor()
    mock_drug_info = DrugInfo(
        drugName="TestDrug",
        alternatives=[],
        restrictions=[]
    )
    alternatives = processor.process_alternatives(mock_drug_info)
    assert isinstance(alternatives, list)
    assert len(alternatives) == 0
