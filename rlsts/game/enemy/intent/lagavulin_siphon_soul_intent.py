from .intent import Intent
from typing import TYPE_CHECKING
from ...effect.debuff.dexterity_down import DexterityDown
from ...effect.debuff.strength_down import StrengthDown
if TYPE_CHECKING:
    from .. import Enemy

class LagavulinSiphonSoulIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)
        
    def perform(self) -> None:
        self.character.receive_effect(DexterityDown(self.combat, self.values[0]))
        self.character.receive_effect(StrengthDown(self.combat, self.values[0]))