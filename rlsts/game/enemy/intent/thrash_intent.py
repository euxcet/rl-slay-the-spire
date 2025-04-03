from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...enemy import Enemy

class ThrashIntent(AttackIntent):
    # values: attack block
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=False)
        # self.values[0] = enemy.estimate_attack(self.values[0])

    # def is_attack(self) -> bool:
    #     return True
        
    # def get_damage(self) -> int:
    #     return self.values[0]

    def perform(self) -> None:
        super().perform()
        # self.enemy.attack(self.values[0])
        self.enemy.add_block(self.values[1])
