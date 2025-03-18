from abc import abstractmethod
from typing import TYPE_CHECKING

from ..target import Target
if TYPE_CHECKING:
    from ..combat import Combat
from ..effect import Effect
from .intent import Intent

class Enemy(Target):
    MAX_INTENTS = 100

    def __init__(
        self,
        hp: int,
    ) -> None:
        self.hp = hp
        self.block = 0
        self.effects: list[Effect] = []

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

    def estimate_attack(self, damage: int) -> int:
        return self.combat.character.estimate_received_damage(self.prepare_attack(damage))

    def attack(self, damage: int) -> int:
        return self.combat.character.receive_damage(self.prepare_attack(damage))
