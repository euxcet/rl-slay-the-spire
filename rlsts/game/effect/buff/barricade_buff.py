from .buff import Buff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class BarricadeBuff(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def modify_remove_block_turn(self, block: int) -> int:
        return 0
