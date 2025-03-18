from enum import Enum, unique, auto

@unique
class IntentType(Enum):
    ATTACK = auto()
    CULTIST_INCANTATION = auto()
    LOUSE_GROW = auto()
    LOUSE_SPIT_WEB = auto()

class Intent():
    def __init__(self, type: IntentType, values: list[int]) -> None:
        self.type = type
        self.values = values
    
    def get_damage(self) -> int:
        if self.type == IntentType.ATTACK:
            assert len(self.values) in [1, 2]
            if len(self.values) == 1:
                return self.values[0]
            else:
                return self.values[0] * self.values[1]
        return 0

    def __str__(self) -> str:
        if self.type is IntentType.ATTACK:
            return f'{self.type.name} {self.values[0]} * {self.values[1]} = {self.values[0] * self.values[1]}'
        return self.type.name

    def __repr__(self) -> str:
        return self.__str__()

    def rich(self) -> str:
        if self.type is IntentType.ATTACK:
            return f'{self.type.name} {self.values[0]} * {self.values[1]} = [bold red]{self.values[0] * self.values[1]}[/bold red]'
        if self.values is None or len(self.values) == 0:
            return self.type.name
        return f"{self.type.name}[{' '.join(map(str, self.values))}]"