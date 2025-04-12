from ...observation.event_observation import EventObservation
from ..event import save_obs
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character

class TheClericEvent(OptionsEvent):
    act = [1]
    is_regular = True

    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.purify_gold = 50
        self.options_label = [
            '[Heal] Lose 35 Gold. Heal 25% of your Max HP.',
            f'[Purify] Lose {self.purify_gold} Gold. Remove a card from your deck.',
            '[Leave] Nothing happens.',
        ]
        self.options = [True] * len(self.options_label)
        
    @property
    def valid(self) -> bool:
        return self.character.gold >= 35

    @save_obs
    def step(self, action: int) -> EventObservation:
        if super().step(action):
            return None
        if action == 0:
            self.character.lose_gold(35)
            self.heal(0.25)
        elif action == 1:
            self.character.lose_gold(self.purify_gold)
            return self.remove_card_obs()
        elif action == 2:
            ...
        else:
            return self.observe()
        return None
