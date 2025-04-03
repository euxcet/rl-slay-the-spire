from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
from ...card.status.burn import Burn, BurnPlus
if TYPE_CHECKING:
    from .. import Enemy

class HexaghostSearIntent(AttackIntent):
    # damage burn
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=False)
        # self.damage = 6
        # self.burn = 1

    # def get_damage(self) -> int:
    #     return self.damage * self.times
        
    def perform(self) -> None:
        super().perform()
        # self.enemy.attack(self.damage)
        for _ in range(self.values[1]):
            if self.enemy.upgrade_burn:
                BurnPlus().to(self.combat).move_to(self.character.discard_pile, is_random=True)
            else:
                Burn().to(self.combat).move_to(self.character.discard_pile, is_random=True)
