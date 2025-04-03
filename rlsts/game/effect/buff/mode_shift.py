from .buff import Buff
from .strength import Strength

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class ModeShift(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def on_receive_damage(self, damage: int, attacker) -> None:
        if self.stack <= damage:
            self.stack = 0
            self.target.shift_mode()
        else:
            self.stack -= damage
