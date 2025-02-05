"""
This module defines the schema for the petit lenormand cards.
"""

from pydantic import BaseModel
from app.models.petit_lenormand_model import PetitLenormandCard


class PastPresentFutureReading(BaseModel):
    """
    Represents a reading consisting of a past, present, and future card.
    """
    past: PetitLenormandCard
    present: PetitLenormandCard
    future: PetitLenormandCard


class YesOrNoReading(BaseModel):
    """
    Represents a reading consisting of a past, present, and future card.
    """
    response: str
    first_card: PetitLenormandCard
    last_card: PetitLenormandCard
