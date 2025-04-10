from ...observation.event_observation import EventObservation
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character

class RestSiteEvent(OptionsEvent):
    act = []
    is_regular = False

    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.options_label = [
            '[Rest] Heal for 30% of your max HP.',
            '[Smith] Upgrade 1 card of your choice.',
            # '[Lift] Permanently gain 1 strength.', # Requires Girga. Maximum of 3 uses per run.
            # '[Toke] Remove 1 card from your deck.', # Requires Peace Pipe.
            # '[Dig] Obtain a random relic.', # Requires Shovel.
            # '[Recall] Obtain the Ruby Key.', # Maximum of 1 use per run.
        ]
        self.options = [True] * len(self.options_label)

    def step(self, action: int) -> EventObservation:
        if super().step(action):
            return None
        if action == 0:
            self.heal(percent=0.3)
        elif action == 1:
            return self.remove_card_obs()
        else:
            return self.observe()
