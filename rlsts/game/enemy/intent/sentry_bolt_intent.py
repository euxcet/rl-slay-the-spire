from .intent import Intent
from typing import TYPE_CHECKING
from ...card.status.dazed import Dazed
if TYPE_CHECKING:
    from .. import Enemy

class SentryBoltIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)

    def perform(self) -> None:
        for _ in range(self.values[0]):
            Dazed().to(self.combat).move_to(self.character.discard_pile, is_random=True)
