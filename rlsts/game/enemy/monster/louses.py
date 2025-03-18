import random
from ..enemy import Enemy
from ...effect import CurlUp
from ..intent import Intent, LouseSpitWebIntent, AttackIntent, GrowIntent

class GreenLouse(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(11, 17) if hp is None else hp)
        self.bite_damage = random.randint(5, 7)
        self.spit_web = 2

    def start_combat(self, combat) -> None:
        super().start_combat(combat)
        self.receive_effect(CurlUp(self.combat, random.randint(3, 7)))

    def get_intent(self) -> Intent:
        return self.choose_intent([
            (AttackIntent(self, [self.bite_damage, 1]), 0.75, 3),
            (LouseSpitWebIntent(self, [self.spit_web]), 0.25, 3),
        ])

class RedLouse(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(10, 15) if hp is None else hp)
        self.bite_damage = random.randint(5, 7)
        self.grow = 3

    def start_combat(self, combat) -> None:
        super().start_combat(combat)
        self.receive_effect(CurlUp(self.combat, random.randint(3, 7)))

    def get_intent(self) -> Intent:
        return self.choose_intent([
            (AttackIntent(self, [self.bite_damage, 1]), 0.75, 3),
            (GrowIntent(self, [self.grow]), 0.25, 3),
        ])