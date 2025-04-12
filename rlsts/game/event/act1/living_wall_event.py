from ...observation.event_observation import EventObservation
from ..event import save_obs
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character
from ...card.curse.injury import Injury

class LivingWallEvent(OptionsEvent):
    act = [1]
    is_regular = True

    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.options_label = [
            '[Forget] Remove a card from your deck.',
            '[Change] Transform a card in your deck.',
            '[Grow] Upgrade a card in your deck.',
        ]
        self.options = [True] * len(self.options_label)

    @save_obs
    def step(self, action: int) -> EventObservation:
        if super().step(action):
            return None
        if action == 0:
            return self.remove_card_obs()
        elif action == 1:
            return self.transform_card_obs()
        elif action == 2:
            return self.upgrade_card_obs()
        else:
            return self.observe()
