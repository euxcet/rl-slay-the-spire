from .intent import Intent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Enemy

class LooterSmokeBombIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)
        
    def perform(self) -> None:
        self.enemy.add_block(self.values[0])
