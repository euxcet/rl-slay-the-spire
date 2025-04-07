from ...observation.event_observation import EventObservation
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character

class NeowEvent(OptionsEvent):
    act = [0]
    is_regular = True

    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.options_label = [
            'Max HP + 8',
        ]
        self.options = [True] * len(self.options_label)

    def step(self, action: int) -> EventObservation:
        if super().step(action):
            return None
        if action == 0:
            self.gain_max_hp(num=8)
            return None
        else:
            return self.observe()
