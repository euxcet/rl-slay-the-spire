from abc import ABC, abstractmethod
from enum import Enum


class CardRarity(Enum):
    Starter = 0
    Common = 1
    Uncommon = 2
    Rare = 3

class CardType(Enum):
    Attack = 0
    Skill = 1
    Power = 2

class Card(ABC):
    ID = -1

    def __init__(
        self,
        rarity: CardRarity,
        type: CardType,
        energy: int,
        playable: bool,
    ) -> None:
        self.rarity = rarity
        self.type = type
        self.energy = energy
        self.playable = playable
        self.combat = None
        self.id = 0

    @abstractmethod
    def play(self):
        ...

    @abstractmethod
    def choose(self, id: int):
        ...

    @abstractmethod
    def on_draw(self):
        ...

    @abstractmethod
    def on_turn_discard(self):
        ...

    @abstractmethod
    def on_discard(self):
        ...

    @abstractmethod
    def on_exhaust(self):
        ...
