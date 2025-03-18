from .intent import Intent
from typing import TYPE_CHECKING
from ...effect import Weak, Frail
if TYPE_CHECKING:
    from .. import Enemy

class GremlinWizardChargingIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values)

    def perform(self) -> None:
        ...