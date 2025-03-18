from abc import ABC, abstractmethod
from .effect import Effect
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .combat import Combat

class Target(ABC):
    def __init__(
        self,
        hp: int,
    ) -> None:
        self.hp = hp
        self.block = 0
        self.effects: list[Effect] = []
        self.combat: Combat = None
        self.died = False

    def start_combat(self, combat: 'Combat') -> None:
        self.combat = combat
        self.effects.clear()

    def die(self) -> None:
        self.hp = 0
        self.died = True

    def start_turn(self) -> None:
        self.block = 0

    def end_turn(self) -> None:
        for effect in self.effects:
            effect.on_turn_end()
        for effect in self.effects:
            effect.stack -= effect.decrease_per_turn
        self.update_effects()

    def add_block(self, block: int) -> int:
        for effect in self.effects:
            block = effect.modify_block(block)
        self.block += block

    def receive_damage(self, damage: int) -> int:
        damage = self.estimate_received_damage(damage)
        if damage <= 0:
            return 0
        # TODO: relics ...
        if damage <= self.block:
            self.block -= damage
            return 0
        damage -= self.block
        self.block = 0
        if damage >= self.hp:
            hp = self.hp
            self.die()
            return hp
        self.hp -= damage
        for effect in self.effects:
            effect.on_receive_damage(damage)
        return damage

    def receive_effect(self, new_effect: Effect) -> None:
        new_effect.target = self
        for effect in self.effects:
            if type(effect) == type(new_effect):
                effect.stack += new_effect.stack
                return
        self.effects.append(new_effect)

    def prepare_attack(self, damage: int) -> int:
        for effect in self.effects:
            damage = effect.modify_damage(damage)
        return damage

    def update_effects(self) -> None:
        self.effects = [effect for effect in self.effects if effect.stack != 0]

    def estimate_received_damage(self, damage: int) -> int:
        for effect in self.effects:
            damage = effect.modify_received_damage(damage)
        # TODO: relics ...
        return damage