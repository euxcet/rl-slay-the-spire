from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..map.map import MapRoom
    from ..character import Character
from .location import Location
from ..event import NeowEvent

class NeowLocation(Location):
    def __init__(self, room: 'MapRoom', character: 'Character', **kwargs) -> None:
        super().__init__(room=room, character=character)
        self.neow = NeowEvent(character=character)

    def reset(self):
        return self.neow.reset()

    def step(self, action: int):
        return self.neow.step(action)
