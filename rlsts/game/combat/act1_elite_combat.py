import random
from .combat import Combat
from ..character import Character
from ..enemy import GremlinNob, Lagavulin, Sentry
from ...utils.random import choose_with_prob

class Act1EliteCombat(Combat):
    def __init__(self, character: Character) -> None:
        super().__init__(character=character, enemies_type=choose_with_prob([
            ([GremlinNob], 1 / 3),
            ([Lagavulin], 1 / 3),
            ([(Sentry, {'start_state': 0}), (Sentry, {'start_state': 1}), (Sentry, {'start_state': 0})], 1 / 3),
        ]))
