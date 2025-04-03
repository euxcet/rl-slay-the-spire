from .intent import Intent
from ...effect import Strength
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Enemy

class JawWormBellowIntent(Intent):
    # values: strength block
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)
        
    def perform(self) -> None:
        self.enemy.receive_effect(Strength(self.combat, self.values[0]))
        self.enemy.add_block(self.values[1])
