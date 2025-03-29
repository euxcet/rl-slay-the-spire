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
        combat: 'Combat' = None,
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
    
    def draw_index(self, index: int) -> Card:
        return self.cards.pop(index)

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

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self) -> Card:
        if self.index < len(self.cards):
            v = self.cards[self.index]
            self.index += 1
            return v
        else:
            raise StopIteration

    def __getitem__(self, index: int) -> Card:
        return self.cards[index]
