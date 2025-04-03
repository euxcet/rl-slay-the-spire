from abc import ABC, abstractmethod
from enum import Enum, unique, auto
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat
    from ..enemy import Enemy
    from ...character import Character

class Intent(ABC):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        self.enemy = enemy
        self.values = values
        self.history = []
    
    @property
    def combat(self) -> 'Combat':
        return self.enemy.combat
    
    @property
    def character(self) -> 'Character':
        return self.enemy.combat.character
    
    def is_attack(self) -> bool:
        return False

    def perform(self) -> None:
        ...

    def get_damage(self) -> int:
        return 0

    def __str__(self) -> str:
        if self.values is None or len(self.values) == 0:
            return type(self).__name__
        return f"{type(self).__name__}[{' '.join(map(str, self.values))}]"

    def __repr__(self) -> str:
        return self.__str__()

    def rich(self) -> str:
        if self.values is None or len(self.values) == 0:
            return type(self).__name__
        return f"{type(self).__name__}[{' '.join(map(str, self.values))}]"