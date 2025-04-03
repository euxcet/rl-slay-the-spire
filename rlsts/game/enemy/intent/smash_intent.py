from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
from ...effect import Weak, Frail
if TYPE_CHECKING:
    from .. import Enemy

class SmashIntent(AttackIntent):
    # attack weak frail
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=False)
        # self.values[0] = enemy.estimate_attack(self.values[0])
        if len(self.values) == 2:
            self.values.append(0)

    # def is_attack(self) -> bool:
    #     return True

    # def get_damage(self) -> int:
    #     return self.values[0]

    def perform(self) -> None:
        super().perform()
        # self.enemy.attack(self.values[0])
        self.character.receive_effect(Weak(self.combat, self.values[1]))
        self.character.receive_effect(Frail(self.combat, self.values[2]))
