import random
from ..event import save_obs
from ...observation.event_observation import EventObservation
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character

class WorldOfGoopEvent(OptionsEvent):
    act = [1]
    if_regular = True

    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.lose_gold = random.randint(20, 50)
        self.options_label = [
            '[Gather Gold] Gain 75 Gold. Lose 11 HP.',
            '[Leave It] Lose some gold.',
        ]
        self.options = [True] * len(self.options_label)

    @save_obs
    def step(self, action: int) -> EventObservation:
        if super().step(action):
            return None
        if action == 0:
            self.character.receive_gold(75)
            self.lose_hp(num=11)
        elif action == 1:
            self.character.lose_gold(self.lose_gold)
        else:
            return self.observe()
        return None
