from __future__ import annotations

from .character import Character
from ..card import Card
from ..card.deck import Deck

class Ironclad(Character):
    def __init__(
        self,
        deck: Deck,
        hp: int = 80,
        max_hp: int = 80,
        gold: int = 100,
    ) -> None:
        super().__init__(
            hp=hp,
            max_hp=max_hp,
            gold=gold,
            deck=deck,
        )

    def set_hp(self, hp: int) -> Ironclad:
        self.hp = hp
        return self
