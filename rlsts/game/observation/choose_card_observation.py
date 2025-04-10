import numpy as np
from ..card import Card

class ChooseCardObservation():
    def __init__(
        self,
        options: list[Card],
        action_mask: np.ndarray,
    ) -> None:
        self.options = options
        self.action_mask = action_mask

    def __str__(self) -> str:
        return "ChooseCardObservation"

    def rich(self) -> str:
        options_str = ''
        for i, option in enumerate(self.options):
            if option != None:
                options_str += f'[{i}] {type(option).__name__}\n'
        return "Choose the Card\n" + options_str
