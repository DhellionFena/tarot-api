"""
This module defines the model for a Tarot card.
"""
from pydantic import BaseModel


class Card(BaseModel):
    """Modelo de negócio para uma carta do Tarot."""
    name: str
    description: str
