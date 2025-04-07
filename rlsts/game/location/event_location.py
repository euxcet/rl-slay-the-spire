from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..map.map import MapRoom
    from ..character import Character
from .location import Location
from ..event import Event, event_collection, choose_event, act1_event_collection

class EventLocation(Location):
    def __init__(self, room: 'MapRoom', character: 'Character', **kwargs) -> None:
        super().__init__(room=room, character=character)

    def reset(self):
        self.event: Event = choose_event(act1_event_collection)(character=self.character)
        return self.event.reset()

    def step(self, action: int):
        return self.event.step(action)
