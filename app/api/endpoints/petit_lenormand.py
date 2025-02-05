"""
This module defines the endpoints for the petit lenormand cards.
"""

from fastapi import APIRouter
from app.services.petit_lenormand_service import read_past_present_future, read_yes_or_no
from app.api.schema.petit_lenormand import PastPresentFutureReading, YesOrNoReading

router = APIRouter()


@router.get("/petit_lenormand/past_present_future", response_model=PastPresentFutureReading)
async def past_present_future(question: str):
    """
    Endpoint to perform a past, present, and future card reading.

    Args:
        question (str): The question or text to be used for generating a unique shuffle pattern.

    Returns:
        PastPresentFutureReading: An object containing three cards representing the past, present, and future.
    """

    return read_past_present_future(question)


@router.get("/petit_lenormand/yes_or_no", response_model=YesOrNoReading)
async def yes_or_no(question: str):
    """
    Endpoint to perform a yes or no card reading.

    Args:
        question (str): The question or text to be used for generating a unique shuffle pattern.

    Returns:
        YesOrNoReading: An object containing the response to the question and the first and last cards drawn.
    """
    return read_yes_or_no(question)
