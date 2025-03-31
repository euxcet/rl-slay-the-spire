from abc import ABC, abstractmethod
from enum import Enum, unique, auto
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..enemy import Enemy

class Intent(ABC):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        self.enemy = enemy
        self.values = values
        self.history = []
    
    def is_attack(self) -> bool:
        return False

    def perform(self) -> None:
        ...

    def get_damage(self) -> int:
        return 0

    def __str__(self) -> str:
        # if self.type is IntentType.ATTACK:
        #     return f'{self.type.name} {self.values[0]} * {self.values[1]} = {self.values[0] * self.values[1]}'
        if self.values is None or len(self.values) == 0:
            return type(self).__name__
        return f"{type(self).__name__}[{' '.join(map(str, self.values))}]"

    def __repr__(self) -> str:
        return self.__str__()

    def rich(self) -> str:
        # if self.type is IntentType.ATTACK:
        #     return f'{self.type.name} {self.values[0]} * {self.values[1]} = [bold red]{self.values[0] * self.values[1]}[/bold red]'
        if self.values is None or len(self.values) == 0:
            return type(self).__name__
        return f"{type(self).__name__}[{' '.join(map(str, self.values))}]"