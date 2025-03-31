import random
from .buff import Buff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class JuggernautBuff(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)
    
    def on_block(self, block: int) -> None:
        if len(self.combat.enemies) > 0:
            random.choice(self.combat.enemies).receive_damage(self.stack, self.target, do_effect=False)
