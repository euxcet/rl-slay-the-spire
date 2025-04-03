import random
from .combat import Combat
from ..character import Character
from ..enemy import Hexaghost, SlimeBoss, TheGuardian
from ...utils.random import choose_with_prob

class Act1BossCombat(Combat):
    def __init__(self, character: Character) -> None:
        super().__init__(character=character, enemies_type=choose_with_prob([
            # ([Hexaghost], 1 / 3),
            # ([SlimeBoss], 1 / 3),
            ([TheGuardian], 1 / 3),
        ]))
