from .intent import Intent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Enemy

class SlimeBossSplitIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)

    def perform(self) -> None:
        from ..monster.slimes import AcidSlimeL
        from ..monster.slimes import SpikeSlimeL
        self.combat.add_enemy(self.enemy.position, AcidSlimeL(self.enemy.hp).start_combat(self.combat))
        self.combat.add_enemy(self.enemy.position, SpikeSlimeL(self.enemy.hp).start_combat(self.combat))
        self.combat.remove_enemy(self.enemy)
