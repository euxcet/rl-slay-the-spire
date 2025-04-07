import random
from .combat import Combat
from .act1_easy_combat import Act1EasyCombat
from .act1_hard_combat import Act1HardCombat
from .act1_elite_combat import Act1EliteCombat
from .act1_boss_combat import Act1BossCombat

def random_combat(character) -> Combat:
    return random.choice([Act1EasyCombat, Act1HardCombat, Act1EliteCombat, Act1BossCombat])(character)
