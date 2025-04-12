from __future__ import annotations
import numpy as np
from ..card import Card
from ..card.card_pool import monster_card_pool
class ChooseCardObservation():
    def __init__(
        self,
        options: list[Card],
        action_mask: np.ndarray,
    ) -> None:
        self.options: list[Card] = options
        self.action_mask = action_mask

    def __str__(self) -> str:
        return "ChooseCardObservation"

    def rich(self) -> str:
        options_str = ''
        for i, option in enumerate(self.options):
            if option != None:
                options_str += f'[{i}] {type(option).__name__}\n'
        return "Choose the Card\n" + options_str

    @staticmethod
    def monster_observation() -> ChooseCardObservation:
        options = [monster_card_pool.next_card() for i in range(3)]
        return ChooseCardObservation(
            options=options,
            action_mask=np.ones(len(options)),
        )
    
    @staticmethod
    def elite_observation() -> ChooseCardObservation:
        options = [monster_card_pool.next_card() for i in range(3)]
        return ChooseCardObservation(
            options=options,
            action_mask=np.ones(len(options)),
        )

    @staticmethod
    def elite_observation() -> ChooseCardObservation:
        options = [monster_card_pool.next_card() for i in range(3)]
        return ChooseCardObservation(
            options=options,
            action_mask=np.ones(len(options)),
        )

    @staticmethod
    def boss_observation() -> ChooseCardObservation:
        options = [monster_card_pool.next_rare_card() for i in range(3)]
        return ChooseCardObservation(
            options=options,
            action_mask=np.ones(len(options)),
        )