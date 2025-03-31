import random
from copy import deepcopy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..combat import Combat

from .card import Card

class Pile():
    def __init__(
        self,
        cards: list[Card] = None,
        combat: 'Combat' = None,
    ) -> None:
        self.cards: list[Card] = []
        if cards is not None:
            self.cards = deepcopy(cards)
        if combat is not None:
            for card in self.cards:
                card.combat = combat

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> Card:
        try:
            return self.cards.pop()
        except:
            return None
    
    def draw_index(self, index: int) -> Card:
        try:
            return self.cards.pop(index)
        except:
            return None

    def remove(self, card: Card) -> None:
        self.cards.remove(card)
    
    # TODO: insert at the beginning?
    def insert(self, card: Card) -> None:
        self.cards.append(card)
        card.pile = self

    def shuffle_into(self, card: Card) -> None:
        self.cards.insert(random.randint(0, len(self.cards)), card)

    def extend(self, cards: list[Card]) -> None:
        for card in cards:
            card.pile = self
        self.cards.extend(cards)

    def clear(self) -> None:
        self.cards.clear()

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, index: int) -> Card:
        return self.cards[index]
