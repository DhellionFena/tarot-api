"""
This module provides functions for drawing petit lenormand cards and performing a reading.
"""

import random

CARDS = [
    {"name": "Cavaleiro", "description": "Mensagens, notícias rápidas.", "number": 1},
    {"name": "Cavaleira", "description": "Mensagens, notícias lentas.", "number": 2},
    {"name": "Cavaleiro", "description": "Mensagens, notícias lentas.", "number": 3},
    {"name": "Trevo", "description": "Sorte, pequenas alegrias.", "number": 4},
    {"name": "Navio", "description": "Viagens, mudanças.", "number": 5},
    {"name": "Navio", "description": "Viagens, mudanças.", "number": 6},
]


def read_past_present_future(shuffle_times: int = 3):
    """
    Performs a reading by shuffling a set of cards multiple times and selecting 
    three cards to represent the past, present, and future. 

    Args:
        shuffle_times (int): Number of times to shuffle the cards. Default is 3.

    Returns:
        list: A list containing a dictionary with three keys 'past', 'present', 
        and 'future', each associated with a card drawn from the shuffled deck.
    """

    session_cards = CARDS
    result = {}
    for _ in range(shuffle_times):
        random.shuffle(session_cards)

    # session_cards = session_cards[int(len(session_cards)/2):]

    result = {
        "past": session_cards[0],
        "present": session_cards[1],
        "future": session_cards[2],
    }

    return result
