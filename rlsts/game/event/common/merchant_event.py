from ...observation.merchat_observation import MerchantObservation
from ..event import Event
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character

class MerchantEvent(Event):
    act = []
    is_regular = False

    # 5 Colored Cards (Class-Specific)
    # 2 Colorless Cards
    # 3 Relics
    # 3 Potions
    # Card Removal Service

    def __init__(self, character: 'Character', ) -> None:
        super().__init__(character=character)
        self.options_label = [
        ]
        self.options = [True] * len(self.options_label)

    def observe(self) -> MerchantObservation:
        return MerchantObservation(

        )

    def reset(self) -> MerchantObservation:
        return self.observe()

    def step(self, action: int) -> MerchantObservation:
        if super().step(action):
            return None
