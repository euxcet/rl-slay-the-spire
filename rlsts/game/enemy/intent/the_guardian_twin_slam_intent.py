from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...enemy import Enemy

class TheGuardianTwinSlamIntent(AttackIntent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=True)

    def perform(self) -> None:
        super().perform()
        self.enemy.shift_mode()
