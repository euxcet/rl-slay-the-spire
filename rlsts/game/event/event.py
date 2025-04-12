import random
import math
import copy
from abc import ABC, abstractmethod
from ..observation.event_observation import EventObservation
from ..observation.modify_deck_observation import ModifyDeckObservation
from ..card import upgrade, ironclad_all_cards
from typing import TYPE_CHECKING
from functools import wraps
if TYPE_CHECKING:
    from ..character import Character

def save_obs(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        obs = func(self, *args, **kwargs)
        self.last_obs = obs
        return obs
    return wrapper

class Event(ABC):
    act = []
    is_regular = True

    def __init__(
        self, 
        character: 'Character',
    ) -> None:
        self.character = character
        self.is_removing = False
        self.is_upgrading = False
        self.is_transforming = False
        self.last_obs = None

    @property
    def valid(self) -> bool:
        return True

    @abstractmethod
    @save_obs
    def reset(self) -> EventObservation:
        ...

    @abstractmethod
    @save_obs
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
        self.character.deck.remove_cards(self.last_obs.options[action])
        self.is_removing = False
        return None

    def remove_card_obs(self) -> ModifyDeckObservation:
        self.is_removing = True
        return ModifyDeckObservation.remove_observation(self.character)

    def upgrade_card(self, action: int | None = None) -> None:
        self.character.deck.remove_cards(self.last_obs.options[action])
        self.character.deck.add_cards(upgrade(self.last_obs.options[action]))
        self.is_upgrading = False
        return None

    def upgrade_card_obs(self) -> ModifyDeckObservation:
        self.is_upgrading = True
        return ModifyDeckObservation.upgrade_observation(self.character)

    def transform_card(self, action: int) -> None:
        self.character.deck.remove_cards(self.last_obs.options[action])
        self.character.deck.add_cards(random.choice(ironclad_all_cards())())
        self.is_transforming = False
        return None

    def transform_card_obs(self) -> ModifyDeckObservation:
        self.is_transforming = True
        return ModifyDeckObservation.transform_observation(self.character)

    def duplicate_card(self, action: int) -> None:
        self.character.deck.add_cards(copy.deepcopy(self.last_obs.options[action]))
        self.is_transforming = False
        return None

    def duplicate_card_obs(self) -> ModifyDeckObservation:
        self.is_transforming = True
        return ModifyDeckObservation.duplicate_observation(self.character)