import random
from .combat import Combat
from .combat_observation import CombatObservation
from .act1_easy_combat import Act1EasyCombat
from .act1_hard_combat import Act1HardCombat

def random_combat(character) -> Combat:
    return random.choice([Act1EasyCombat, Act1HardCombat])(character)
