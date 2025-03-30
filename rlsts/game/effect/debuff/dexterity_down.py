from .debuff import Debuff
from ..buff.dexterity import Dexterity

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class DexterityDown(Debuff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def on_turn_end(self):
        self.target.receive_effect(Dexterity(self.combat, -self.stack))
        self.stack = 0
