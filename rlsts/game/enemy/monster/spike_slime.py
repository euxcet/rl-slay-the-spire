import random
from ..enemy import Enemy
from ...effect import Ritual
from ..intent import Intent, SpikeSlimeSplitIntent, SpikeSlimeLickIntent, SpikeSlimeFlameTackleIntent, AttackIntent

class SpikeSlimeL(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(65, 69) if hp is None else hp)
        self.corrosive_spit_damage = 11
        self.corrosive_spit_slimed = 2
        self.attack_damage = 16
        self.lick = 2

    def get_intent(self) -> Intent:
        if self.hp < self.max_hp * 0.5:
            return SpikeSlimeSplitIntent(self, [])
        return self.choose_intent( [
            (SpikeSlimeFlameTackleIntent(self, [self.corrosive_spit_damage, self.corrosive_spit_slimed]), 0.3, 3),
            (AttackIntent(self, [self.attack_damage]), 0.4, 2),
            (SpikeSlimeLickIntent(self, [self.lick]), 0.3, 2),
        ])

class SpikeSlimeM(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(28, 32) if hp is None else hp)
        self.corrosive_spit_damage = 7
        self.corrosive_spit_slimed = 1
        self.attack_damage = 10
        self.lick = 1

    def get_intent(self) -> Intent:
        return self.choose_intent( [
            (SpikeSlimeFlameTackleIntent(self, [self.corrosive_spit_damage, self.corrosive_spit_slimed]), 0.3, 3),
            (AttackIntent(self, [self.attack_damage]), 0.4, 2),
            (SpikeSlimeLickIntent(self, [self.lick]), 0.3, 2),
        ])

class SpikeSlimeS(Enemy):
    def __init__(self) -> None:
        super().__init__(hp=random.randint(8, 12))
        self.attack_damage = 3
        self.lick = 1

    def get_intent(self) -> Intent:
        return self.choose_intent([
            (AttackIntent(self, [self.attack_damage]), 0.5, 2),
            (SpikeSlimeLickIntent(self, [self.lick]), 0.5, 2),
        ])
