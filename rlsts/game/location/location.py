from abc import ABC
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

class Location(ABC):
    def __init__(self, floor: int, character: 'Character') -> None:
        self.floor = floor

    def reset(self):
        ...

    def step(self, action: int):
        ...