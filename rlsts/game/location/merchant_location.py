from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..map.map import MapRoom
    from ..character import Character
from .location import Location
from ..event.common.merchant_event import MerchantEvent

class MerchantLocation(Location):
    def __init__(self, room: 'MapRoom', character: 'Character', **kwargs) -> None:
        super().__init__(room=room, character=character)

    def reset(self):
        self.merchant = MerchantEvent(character=self.character)
        return self.merchant.reset()

    def step(self, action: int):
        return self.merchant.step(action)
