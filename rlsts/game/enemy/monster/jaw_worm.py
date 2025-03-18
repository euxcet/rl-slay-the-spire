import random
from ..enemy import Enemy
from ..intent import Intent, AttackIntent, ThrashIntent, JawWormBellowIntent

class JawWorm(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(40, 44) if hp is None else hp)
        self.damage = 11
        self.thrash_damage = 7
        self.thrash_block = 5
        self.bellow_strength = 3
        self.bellow_block = 6

    def get_intent(self) -> Intent:
        if self.combat.turn == 0:
            return AttackIntent(self, [self.damage, 1])
        return self.choose_intent([
            (AttackIntent(self, [self.damage, 1]), 0.25, 2),
            (ThrashIntent(self, [self.thrash_damage, self.thrash_block]), 0.3, 3),
            (JawWormBellowIntent(self, [self.bellow_strength, self.bellow_block]), 0.45, 2),
        ])
