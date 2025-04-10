from ..card import Card
from enum import Enum

class ModifyDeckType(Enum):
    Remove = 0
    Upgrade = 1
    Transform = 2
    Duplicate = 3
    Innate = 4

class ModifyDeckObservation():
    # TODO: add map
    def __init__(
        self,
        character_hp: int,
        deck: list[Card],
        options: list[Card],
    ) -> None:
        self.character_hp = character_hp
        self.deck = deck
        self.options = options

    def __str__(self) -> str:
        return "ModifyDeckObservation"

    def rich(self) -> str:
        ...