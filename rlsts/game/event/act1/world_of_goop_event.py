import random
from ..event_observation import EventObservation
from ..event import Event
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character
from ...card.curse.doubt import Doubt

class WorldOfGoopEvent(OptionsEvent):
    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.gold = 75
        self.hp_cost = 11
        self.lose_gold = random.randint(20, 50)
        self.options_label = [
            '[Gather Gold] Gain 75 Gold. Lose 11 HP.',
            '[Leave It] Lose some gold.',
        ]
        self.options = [True] * len(self.options_label)

    def step(self, action: int) -> EventObservation:
        if action == 0:
            self.character.receive_gold(self.gold)
            self.character.lose_hp(self.hp_cost)
        elif action == 1:
            self.character.lose_gold(self.lose_gold)
            return None
