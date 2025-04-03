import random
from ..enemy import Enemy
from ..intent import Intent, AttackIntent, LagavulinSiphonSoulIntent, SkipIntent

class Lagavulin(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(82, 86) if hp is None else hp)
        self.waked = False
        self.waked_turn = 0
        self.damage = 18
        self.debuff = 1

    def get_intent(self) -> Intent:
        if self.combat.turn == 3 and not self.waked:
            self.wake_up(self.combat.turn)
        if not self.waked or self.combat.turn < self.waked_turn:
            return SkipIntent(self, [])
        if (self.combat.turn - self.waked_turn) % 3 == 2:
            return LagavulinSiphonSoulIntent(self, [self.debuff])
        else:
            return AttackIntent(self, [self.damage], is_multi=False)

    def wake_up(self, turn: int) -> None:
        self.waked = True
        self.waked_turn = turn

    def on_receive_damage(self, damage, attacker) -> None:
        if not self.waked:
            self.wake_up(self.combat.turn + 1)
