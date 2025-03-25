import random
from .combat import Combat
from ..character import Character
from ..enemy import Cultist, JawWorm, RedLouse, GreenLouse
from ..enemy import AcidSlimeM, AcidSlimeS, SpikeSlimeM, SpikeSlimeS
from ..enemy import AcidSlimeL, SpikeSlimeL
from ..enemy import BlueSlaver, RedSlaver
from ..enemy import FungiBeast, Looter
from ..enemy import MadGremlin, SneakyGremlin, FatGremlin, GremlinWizard, ShieldGremlin
from ...utils.random import choose_with_prob

class Act1HardCombat(Combat):
    def __init__(self, character: Character) -> None:
        super().__init__(character=character, enemies_type=choose_with_prob([
            (random.sample([MadGremlin, MadGremlin, SneakyGremlin, SneakyGremlin, FatGremlin, FatGremlin, GremlinWizard, ShieldGremlin], 4), 0.0625),
            ([random.choice([AcidSlimeL, SpikeSlimeL])], 0.125),
            ([SpikeSlimeS, SpikeSlimeS, SpikeSlimeS, AcidSlimeS, AcidSlimeS], 0.0625),
            ([BlueSlaver], 0.125),
            ([RedSlaver], 0.0625),
            ([random.choice([GreenLouse, RedLouse]), random.choice([GreenLouse, RedLouse]), random.choice([GreenLouse, RedLouse])], 0.125),
            ([FungiBeast, FungiBeast], 0.125),
            ([random.choice([GreenLouse, RedLouse, AcidSlimeM, SpikeSlimeM]), random.choice([Looter, Cultist, RedSlaver, BlueSlaver])], 0.09375),
            ([random.choice([FungiBeast, JawWorm]), random.choice([RedLouse, GreenLouse, AcidSlimeM, SpikeSlimeM])], 0.09375),
            ([Looter], 0.125),
        ]))
