from ..event_observation import EventObservation
from ..event import Event
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character
from ...card.curse.doubt import Doubt

class TheSsssserpentEvent(OptionsEvent):
    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.gold = 150
        self.options_label = [
            f'[Agree] Receive {self.gold} Gold. Become Cursed - Doubt.',
            '[Disagree] Nothing happens.',
        ]
        self.options = [True] * len(self.options_label)

    def step(self, action: int) -> EventObservation:
        if action == 0:
            self.character.receive_gold(self.gold)
            self.character.deck.add_cards(Doubt())
        elif action == 1:
            return None
