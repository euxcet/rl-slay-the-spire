from ...observation.event_observation import EventObservation
from ..options_event import OptionsEvent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character
from ...card.curse.pain import Pain

class OminousForgeEvent(OptionsEvent):
    act = [1, 2, 3]
    is_regular = False

    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.options_label = [
            '[Forge] Upgrade a card (Requires an upgradable card).',
            '[Rummage] Obtain Warped Tongs. Become Cursed - Pain.',
            '[Leave] Nothing happens.',
        ]
        self.options = [True] * len(self.options_label)

    def step(self, action: int) -> EventObservation:
        if super().step(action):
            return None
        if action == 0:
            return self.upgrade_card_obs()
        elif action == 1:
            # TODO obtain Warped Tongs
            self.character.deck.add_cards(Pain())
        elif action == 2:
            ...
        else:
            return self.observe()
        return None
