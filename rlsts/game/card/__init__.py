import numpy as np

NUM_CARD = 0
CARD_TYPES = []

def add_card(card: type) -> None:
    global NUM_CARD
    NUM_CARD += 1
    card.ID = NUM_CARD
    CARD_TYPES.append(card)

def create_tensor(cards: list[type]) -> np.ndarray:
    t = np.zeros(NUM_CARD, np.int8)
    for card in cards:
        if card is not type:
            card = type(card)
        for i in range(len(CARD_TYPES)):
            if CARD_TYPES[i] == card:
                t[i] += 1
    return t

from .starter import Strike, Defend
from .ironclad import Bash

add_card(Strike)
add_card(Defend)
add_card(Bash)