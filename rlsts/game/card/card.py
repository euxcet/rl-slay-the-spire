from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import TYPE_CHECKING
import numpy as np

if TYPE_CHECKING:
    from ..combat import Combat
    from ..effect import Effect
    from ..enemy import Enemy
    from .pile import Pile

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
        is_exhaust: bool = False,
    ) -> None:
        self.rarity = rarity
        self.type = type
        self.cost = cost
        self.origin_cost = cost
        self._is_unplayable = is_unplayable
        self.is_ethereal = is_ethereal
        self.is_exhaust = is_exhaust
        self.combat: 'Combat' = None
        self.target_types = target_types
        self.step = 0
        self.pile: Pile = None
        # for x
        self.energy = 0

    @property
    def is_unplayable(self) -> bool:
        return self._is_unplayable

    @property
    def draw_pile(self) -> 'Pile':
        return self.combat.character.draw_pile

    @property
    def hand_pile(self) -> 'Pile':
        return self.combat.character.hand_pile

    @property
    def discard_pile(self) -> 'Pile':
        return self.combat.character.discard_pile

    @property
    def exhaust_pile(self) -> 'Pile':
        return self.combat.character.exhaust_pile

    def target_type(self) -> CardTargetType:
        if len(self.target_types) == 0:
            return None
        return self.target_types[self.step]

    def next_step(self) -> bool:
        while self.step < len(self.target_types):
            if np.sum(self.get_action_mask(self.combat.MAX_ACTION)) == 0:
                self.targets.append(None)
                self.step += 1
            else:
                break
        if self.step == len(self.target_types):
            self._finish(self.energy)
            return True
        return False

    # return: has the card completed its function
    def play(self, energy: int) -> bool:
        self.energy = energy
        self.step = 0
        self.targets = []
        return self.next_step()

    # return: has the card completed its function
    def choose(self, target: int) -> bool:
        self.step += 1
        self.targets.append(target)
        return self.next_step()

    def can_choose(self, target: int) -> bool:
        if self.target_types[self.step] == CardTargetType.Enemy:
            return target < len(self.combat.enemies)
        elif self.target_types[self.step] == CardTargetType.Hand:
            return target < len(self.hand_pile)
        elif self.target_types[self.step] == CardTargetType.Draw:
            return target < len(self.draw_pile)
        elif self.target_types[self.step] == CardTargetType.Discard:
            return target < len(self.discard_pile)
        elif self.target_types[self.step] == CardTargetType.Exhaust:
            return target < len(self.exhaust_pile)

    def get_action_mask(self, max_action: int) -> np.ndarray:
        if self.target_types[self.step] == CardTargetType.Enemy:
            l = len(self.combat.enemies)
        elif self.target_types[self.step] == CardTargetType.Hand:
            l = len(self.hand_pile)
        elif self.target_types[self.step] == CardTargetType.Draw:
            l = len(self.draw_pile)
        elif self.target_types[self.step] == CardTargetType.Discard:
            l = len(self.discard_pile)
        elif self.target_types[self.step] == CardTargetType.Exhaust:
            l = len(self.exhaust_pile)
        return np.pad(np.ones((min(max_action, l),), dtype=np.float32), [(0, max(0, max_action - l))])

    def to(self, combat: Combat) -> Card:
        self.combat = combat
        return self

    # Put the card on top of the pile
    def move_to(self, pile: 'Pile') -> Card:
        if self.pile != None and self in self.pile:
            self.pile.remove(self)
        if pile != None:
            pile.insert(self)
        return self

    def exhaust(self) -> None:
        self.move_to(self.exhaust_pile).on_exhaust()

    def discard(self, is_turn_end: bool = False) -> None:
        if is_turn_end:
            self.move_to(self.discard_pile).on_turn_discard()
        else:
            self.move_to(self.discard_pile).on_discard()

    def _finish(self, energy: int) -> None:
        self.finish(energy)
        if self.is_exhaust:
            self.exhaust()
        else:
            self.discard()
        #     self.combat.character.exhaust_pile.insert(self)
        # else:
        #     self.combat.character.discard_pile.insert(self)

    @abstractmethod
    def finish(self, energy: int) -> None:
        ...

    def on_draw(self) -> None:
        ...

    def on_turn_discard(self) -> None:
        ...

    def on_discard(self) -> None:
        ...
        # if self.is_ethereal:
        #     self.exhaust()
        # else:
        #     self.move_to(self.discard_pile)

    def on_exhaust(self) -> None:
        ...

    def get_enemy(self, target: int) -> Enemy:
        return self.combat.enemies[target]

    def add_block(self, block: int) -> None:
        self.combat.character.add_block(block)

    def attack(self, enemy: Enemy, damage: int) -> int:
        self.combat.character.attack(enemy, damage)

    def effect_character(self, effect: 'Effect') -> None:
        self.combat.character.receive_effect(effect)

    def effect_enemy(self, enemy: Enemy, effect: 'Effect') -> None:
        enemy.receive_effect(effect)
