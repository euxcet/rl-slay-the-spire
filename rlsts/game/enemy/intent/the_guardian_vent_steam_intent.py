from .intent import Intent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Enemy
from ...effect.debuff.weak import Weak
from ...effect.debuff.vulnerable import Vulnerable

class TheGuardianVentSteamIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)

    def perform(self) -> None:
        self.character.receive_effect(Weak(self.combat, self.values[0]))
        self.character.receive_effect(Vulnerable(self.combat, self.values[0]))
