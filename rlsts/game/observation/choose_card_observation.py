from __future__ import annotations
import numpy as np
from ..card import Card
from ..card.card_pool import monster_card_pool
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

class ChooseCardObservation():
    def __init__(
        self,
        options: list[Card],
        character_hp: int,
        character_max_hp: int,
        deck: list[Card],
        action_mask: np.ndarray,
        # TODO: relics
        is_over: bool = False,
    ) -> None:
        self.options: list[Card] = options
        self.character_hp = character_hp
        self.character_max_hp = character_max_hp
        self.deck = deck
        self.action_mask = action_mask
        self.is_over = is_over

    def __str__(self) -> str:
        return "ChooseCardObservation"

    def rich(self) -> str:
        options_str = ''
        for i, option in enumerate(self.options):
            if option != None:
                options_str += f'[{i}] {type(option).__name__}\n'
        return "Choose the Card\n" + options_str

    @staticmethod
    def create_observation(character: 'Character', options: list[Card]) -> ChooseCardObservation:
        return ChooseCardObservation(
            options=options,
            character_hp = character.hp,
            character_max_hp = character.max_hp,
            deck = character.deck.cards,
            action_mask = np.ones(len(options) + 1), # 0 for skip
        )

    @staticmethod
    def monster_observation(character: 'Character') -> ChooseCardObservation:
        return ChooseCardObservation.create_observation(
            character=character,
            options=[monster_card_pool.next_card() for i in range(3)]
        )
    
    @staticmethod
    def elite_observation(character: 'Character') -> ChooseCardObservation:
        return ChooseCardObservation.create_observation(
            character=character,
            options=[monster_card_pool.next_card() for i in range(3)]
        )

    @staticmethod
    def boss_observation(character: 'Character') -> ChooseCardObservation:
        return ChooseCardObservation.create_observation(
            character=character,
            options=[monster_card_pool.next_rare_card() for i in range(3)]
        )