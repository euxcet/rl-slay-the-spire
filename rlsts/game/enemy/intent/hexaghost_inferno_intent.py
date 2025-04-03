from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
from ...card.status.burn import Burn, BurnPlus
if TYPE_CHECKING:
    from .. import Enemy

class HexaghostInfernoIntent(AttackIntent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=True)
        # self.damage = 2
        # self.times = 6
        # self.burn = 3

    # def get_damage(self) -> int:
    #     return self.damage * self.times
        
    def perform(self) -> None:
        super().perform()
        # for _ in range(self.times):
        #     self.enemy.attack(self.damage)
        self.enemy.upgrade_burn = True
        for _ in range(self.values[2]):
            if self.enemy.upgrade_burn:
                BurnPlus().to(self.combat).move_to(self.character.discard_pile, is_random=True)
            else:
                Burn().to(self.combat).move_to(self.character.discard_pile, is_random=True)