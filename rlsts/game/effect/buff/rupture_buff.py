from __future__ import annotations
from .buff import Buff
from .strength import Strength

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class RuptureBuff(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def on_lose_hp(self, hp: int) -> None:
        self.target.receive_effect(Strength(self.combat, self.stack))
