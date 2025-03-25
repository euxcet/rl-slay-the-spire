from __future__ import annotations

from .card import Card
from .starter.strike import Strike
from .starter.defend import Defend
from .ironclad.attack.bash import Bash

class Deck():
    def __init__(self, cards: list[Card]) -> None:
        self.cards = cards

    @staticmethod
    def ironclad_starter_deck() -> Deck:
        return Deck([
            Strike(), Strike(), Strike(), Strike(), Strike(),
            Defend(), Defend(), Defend(), Defend(),
            Bash(),
        ])

    def add_cards(self, cards: list[Card]) -> None:
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)