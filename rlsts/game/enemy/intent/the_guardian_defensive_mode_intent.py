from .intent import Intent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Enemy
from ...effect.buff.sharp_hide import SharpHide

class TheGuardianDefensiveModeIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)

    def perform(self) -> None:
        self.enemy.receive_effect(SharpHide(self.combat, self.values[0]))
