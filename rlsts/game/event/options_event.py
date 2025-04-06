from .event_observation import EventObservation
from .event import Event
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

class OptionsEvent(Event):
    def __init__(self, character: 'Character') -> None:
        super().__init__(character=character)
        self.options = []
        self.options_label = []
    
    def observe(self) -> EventObservation:
        return EventObservation(
            event_type=type(self),
            options=self.options,
            options_label=self.options_label,
        )

    def reset(self) -> EventObservation:
        return self.observe()

    def step(self, action: int) -> EventObservation:
        return super().step(action)
