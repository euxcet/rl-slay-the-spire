from ...observation.event_observation import EventObservation
from ..event import save_obs
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character
from ...card.curse.regret import Regret

class BigFishEvent(OptionsEvent):
    act = [1]
    is_regular = True
    
    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.options_label = [
            '[Banana] Heal 1/3 of your max HP.',
            '[Donut] Max HP + 5.',
            '[Box] Receive a Relic. Become Cursed: Regret.',
        ]
        self.options = [True] * len(self.options_label)

    @save_obs
    def step(self, action: int) -> EventObservation:
        if super().step(action):
            return None
        if action == 0:
            self.heal(1 / 3)
        elif action == 1:
            self.gain_max_hp(num=5)
        elif action == 2:
            self.character.deck.add_cards(Regret())
            self.character.receive_relic()
        else:
            return self.observe()
        return None