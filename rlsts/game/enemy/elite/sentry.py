import random
from ..enemy import Enemy
from ..intent import Intent, AttackIntent, SentryBoltIntent
from ...effect.buff.artifact import Artifact

class Sentry(Enemy):
    def __init__(self, hp: int = None, start_state: int = 0) -> None:
        super().__init__(hp=random.randint(82, 86) if hp is None else hp)
        self.start_state = start_state
        self.artifact = 1
        self.damage = 9
        self.bolt = 2

    def start_combat(self, combat) -> None:
        super().start_combat(combat)
        self.receive_effect(Artifact(self.combat, self.artifact))

    def get_intent(self) -> Intent:
        if (self.combat.turn + self.start_state) % 2 == 0:
            return SentryBoltIntent(self, [self.bolt])
        else:
            return AttackIntent(self, [self.damage], is_multi=False)
