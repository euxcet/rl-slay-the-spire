from ..effect import Effect

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class Debuff(Effect):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
        decrease_per_turn: int,
    ) -> None:
        super().__init__(
            combat=combat,
            stack=stack,
            decrease_per_turn=decrease_per_turn
        )