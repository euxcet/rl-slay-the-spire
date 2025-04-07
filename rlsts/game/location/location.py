from abc import ABC
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..map.map import MapRoom
    from ..character import Character

class Location(ABC):
    def __init__(self, room: 'MapRoom', character: 'Character') -> None:
        self.room = room
        self.character = character

    def reset(self):
        ...

    def step(self, action: int):
        ...