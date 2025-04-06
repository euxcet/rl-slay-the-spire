from ..event_observation import EventObservation
from ..event import Event
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character
from ...card.curse.injury import Injury

class GoldenIdolEvent(OptionsEvent):
    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.smash_percent = 25
        self.hide_percent = 8
        self.options_label = [
            '[Outrun] Become Cursed - Injury.',
            f'[Smash] Take damage equal to {self.smash_percent}% of Max HP.',
            f'[Hide] Lose {self.hide_percent}% Max HP.',
            '[Leave] Nothing happens.',
        ]
        self.options = [True] * len(self.options_label)
        
    def step(self, action: int) -> EventObservation:
        if action == 0:
            self.character.deck.add_cards(Injury())
        elif action == 1:
            self.lose_hp(self.smash_percent / 100)
        elif action == 2:
            self.lose_max_hp(self.hide_percent / 100)
        return None
