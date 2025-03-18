from .character import Ironclad
from .combat import Combat
from .enemy import Cultist
from .enemy import RedLouse

class SlayTheSpire():
    def __init__(self) -> None:
        self.character = Ironclad()

    def get_combat(self) -> Combat:
        return Combat(self.character, [RedLouse()])
