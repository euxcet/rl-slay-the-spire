from __future__ import annotations

from .card import Card
from .starter import Strike, Defend
from .ironclad import Bash

class Deck():
    def __init__(self) -> None:
        self.cards: list[Card] = []

    @staticmethod
    def ironclad_starter_deck() -> Deck:
        return [
            Strike(), Strike(), Strike(), Strike(), Strike(),
            Defend(), Defend(), Defend(), Defend(),
            Bash(),
        ]
