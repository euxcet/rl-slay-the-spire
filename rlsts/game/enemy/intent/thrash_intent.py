from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...enemy import Enemy

class ThrashIntent(AttackIntent):
    # values: attack block
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=False)

    def perform(self) -> None:
        super().perform()
        self.enemy.add_block(self.values[1])
