import random
from ..enemy import Enemy
from ...effect import Angry
from ..intent import Intent, AttackIntent, SmashIntent, GremlinWizardChargingIntent, ShieldGremlinProtectIntent

class FatGremlin(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(13, 17) if hp is None else hp)
        self.damage = 4
        self.weak = 1

    def get_intent(self) -> Intent:
        return SmashIntent(self, [self.damage, self.weak])

class MadGremlin(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(20, 24) if hp is None else hp)
        self.damage = 4
        self.angry = 1

    def start_combat(self, combat) -> None:
        super().start_combat(combat)
        self.receive_effect(Angry(self.combat, self.angry))

    def get_intent(self) -> Intent:
        return AttackIntent(self, [self.damage], is_multi=False)

class ShieldGremlin(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(20, 24) if hp is None else hp)
        self.damage = 6
        self.protect = 7
        self.last_turn = -1
        self.target = None

    def get_intent(self) -> Intent:
        if self.combat.turn != self.last_turn:
            self.target = None
            self.combat.turn = self.last_turn
            if len(self.combat.enemies) > 1:
                while True:
                    self.target = self.combat.enemies[self.intent_pool.get_int(0, len(self.combat.enemies))]
                    if self.target != self:
                        break
        if self.target is not None and not self.target.died:
            return ShieldGremlinProtectIntent(self, [self.target, self.protect])
        if self.target is not None:
            return ShieldGremlinProtectIntent(self, [self, self.protect])
        return AttackIntent(self, [self.damage], is_multi=False)

class SneakyGremlin(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(10, 14) if hp is None else hp)
        self.damage = 9

    def get_intent(self) -> Intent:
        return AttackIntent(self, [self.damage], is_multi=False)

class GremlinWizard(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(23, 25) if hp is None else hp)
        self.damage = 25
        self.first_turn = 2
        self.gap_turn = 4

    def get_intent(self) -> Intent:
        if self.combat.turn >= self.first_turn and (self.combat.turn - self.first_turn) % self.gap_turn == 0:
            return AttackIntent(self, [self.damage], is_multi=False)
        return GremlinWizardChargingIntent(self, [])
