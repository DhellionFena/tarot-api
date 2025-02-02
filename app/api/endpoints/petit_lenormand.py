"""
This module defines the endpoints for the petit lenormand cards.
"""

from fastapi import APIRouter, Query
from app.services.petit_lenormand_service import read_past_present_future
from app.api.schema.petit_lenormand import PastPresentFutureReading

router = APIRouter()


@router.get("/petit_lenormand/past_present_future", response_model=PastPresentFutureReading)
async def past_present_future(shuffle_times: int = Query(1, ge=1, le=5)):
    """
    Endpoint to perform a past, present, and future card reading.

    Args:
        shuffle_times (int): Number of times to shuffle the cards before drawing. 
                             Must be between 1 and 5, inclusive. Default is 1.

    Returns:
        list[Card]: A list of three cards representing the past, present, and future.
    """

    return read_past_present_future(shuffle_times)
