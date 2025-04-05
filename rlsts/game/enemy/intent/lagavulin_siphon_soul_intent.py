from .intent import Intent
from typing import TYPE_CHECKING
from ...effect.buff.strength import Strength
from ...effect.buff.dexterity import Dexterity
if TYPE_CHECKING:
    from .. import Enemy

class LagavulinSiphonSoulIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)
        
    def perform(self) -> None:
        self.character.receive_effect(Dexterity(self.combat, -self.values[0]))
        self.character.receive_effect(Strength(self.combat, -self.values[0]))