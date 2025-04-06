from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

class NeowLocation():
    def __init__(self, floor: int, character: 'Character') -> None:
        super().__init__(floor=floor, character=character)

    def reset(self):
        ...

    def step(self, action: int):
        ...