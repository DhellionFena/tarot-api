"""
This module provides functions for drawing petit lenormand cards and performing a reading.
"""

import hashlib
from app.services.cards import shuffle_cards


def read_past_present_future(question: str):
    """
    Performs a past, present, and future card reading based on a given question.

    Args:
        question (str): The question or text to be used for generating a unique shuffle pattern.

    Returns:
        dict: A dictionary containing three cards representing the past, present, and future.
    """

    shuffle_times = (
        int(hashlib.md5(question.encode()).hexdigest(), 16) % 10) + 1

    session_cards = shuffle_cards(shuffle_times)

    session_cards = session_cards[int(len(session_cards)/2):]

    result = {
        "past": session_cards[0],
        "present": session_cards[1],
        "future": session_cards[2],
    }

    return result


def read_yes_or_no(question: str):
    """
    Performs a yes or no card reading based on a given question.

    Args:
        question (str): The question or text to be used for generating a unique shuffle pattern.

    Returns:
        dict: A dictionary containing the response as "Sim.", "Não.", or "Talvez.",
              along with the first and last card used in determining the response.
    """

    shuffle_times = (
        int(hashlib.md5(question.encode()).hexdigest(), 16) % 10) + 1

    session_cards = shuffle_cards(shuffle_times)

    session_cards = session_cards[int(len(session_cards)/2):]

    result = session_cards[0].positivity + session_cards[1].positivity

    response = "Talvez."
    if result > 0:
        response = "Sim."
    elif result < 0:
        response = "Não."

    result = {
        "response": response,
        "first_card": session_cards[0],
        "last_card": session_cards[1]
    }

    return result
