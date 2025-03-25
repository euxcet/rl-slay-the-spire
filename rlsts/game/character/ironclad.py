from __future__ import annotations

from .character import Character
from ..card import Card
from ..card.deck import Deck

class Ironclad(Character):
    def __init__(self):
        super().__init__(
            hp=80,
            max_hp=80,
            gold=100,
            deck=Deck.ironclad_starter_deck(),
        )

    def set_hp(self, hp: int) -> Ironclad:
        self.hp = hp
        return self
