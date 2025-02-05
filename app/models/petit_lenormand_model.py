"""
This module defines the model for a Petit Lenormand card.
"""

from app.models.card_model import Card


class PetitLenormandCard(Card):
    """Modelo de negócio para uma carta do Tarot Petit Lenormand."""
    number: int
    positivity: int

    def __str__(self):
        return f"{self.name} ({self.description})"
