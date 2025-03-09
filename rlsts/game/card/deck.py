from __future__ import annotations

from .card import Card
from .starter import Strike, Defend
from .ironclad import Bash

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
