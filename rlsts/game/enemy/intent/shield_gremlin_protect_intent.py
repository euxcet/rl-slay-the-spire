from .intent import Intent
from ...effect import Strength
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Enemy

class ShieldGremlinProtectIntent(Intent):
    # values: enemy block
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)
        
    def perform(self) -> None:
        self.values[0].add_block(self.values[1])
