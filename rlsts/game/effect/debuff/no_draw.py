from .debuff import Debuff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class NoDraw(Debuff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=1)

    def modify_num_draw(self, num: int) -> int:
        return 0