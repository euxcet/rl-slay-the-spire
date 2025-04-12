from __future__ import annotations

import numpy as np
from enum import Enum
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from ..card import Card
    from ..card.deck import Deck
    from ..character import Character

class ModifyDeckType(Enum):
    Remove = 0
    Upgrade = 1
    Transform = 2
    Duplicate = 3
    Innate = 4

class ModifyDeckObservation():
    # TODO: add map
    def __init__(
        self,
        type: ModifyDeckType,
        character_hp: int,
        character_max_hp: int,
        deck: list[Card],
        options: list[Card],
        action_mask: np.ndarray,
    ) -> None:
        self.type = type
        self.character_hp = character_hp
        self.character_max_hp = character_max_hp
        self.deck = deck
        self.options = options
        self.action_mask = action_mask

    def __str__(self) -> str:
        return "ModifyDeckObservation"

    def rich(self) -> str:
        options_str = ''
        for i, option in enumerate(self.options):
            if option != None:
                options_str += f'[{i}] {type(option).__name__}\n'
        return f"{self.type.name}\n" + options_str

    @staticmethod
    def _observation(type: ModifyDeckType, character: 'Character', cards: list[Card]) -> ModifyDeckObservation:
        if len(cards) == 0:
            return None
        return ModifyDeckObservation(
            type=type,
            character_hp=character.hp,
            character_max_hp=character.max_hp,
            deck=character.deck.cards,
            options=cards,
            action_mask=np.ones(len(cards)),
        )

    @staticmethod
    def remove_observation(character: 'Character', f: Callable = lambda x: True) -> ModifyDeckObservation:
        cards = character.deck.filter(lambda x: f(x))
        return ModifyDeckObservation._observation(type=ModifyDeckType.Remove, character=character, cards=cards)

    @staticmethod
    def upgrade_observation(character: 'Character', f: Callable = lambda x: True) -> ModifyDeckObservation:
        cards = character.deck.filter(lambda x: not type(x).__name__.endswith('Plus') and f(x))
        return ModifyDeckObservation._observation(type=ModifyDeckType.Upgrade, character=character, cards=cards)

    @staticmethod
    def transform_observation(character: 'Character', f: Callable = lambda x: True) -> ModifyDeckObservation:
        cards = character.deck.filter(lambda x: f(x))
        return ModifyDeckObservation._observation(type=ModifyDeckType.Transform, character=character, cards=cards)

    @staticmethod
    def duplicate_observation(character: 'Character', f: Callable = lambda x: True) -> ModifyDeckObservation:
        cards = character.deck.filter(lambda x: f(x))
        return ModifyDeckObservation._observation(type=ModifyDeckType.Duplicate, character=character, cards=cards)

    @staticmethod
    def innate_observation(character: 'Character', f: Callable = lambda x: True) -> ModifyDeckObservation:
        cards = character.deck.filter(lambda x: not x.is_innate and f(x))
        return ModifyDeckObservation._observation(type=ModifyDeckType.Innate, character=character, cards=cards)
