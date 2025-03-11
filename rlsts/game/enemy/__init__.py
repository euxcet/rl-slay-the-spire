import numpy as np
from .enemy import Enemy
from .monster.cultist import Cultist
from ...utils.collection import Collection

enemy_collection = Collection()
enemy_collection.add(Cultist)
