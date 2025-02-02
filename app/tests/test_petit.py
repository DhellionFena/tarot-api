"""
This module contains tests for the petit lenormand cards.
"""

from fastapi.testclient import TestClient
from app.main import app
from app.api.schema.petit_lenormand import PastPresentFutureReading
from app.services.petit_lenormand_service import CARDS

client = TestClient(app)


def test_past_present_future():
    """
    Tests if the /petit_lenormand/past_present_future endpoint 
    returns a response with status 200 and with the keys past, present, and future,
    and if the returned cards are in the original list of cards.
    """
    response = client.get(
        "/api/v1/petit_lenormand/past_present_future?shuffle_times=1")

    # Check if the status code is 200 (OK)
    assert response.status_code == 200

    # Validate the response structure using the Pydantic model
    try:
        PastPresentFutureReading(**response.json())
    except ValueError:
        assert False, "Response does not match the PastPresentFutureReading model"

    # Check if the response contains the expected keys
    data = response.json()
    assert "past" in data
    assert "present" in data
    assert "future" in data

    # Check if the returned cards are in the original list of cards

    assert data["past"] in CARDS
    assert data["present"] in CARDS
    assert data["future"] in CARDS
