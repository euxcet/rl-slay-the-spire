from __future__ import annotations

import random
from abc import ABC, abstractmethod
from enum import Enum
from typing import TYPE_CHECKING
import numpy as np

if TYPE_CHECKING:
    from ..combat import Combat
    from ..effect import Effect
    from ..enemy import Enemy
    from ..character import Character
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
        self._cost = cost
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
    def cost(self) -> int:
        return self._cost
    
    @cost.setter
    def cost(self, c: int) -> None:
        self._cost = c

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

    @property
    def character(self) -> 'Character':
        return self.combat.character

    @property
    def enemies(self) -> list['Enemy']:
        return self.combat.enemies

    def target_type(self) -> CardTargetType:
        if len(self.target_types) == 0:
            return None
        if isinstance((t := self.target_types[self.step]), tuple):
            return t[0]
        else:
            return t

    def next_step(self) -> bool:
        while self.step < len(self.target_types):
            if np.sum(self.get_action_mask()) == 0:
                self.targets.append(None)
                self.step += 1
            else:
                break
        if self.step == len(self.target_types):
            self._finish(self.energy)
            for effect in self.character.effects:
                effect.on_play_card(self)
            for enemy in self.enemies:
                for effect in enemy.effects:
                    effect.on_play_card(self)
            return True
        return False

    # return: has the card completed its function
    def play(self, energy: int) -> bool:
        self.energy = energy
        self.step = 0
        self.targets = []
        self.on_play()
        return self.next_step()

    def random_play(self, energy: int):
        self.energy = energy
        self.step = 0
        self.targets = []
        while self.step < len(self.target_types):
            action_mask = self.get_action_mask()
            if np.sum(action_mask) == 0:
                self.targets.append(None)
            else:
                self.targets.append(random.choice([i for i in range(len(action_mask)) if action_mask[i] > 0]))
            self.step += 1
        self._finish(self.energy)

    # return: has the card completed its function
    def choose(self, target: int) -> bool:
        self.step += 1
        self.targets.append(target)
        return self.next_step()

    def can_choose(self, target: int) -> bool:
        return target < self.combat.MAX_ACTION and self.get_action_mask()[target] > 0

    def get_action_mask(self) -> np.ndarray:
        if isinstance(self.target_types[self.step], tuple):
            target_type = self.target_types[self.step][0]
            constraint = self.target_types[self.step][1]
        else:
            target_type = self.target_types[self.step]
            constraint = None

        if target_type == CardTargetType.Enemy:
            l = len(self.enemies)
        elif target_type == CardTargetType.Hand:
            l = len(self.hand_pile)
        elif target_type == CardTargetType.Draw:
            l = len(self.draw_pile)
        elif target_type == CardTargetType.Discard:
            l = len(self.discard_pile)
        elif target_type == CardTargetType.Exhaust:
            l = len(self.exhaust_pile)

        mask = np.pad(np.ones((min(self.combat.MAX_ACTION, l),), dtype=np.float32), [(0, max(0, self.combat.MAX_ACTION - l))])
        if constraint != None:
            for i in range(len(mask)):
                if mask[i] > 0:
                    if target_type == CardTargetType.Enemy:
                        mask[i] = constraint(self.enemies[i])
                    elif target_type == CardTargetType.Hand:
                        mask[i] = constraint(self.hand_pile[i])
                    elif target_type == CardTargetType.Draw:
                        mask[i] = constraint(self.draw_pile[i])
                    elif target_type == CardTargetType.Discard:
                        mask[i] = constraint(self.discard_pile[i])
                    elif target_type == CardTargetType.Exhaust:
                        mask[i] = constraint(self.exhaust_pile[i])
        return mask

    def to(self, combat: Combat) -> Card:
        self.combat = combat
        return self
    
    def to_pile(self, pile: 'Pile') -> Card:
        self.pile = pile
        return self

    # Put the card on top of the pile
    def move_to(self, pile: 'Pile', is_random: bool = False) -> Card:
        if self.pile != None and self in self.pile:
            self.pile.remove(self)
        if pile != None:
            if is_random:
                pile.insert(self, random.randint(0, len(pile)))
            else:
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
        elif self.type == CardType.Attack or self.type == CardType.Skill:
            self.discard()

    @abstractmethod
    def finish(self, energy: int) -> None:
        ...

    def on_play(self) -> None:
        ...

    def on_draw(self) -> None:
        ...

    def on_turn_discard(self) -> None:
        ...

    def on_discard(self) -> None:
        ...

    def on_exhaust(self) -> None:
        for effect in self.combat.character.effects:
            effect.on_exhaust(self)

    def get_enemy(self, target: int) -> Enemy:
        return self.enemies[target]

    def add_block(self, block: int) -> None:
        self.character.add_block(block)

    def attack(self, enemy: Enemy, damage: int) -> int:
        self.character.attack(enemy, damage)

    def effect_character(self, effect: 'Effect') -> None:
        self.character.receive_effect(effect)

    def effect_enemy(self, enemy: Enemy, effect: 'Effect') -> None:
        enemy.receive_effect(effect)

    def choose_hand_card(self, index: int = None) -> Card:
        if index == None:
            if len(self.hand_pile) == 0:
                return None
            else:
                return random.choice(self.hand_pile)
        else:
            return self.hand_pile[index]

    # for test
    def get_choice_list(self) -> list[tuple]:
        if self.step > len(self.target_types):
            return []
        def merge(targets: list, mask: np.ndarray) -> list[tuple]:
            result = []
            for i in range(min(len(targets), len(mask))):
                result.append((targets[i], mask[i]))
            return result

        if isinstance(self.target_types[self.step], tuple):
            target_type = self.target_types[self.step][0]
        else:
            target_type = self.target_types[self.step]
        mask = self.get_action_mask()

        if target_type == CardTargetType.Enemy:
            return merge(self.enemies, mask)
        elif target_type == CardTargetType.Hand:
            return merge(self.hand_pile.cards, mask)
        elif target_type == CardTargetType.Draw:
            return merge(self.draw_pile.cards, mask)
        elif target_type == CardTargetType.Discard:
            return merge(self.discard_pile.cards, mask)
        elif target_type == CardTargetType.Exhaust:
            return merge(self.exhaust_pile.cards, mask)

    def rich(self, offset: int = 0, style: str = 'bold green') -> str:
        return f'[{style}]{type(self).__name__}[{offset}][/{style}]'
