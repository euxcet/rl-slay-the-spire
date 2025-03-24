from .buff import Buff
from .strength import Strength

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class Ritual(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
        skip: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0, skip=skip)

    def on_turn_end(self):
        if self.skip > 0:
            self.skip -= 1
        else:
            self.target.receive_effect(Strength(self.combat, self.stack))
