from .intent import Intent
from typing import TYPE_CHECKING
from ...effect.buff.strength import Strength
if TYPE_CHECKING:
    from .. import Enemy

class HexaghostInflameIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)
        # self.strength = 2 self.block = 12
        
    def perform(self) -> None:
        self.enemy.receive_effect(Strength(self.combat, self.values[0]))
        self.enemy.add_block(self.values[1])
