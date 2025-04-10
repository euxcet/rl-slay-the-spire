import math
from abc import ABC, abstractmethod
from ..observation.event_observation import EventObservation
from ..observation.modify_deck_observation import ModifyDeckObservation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

class Event(ABC):
    act = []
    is_regular = True

    def __init__(
        self, 
        character: 'Character',
        # act: list[int],
        # is_regular: bool,
    ) -> None:
        self.character = character
        self.is_removing = False
        self.is_upgrading = False
        self.is_transforming = False
        # self.act = act
        # self.is_regular = is_regular

    @property
    def valid(self) -> bool:
        return True

    @abstractmethod
    def reset(self) -> EventObservation:
        ...

    @abstractmethod
    def step(self, action: int) -> bool:
        if self.is_removing:
            self.remove_card(action)
            return True
        if self.is_upgrading:
            self.upgrade_card(action)
            return True
        if self.is_transforming:
            self.transform_card(action)
            return True
        return False

    def heal(self, percent: float) -> None:
        self.character.hp = min(self.character.hp + math.floor(self.character.max_hp * percent), self.character.max_hp)
    
    def lose_hp(self, num: int = None, percent: float = None) -> None:
        if num is None:
            num = math.floor(self.character.max_hp * percent)
        self.character.hp = max(self.character.hp - num, 0)

    def lose_max_hp(self, num: int = None, percent: float = None) -> None:
        self.character.lose_max_hp(num=num, percent=percent)

    def gain_max_hp(self, num: int = None, percent: float = None) -> None:
        self.character.gain_max_hp(num=num, percent=percent)

    def remove_card(self, action: int) -> None:
        # len(deck) > 0
        self.is_removing = False
        return None

    def remove_card_obs(self) -> ModifyDeckObservation:
        self.is_removing = True
        ...

    # upgrade a random card if action is None
    def upgrade_card(self, action: int | None = None) -> None:
        # len(deck) > 0
        self.is_upgrading = False
        return None

    def upgrade_card_obs(self) -> ModifyDeckObservation:
        self.is_upgrading = True
        ...

    def transform_card(self, action: int) -> None:
        # len(deck) > 0
        self.is_transforming = False
        return None

    def transform_card_obs(self) -> ModifyDeckObservation:
        self.is_transforming = True
        ...

    def duplicate_card(self, action: int) -> None:
        # len(deck) > 0
        self.is_transforming = False
        return None

    def duplicate_card_obs(self) -> ModifyDeckObservation:
        self.is_transforming = True
        ...