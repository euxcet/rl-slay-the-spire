import numpy as np
from .enemy import Enemy
from .monster.cultist import Cultist
from .monster.red_louse import RedLouse
from ...utils.collection import Collection

enemy_collection = Collection()
enemy_collection.add(Cultist)
enemy_collection.add(RedLouse)
