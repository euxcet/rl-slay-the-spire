import random
from ..enemy import Enemy
from ...effect import Thievery
from ..intent import Intent, AttackIntent, LooterEscapeIntent, BlockIntent

class Looter(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(44, 48) if hp is None else hp)
        self.thievery = 15
        self.mug = 10
        self.lunge = 12
        self.smoke = 6

    def start_combat(self, combat) -> None:
        super().start_combat(combat)
        self.receive_effect(Thievery(self.combat, self.thievery))

    def get_intent(self) -> Intent:
        if self.combat.turn < 2:
            return AttackIntent(self, [self.mug], is_multi=False)
        if type(self.intent_history[-1]) is BlockIntent:
            return LooterEscapeIntent(self, [])
        if self.combat.turn == 2:
            if self.intent_pool.peek(self.combat.turn) < 0.5:
                return AttackIntent(self, [self.lunge], is_multi=False)
            else:
                return BlockIntent(self, [])
        return BlockIntent(self, [])

class Mugger(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(48, 52) if hp is None else hp)
        self.thievery = 15
        self.mug = 10
        self.lunge = 16
        self.smoke = 11

    def start_combat(self, combat) -> None:
        super().start_combat(combat)
        self.receive_effect(Thievery(self.combat, self.thievery))

    def get_intent(self) -> Intent:
        if self.combat.turn < 2:
            return AttackIntent(self, [self.mug], is_multi=False)
        if type(self.intent_history[-1]) is BlockIntent:
            return LooterEscapeIntent(self, [])
        if self.combat.turn == 2:
            if self.intent_pool.peek(self.combat.turn) < 0.5:
                return AttackIntent(self, [self.lunge], is_multi=False)
            else:
                return BlockIntent(self, [])
        return BlockIntent(self, [])
