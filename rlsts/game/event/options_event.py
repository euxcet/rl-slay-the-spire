import numpy as np
from ..observation.event_observation import EventObservation
from .event import Event, save_obs
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

class OptionsEvent(Event):
    def __init__(
        self,
        character: 'Character',
    ) -> None:
        super().__init__(
            character=character,
        )
        self.options = []
        self.options_label = []
    
    def observe(self) -> EventObservation:
        return EventObservation(
            event_type=type(self),
            options=self.options,
            options_label=self.options_label,
            character_type=type(self.character),
            character_hp=self.character.hp,
            character_max_hp=self.character.max_hp,
            character_gold=self.character.gold,
            character_deck=self.character.deck.cards,
            action_mask=np.array(self.options, dtype=np.int16)
        )

    @save_obs
    def reset(self) -> EventObservation:
        return self.observe()

    @save_obs
    def step(self, action: int) -> EventObservation:
        return super().step(action)
