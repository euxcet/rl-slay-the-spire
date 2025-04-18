import numpy as np
from ..map.map import MapRoom

class ChooseRoomObservation():
    def __init__(
        self,
        options: list[MapRoom],
        action_mask: np.ndarray,
    ) -> None:
        self.options = options
        self.action_mask = action_mask

    def __str__(self) -> str:
        return "ChooseRoomObservation"

    def rich(self) -> str:
        options_str = ''
        for i, option in enumerate(self.options):
            if option != None:
                options_str += f'[{i}] {option.location.name}\n'
        return "Choose Next Room\n" + options_str
