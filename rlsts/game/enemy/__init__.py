from .enemy import Enemy
from .monster.cultist import Cultist
from .monster.louses import RedLouse
from .monster.louses import GreenLouse
from .monster.slimes import AcidSlimeL, AcidSlimeM, AcidSlimeS
from .monster.slimes import SpikeSlimeL, SpikeSlimeM, SpikeSlimeS
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
