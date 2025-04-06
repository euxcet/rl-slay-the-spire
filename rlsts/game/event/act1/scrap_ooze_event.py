import math
import random
from ..event_observation import EventObservation
from ..event import Event
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character

class ScrapOozeEvent(OptionsEvent):
    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.hp_cost = 3
        self.prob = 0.25
        self.options_label = [
            f'[Reach Inside] Lose {self.hp_cost} HP. {math.floor(self.prob * 100)}% chance to find a Relic.',
            '[Leave] Nothing happens.',
        ]
        self.options = [True] * len(self.options_label)

    def step(self, action: int) -> EventObservation:
        if action == 0:
            self.character.lose_hp(self.hp_cost)
            if random.random() < self.prob:
                self.character.receive_relic()
                return None
            self.hp_cost += 1
            self.prob += 0.1
            return self.observe()
        elif action == 1:
            return None
