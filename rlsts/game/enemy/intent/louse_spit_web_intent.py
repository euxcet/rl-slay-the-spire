from .intent import Intent
from typing import TYPE_CHECKING
from ...effect import Weak
if TYPE_CHECKING:
    from .. import Enemy

class LouseSpitWebIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)
        
    def perform(self) -> None:
        self.enemy.combat.character.receive_effect(Weak(self.enemy.combat, self.values[0]))
