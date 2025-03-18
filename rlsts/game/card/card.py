from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..combat import Combat
    from ..effect import Effect

class CardRarity(Enum):
    Starter = 0
    Common = 1
    Uncommon = 2
    Rare = 3

class CardType(Enum):
    Attack = 0
    Skill = 1
    Power = 2
    Status = 3
    Curse = 4

class CardTargetType(Enum):
    Enemy = 0
    Hand = 1
    Draw = 2
    Discard = 3
    Exhaust = 4

class Card(ABC):
    ID = -1

    def __init__(
        self,
        rarity: CardRarity,
        type: CardType,
        cost: int,
        target_types: list[CardTargetType],
        is_unplayable: bool = False,
        is_ethereal: bool = False,
    ) -> None:
        self.rarity = rarity
        self.type = type
        self.cost = cost
        self.origin_cost = cost
        self.is_unplayable = is_unplayable
        self.is_ethereal = is_ethereal
        self.combat: 'Combat' = None
        self.target_types = target_types

    # return: has the card completed its function
    def play(self) -> bool:
        self.current_target_id = 0
        self.targets = []
        if len(self.target_types) == 0:
            self._finish()
            return True
        return False

    # return: has the card completed its function
    def choose(self, id: int) -> bool:
        self.targets.append(id)
        self.current_target_id += 1
        if self.current_target_id == len(self.target_types):
            self._finish()
            return True
        return False

    def to(self, combat: Combat) -> Card:
        self.combat = combat
        return self

    def _finish(self) -> None:
        self.finish()
        if self.is_ethereal:
            self.combat.character.exhaust_pile.insert(self)
        else:
            self.combat.character.discard_pile.insert(self)

    @abstractmethod
    def finish(self) -> None:
        ...

    def on_draw(self) -> None:
        ...

    def on_turn_discard(self) -> None:
        ...

    def on_discard(self) -> None:
        ...

    def on_exhaust(self) -> None:
        ...

    def add_block(self, block: int) -> None:
        self.combat.character.add_block(block)

    def attack(self, target: int, damage: int) -> int:
        return self.combat.enemies[target].receive_damage(self.combat.character.prepare_attack(damage))

    def effect_character(self, effect: 'Effect') -> None:
        self.combat.character.receive_effect(effect)

    def effect_enemy(self, target: int, effect: 'Effect') -> None:
        self.combat.enemies[target].receive_effect(effect)