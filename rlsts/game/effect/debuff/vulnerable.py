import math
from .debuff import Debuff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class Vulnerable(Debuff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=1)

    def modify_received_damage(self, damage: int) -> int:
        return math.floor(damage * 1.5)