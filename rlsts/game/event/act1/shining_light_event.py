import math
from ..event_observation import EventObservation
from ..event import Event
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character

class ShiningLightEvent(OptionsEvent):
    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.hp_cost = 0.2
        self.options_label = [
            f'[Enter] Upgrade 2 random cards. Take {math.floor(self.hp_cost * 100)}% of your max HP in damage.',
            '[Leave] Nothing happens.',
        ]
        self.options = [True] * len(self.options_label)

    def step(self, action: int) -> EventObservation:
        if action == 0:
            self.lose_hp(self.hp_cost)
            self.upgrade_card()
            self.upgrade_card()
        elif action == 1:
            return None
