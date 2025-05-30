from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from ..target import Target
if TYPE_CHECKING:
    from ..combat import Combat
from .intent import Intent
from ...utils.random_pool import RandomPool

class Enemy(Target):
    def __init__(
        self,
        hp: int,
    ) -> None:
        super().__init__(hp=hp, max_hp=hp)
        self.position = 0
        self.intent_history: list[Intent] = []
        self.intent_pool = RandomPool()

    def start_turn(self) -> None:
        super().start_turn()

    def end_turn(self) -> None:
        super().end_turn()

    @abstractmethod
    def get_intent(self, turn: int) -> Intent:
        ...

    def perform(self) -> None:
        intent: Intent = self.get_intent()
        self.intent_history.append(intent)
        intent.perform()

    def die(self) -> None:
        super().die()
        self.combat.remove_enemy(self)

    def estimate_attack(self, damage: int) -> int:
        return self.combat.character.estimate_received_damage(self.prepare_attack(damage))

    def attack(self, damage: int) -> int:
        for effect in self.effects:
            effect.on_attack(damage)
        return self.combat.character.receive_damage(self.prepare_attack(damage), self)

    # intent, chance, continuous_limit
    def choose_intent(self, options: list[tuple[Intent, float, int]]) -> Intent:
        valid_options = []
        for option in options:
            if option[2] < 2 or \
               sum(map(lambda x: type(x) == type(option[0]), self.intent_history[-option[2] + 1:])) < option[2] - 1:
                valid_options.append(option)
        assert len(valid_options) >= 1
        s = sum(map(lambda x: x[1], valid_options))
        r = self.intent_pool.peek(self.combat.turn)
        for option in valid_options:
            if r < option[1] / s:
                return option[0]
            r -= option[1] / s
        assert False

    def __lt__(self, other: Enemy) -> bool:
        return self.ID < other.ID

    def rich(self, offset: int = 0, style: str = 'bold green') -> str:
        return f'[{style}]{type(self).__name__}[{offset}][/{style}]'