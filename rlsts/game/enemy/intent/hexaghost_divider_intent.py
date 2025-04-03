from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Enemy

class HexaghostDividerIntent(AttackIntent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=True)

    @property
    def values(self) -> list[int]:
        return [self.character.hp // 12, 6]

    @values.setter
    def values(self, _values):
        ...
        