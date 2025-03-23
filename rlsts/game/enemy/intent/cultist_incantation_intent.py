from .intent import Intent
from typing import TYPE_CHECKING
from ...effect import Ritual
if TYPE_CHECKING:
    from ...enemy import Enemy

class CultistIncantationIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)
        
    def perform(self) -> None:
        self.enemy.receive_effect(Ritual(self.enemy.combat, self.values[0]))
