from .buff import Buff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class CurlUp(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def on_receive_damage(self, damage: int) -> None:
        self.target.add_block(self.stack)
        self.stack = 0
        self.target.update_effects()
