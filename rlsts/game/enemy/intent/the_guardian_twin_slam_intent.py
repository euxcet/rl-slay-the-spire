from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...enemy import Enemy

class TheGuardianTwinSlamIntent(AttackIntent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=True)
        # self.values[0] = enemy.estimate_attack(self.values[0])
        # if len(self.values) == 1:
        #     self.values.append(1)

    # def is_attack(self) -> bool:
    #     return True
        
    # def get_damage(self) -> int:
    #     return self.values[0] * self.values[1]

    def perform(self) -> None:
        super().perform()
        # for _ in range(self.values[1]):
        #     self.enemy.attack(self.values[0])
        self.enemy.shift_mode()
