"""
This module defines the schema for the petit lenormand cards.
"""

from pydantic import BaseModel


class PetitLenormandCard(BaseModel):
    """
    A petit lenormand card.

    Attributes:
        name (str): The name of the card.
        description (str): A brief description of the card.
        number (int): The number of the card.
    """
    name: str
    description: str
    number: int


class PastPresentFutureReading(BaseModel):
    past: PetitLenormandCard
    present: PetitLenormandCard
    future: PetitLenormandCard
