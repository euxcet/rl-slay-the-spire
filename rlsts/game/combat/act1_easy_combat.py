import random
from .combat import Combat
from ..character import Character
from ..enemy import Cultist, JawWorm, RedLouse, GreenLouse
from ..enemy import AcidSlimeM, AcidSlimeS, SpikeSlimeM, SpikeSlimeS
from ...utils.random import choose_with_prob

class Act1EasyCombat(Combat):
    def __init__(self, character: Character) -> None:
        super().__init__(character=character, enemies_type=choose_with_prob([
            ([Cultist], 0.25),
            ([JawWorm], 0.25),
            ([random.choice([GreenLouse, RedLouse]), random.choice([GreenLouse, RedLouse])], 0.25),
            ([random.choice([AcidSlimeM, SpikeSlimeM]), random.choice([AcidSlimeS, SpikeSlimeS])] , 0.25),
        ]))
