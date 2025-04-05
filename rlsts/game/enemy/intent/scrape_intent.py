from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
from ...effect import Vulnerable
if TYPE_CHECKING:
    from .. import Enemy

class ScrapeIntent(AttackIntent):
    # attack vulnerable
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=False)

    def perform(self) -> None:
        super().perform()
        self.character.receive_effect(Vulnerable(self.combat, self.values[1]))
