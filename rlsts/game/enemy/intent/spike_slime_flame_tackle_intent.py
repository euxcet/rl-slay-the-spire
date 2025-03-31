from .intent import Intent
from typing import TYPE_CHECKING
from ...card import Slimed
if TYPE_CHECKING:
    from .. import Enemy

class SpikeSlimeFlameTackleIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)
        self.values[0] = enemy.estimate_attack(self.values[0])

    def is_attack(self) -> bool:
        return True

    def get_damage(self):
        return self.values[0]
        
    def perform(self) -> None:
        self.enemy.attack(self.values[0])
        for _ in range(self.values[1]):
            self.enemy.combat.character.discard_pile.shuffle_into(Slimed().to(self.enemy.combat))
