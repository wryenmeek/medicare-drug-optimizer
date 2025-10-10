from unittest.mock import MagicMock

import pytest
from app.services.drug_alternatives_service import DrugAlternativesService


@pytest.fixture
def mock_rxclass_client():
    return MagicMock()

def test_get_alternatives_categorization(mock_rxclass_client):
    mock_rxclass_client.get_drug_classes.return_value = {
        "allRelatedGroup": {
            "conceptGroup": [
                {
                    "concept": [
                        {
                            "conceptName": "Simvastatin",
                            "rxcui": "36567"
                        }
                    ]
                }
            ]
        }
    }

    service = DrugAlternativesService(mock_rxclass_client)
    alternatives = service.get_alternatives("12345")

    assert len(alternatives) == 1
    assert alternatives[0].category == "Generic"
    assert alternatives[0].category == "Generic"
