from .intent import Intent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Enemy

class AcidSlimeSplitIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)

    def perform(self) -> None:
        from ..monster.slimes import AcidSlimeM
        self.enemy.combat.add_enemy(self.enemy.position, AcidSlimeM(self.enemy.hp).to(self.enemy.combat))
        self.enemy.combat.add_enemy(self.enemy.position, AcidSlimeM(self.enemy.hp).to(self.enemy.combat))
        # TODO: garbage collection
        self.enemy.combat.remove_enemy(self.enemy)
