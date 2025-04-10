from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..map.map import MapRoom
    from ..character import Character
from .location import Location
from ..event.common.rest_site_event import RestSiteEvent

class RestSiteLocation(Location):
    def __init__(self, room: 'MapRoom', character: 'Character', **kwargs) -> None:
        super().__init__(room=room, character=character)

    def reset(self):
        self.rest_site = RestSiteEvent(character=self.character)
        return self.rest_site.reset()

    def step(self, action: int):
        return self.rest_site.step(action)
