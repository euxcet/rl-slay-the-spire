from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
from ...card import Slimed
if TYPE_CHECKING:
    from .. import Enemy

class SpikeSlimeFlameTackleIntent(AttackIntent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=False)
        # self.values[0] = enemy.estimate_attack(self.values[0])

    # def is_attack(self) -> bool:
    #     return True

    # def get_damage(self):
    #     return self.values[0]
        
    def perform(self) -> None:
        super().perform()
        # self.enemy.attack(self.values[0])
        for _ in range(self.values[1]):
            Slimed().to(self.combat).move_to(self.character.discard_pile, is_random=True)
