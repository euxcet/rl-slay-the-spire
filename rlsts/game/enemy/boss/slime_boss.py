import random
from ..enemy import Enemy
from ..intent import Intent, SlimeBossSplitIntent, SlimeBossGoopSprayIntent, SkipIntent, AttackIntent

class SlimeBoss(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(140, 140) if hp is None else hp)
        self.goop_spray = 3
        self.damage = 35

    def get_intent(self) -> Intent:
        if self.hp < self.max_hp * 0.5:
            return SlimeBossSplitIntent(self, [])
        if self.combat.turn % 3 == 0:
            return SlimeBossGoopSprayIntent(self, [self.goop_spray])
        elif self.combat.turn % 3 == 1:
            return SkipIntent(self, [])
        else:
            return AttackIntent(self, [self.damage], is_multi=False)
