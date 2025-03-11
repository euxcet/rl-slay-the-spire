from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..combat import Combat
from ..effect import Effect
from .intent import Intent

class Enemy(ABC):
    def __init__(
        self,
        hp: int,
    ) -> None:
        self.hp = hp
        self.block = 0
        self.effects: list[Effect] = []

    def start_combat(self, combat: 'Combat') -> None:
        self.combat = combat
        self.effects.clear()
        self.died = False

    def start_turn(self) -> None:
        self.block = 0

    def end_turn(self) -> None:
        for effect in self.effects:
            effect.on_turn_end()

    @abstractmethod
    def get_intent(self) -> Intent:
        ...

    @abstractmethod
    def perform(self) -> None:
        ...

    def die(self) -> None:
        self.hp = 0
        self.died = True
        self.combat.enemy_die()

    def receive_damage(self, damage: int) -> int:
        for effect in self.effects:
            damage = effect.modify_received_damage(damage)
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
        return damage

    def receive_effect(self, new_effect: Effect) -> None:
        new_effect.target_enemy = self
        for effect in self.effects:
            if type(effect) == type(new_effect):
                effect.stack += new_effect.stack
                return
        self.effects.append(new_effect)

    def prepare_attack(self, damage: int) -> int:
        for effect in self.effects:
            damage = effect.modify_damage(damage)
        return damage

    def estimate_attack(self, damage: int) -> int:
        return self.combat.character.estimate_damage(self.prepare_attack(damage))

    def attack(self, damage: int) -> int:
        return self.combat.character.receive_damage(self.prepare_attack(damage))
