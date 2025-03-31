from __future__ import annotations
from .buff import Buff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class MetallicizeBuff(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def on_turn_end(self) -> None:
        self.target.add_block(self.stack, do_effect=False)
