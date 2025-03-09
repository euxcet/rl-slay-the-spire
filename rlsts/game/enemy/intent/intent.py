from enum import Enum, unique, auto

@unique
class IntentType(Enum):
    ATTACK = auto()
    CULTIST_INCANTATION = auto()

class Intent():
    def __init__(self, type: IntentType, values: list[int]) -> None:
        self.type = type
        self.values = values