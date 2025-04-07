from ...observation.event_observation import EventObservation
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character

class PurifierEvent(OptionsEvent):
    act = [1, 2, 3]
    is_regular = False

    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.options_label = [
            '[Pray] Remove a card from your deck.',
            '[Leave] Nothing happens.',
        ]
        self.options = [True] * len(self.options_label)

    def step(self, action: int) -> EventObservation:
        if super().step(action):
            return None
        if action == 0:
            return self.remove_card_obs()
        elif action == 1:
            return None
        else:
            return self.observe()
