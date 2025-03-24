from .character import Ironclad
from .combat import Combat
from .enemy import Cultist, RedLouse, GreenLouse, AcidSlimeL, AcidSlimeM, AcidSlimeS
from .enemy import SpikeSlimeL, SpikeSlimeM, SpikeSlimeS

class SlayTheSpire():
    def __init__(self) -> None:
        self.character = Ironclad()

    def get_combat(self) -> Combat:
        return Combat(self.character, [Cultist])
