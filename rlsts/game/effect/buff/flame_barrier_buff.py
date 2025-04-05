from .buff import Buff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat
    from ...target import Target

class FlameBarrierBuff(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def on_turn_start(self) -> None:
        self.stack = 0

    def on_attacked(self, damage: int, attacker: 'Target'):
        from ...enemy import Enemy
        if attacker != None and isinstance(attacker, Enemy):
            attacker.receive_damage(self.stack, self.target)
