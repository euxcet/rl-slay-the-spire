from .intent import Intent
from typing import TYPE_CHECKING
from ...effect import Strength
if TYPE_CHECKING:
    from .. import Enemy

class LouseGrowIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)
        
    def perform(self) -> None:
        self.enemy.receive_effect(Strength(self.enemy.combat, self.values[0]))
