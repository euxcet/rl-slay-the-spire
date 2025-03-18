import numpy as np
from .enemy import Enemy
from .monster.cultist import Cultist
from .monster.red_louse import RedLouse
from .monster.green_louse import GreenLouse
from .monster.acid_slime import AcidSlimeL, AcidSlimeM, AcidSlimeS
from .monster.spike_slime import SpikeSlimeL, SpikeSlimeM, SpikeSlimeS
from ...utils.collection import Collection

enemy_collection = Collection()
enemy_collection.add(Cultist)
enemy_collection.add(RedLouse)
enemy_collection.add(GreenLouse)
enemy_collection.add(AcidSlimeL)
enemy_collection.add(AcidSlimeM)
enemy_collection.add(AcidSlimeS)
enemy_collection.add(SpikeSlimeL)
enemy_collection.add(SpikeSlimeM)
enemy_collection.add(SpikeSlimeS)
