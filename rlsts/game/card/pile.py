import random
from copy import deepcopy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..combat import Combat

from .card import Card
from .deck import Deck

class Pile():
    def __init__(
        self,
        deck: Deck = None,
        combat: Combat = None,
    ) -> None:
        self.cards: list[Card] = []
        if deck is not None:
            self.cards = deepcopy(deck.cards)
        if combat is not None:
            for card in self.cards:
                card.combat = combat

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()
    
    def draw_by_id(self, card_id: int) -> Card:
        for i, card in enumerate(self.cards):
            if card.id == card_id:
                return self.cards.pop(i)
        return None
    
    # TODO: insert at the beginning?
    def insert(self, card: Card) -> None:
        self.cards.append(card)

    def __len__(self) -> int:
        return len(self.cards)
