from .enemy import Enemy
from .monster.cultist import Cultist
from .monster.louses import RedLouse, GreenLouse
from .monster.slimes import AcidSlimeL, AcidSlimeM, AcidSlimeS
from .monster.slimes import SpikeSlimeL, SpikeSlimeM, SpikeSlimeS
from .monster.fungi_beast import FungiBeast
from .monster.gremlins import FatGremlin, MadGremlin, ShieldGremlin, SneakyGremlin, GremlinWizard
from .monster.slavers import RedSlaver, BlueSlaver
from .monster.thieves import Looter, Mugger
from .monster.jaw_worm import JawWorm

from .elite.gremlin_nob import GremlinNob
from .elite.lagavulin import Lagavulin
from .elite.sentry import Sentry

from .boss.hexaghost import Hexaghost
from .boss.slime_boss import SlimeBoss
from .boss.the_guardian import TheGuardian

from ...utils.collection import Collection

enemy_collection = Collection()

# monsters
enemy_collection.add(Cultist)
enemy_collection.add(RedLouse)
enemy_collection.add(GreenLouse)
enemy_collection.add(AcidSlimeL)
enemy_collection.add(AcidSlimeM)
enemy_collection.add(AcidSlimeS)
enemy_collection.add(SpikeSlimeL)
enemy_collection.add(SpikeSlimeM)
enemy_collection.add(SpikeSlimeS)
enemy_collection.add(JawWorm)
enemy_collection.add(FungiBeast)
enemy_collection.add(RedSlaver)
enemy_collection.add(BlueSlaver)
enemy_collection.add(Looter)
enemy_collection.add(Mugger)
enemy_collection.add(FatGremlin)
enemy_collection.add(MadGremlin)
enemy_collection.add(ShieldGremlin)
enemy_collection.add(SneakyGremlin)
enemy_collection.add(GremlinWizard)

# elites
enemy_collection.add(GremlinNob)
enemy_collection.add(Lagavulin)
enemy_collection.add(Sentry)

# bosses
enemy_collection.add(Hexaghost)
enemy_collection.add(SlimeBoss)
enemy_collection.add(TheGuardian)
