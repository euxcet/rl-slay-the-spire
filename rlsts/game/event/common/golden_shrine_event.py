from ...observation.event_observation import EventObservation
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character
from ...card.curse.regret import Regret

class GoldenShrineEvent(OptionsEvent):
    act = [1, 2, 3]
    is_regular = False

    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.gold = 100
        self.options_label = [
            f'[Pray] Gain {self.gold} Gold.',
            '[Desecrate] Gain 275 Gold. Become Cursed - Regret.',
            '[Leave] Nothing happens.'
        ]
        self.options = [True] * len(self.options_label)

    def step(self, action: int) -> EventObservation:
        if super().step(action):
            return None
        if action == 0:
            self.character.receive_gold(self.gold)
        elif action == 1:
            self.character.receive_gold(275)
            self.character.deck.add_cards(Regret())
        elif action == 2:
            ...
        else:
            return self.observe()
        return None
