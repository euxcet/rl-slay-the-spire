from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
from ...effect import Weak, Frail
if TYPE_CHECKING:
    from .. import Enemy

class SmashIntent(AttackIntent):
    # attack weak frail
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=False)
        if len(self.values) == 2:
            self.values.append(0)

    def perform(self) -> None:
        super().perform()
        self.character.receive_effect(Weak(self.combat, self.values[1]))
        self.character.receive_effect(Frail(self.combat, self.values[2]))
