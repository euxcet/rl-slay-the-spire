import random
from ..enemy import Enemy

class Cultist(Enemy):
    def __init__(self):
        super().__init__(hp=random.randint(48, 54))
