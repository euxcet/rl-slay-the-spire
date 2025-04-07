from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..map.map import MapRoom
    from ..character import Character
from .location import Location
from ..combat import Act1EliteCombat

class EliteLocation(Location):
    def __init__(self, room: 'MapRoom', character: 'Character', **kwargs) -> None:
        super().__init__(room=room, character=character)

    def reset(self):
        self.combat = Act1EliteCombat(character=self.character)
        return self.combat.reset()

    def step(self, action: int):
        return self.combat.step(action)
