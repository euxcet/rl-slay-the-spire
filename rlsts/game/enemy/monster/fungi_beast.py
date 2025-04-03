import random
from ..enemy import Enemy
from ...effect import CurlUp
from ..intent import Intent, AttackIntent, GrowIntent

class FungiBeast(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(22, 28) if hp is None else hp)
        self.damage = 6
        self.grow = 3

    def get_intent(self) -> Intent:
        return self.choose_intent([
            (AttackIntent(self, [self.damage], is_multi=False), 0.6, 3),
            (GrowIntent(self, [self.grow]), 0.4, 2)
        ])
