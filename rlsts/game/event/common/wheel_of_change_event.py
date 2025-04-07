import random
from ...observation.event_observation import EventObservation
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character
from ...card.curse.decay import Decay

class WheelOfChangeEvent(OptionsEvent):
    act = [1, 2, 3]
    is_regular = False

    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.result = random.randint(0, 5)
        self.hp_cost = 0.1
        self.options_label = [
            '[Play] Spin the wheel and get a prize.',
        ]
        self.options = [True] * len(self.options_label)

    def step(self, action: int) -> EventObservation:
        if super().step(action):
            return None
        if self.result == 0:
            self.character.receive_gold(self.character.act * 100)
        elif self.result == 1:
            self.character.receive_relic()
        elif self.result == 2:
            self.heal(1)
        elif self.result == 3:
            self.character.deck.add_cards(Decay())
        elif self.result == 4:
            return self.remove_card_obs()
        elif self.result == 5:
            self.lose_hp(percent=self.hp_cost)
        return None
