from .intent import Intent
from typing import TYPE_CHECKING
from ...effect import Vulnerable
if TYPE_CHECKING:
    from .. import Enemy

class ScrapeIntent(Intent):
    # attack vulnerable
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)
        self.values[0] = enemy.estimate_attack(self.values[0])

    def get_damage(self) -> int:
        return self.values[0]

    def perform(self) -> None:
        self.enemy.attack(self.values[0])
        self.enemy.combat.character.receive_effect(Vulnerable(self.enemy.combat, self.values[1]))
