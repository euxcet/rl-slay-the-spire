from __future__ import annotations
from .buff import Buff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class CombustBuff(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
        damage: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)
        self.damage = damage

    def on_turn_end(self):
        self.target.lose_hp(self.stack)
        for enemy in self.combat.enemies.copy():
            enemy.receive_damage(self.damage, self.target, do_effect=False)

    def merge(self, effect: CombustBuff) -> None:
        super().merge(effect)
        self.damage += effect.damage