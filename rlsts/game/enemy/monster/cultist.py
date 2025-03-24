import random
from ..enemy import Enemy
from ...effect import Ritual
from ..intent import Intent, AttackIntent, CultistIncantationIntent

class Cultist(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(48, 54) if hp is None else hp)
        self.damage = 6
        self.incantation = 3

    def get_intent(self) -> Intent:
        if self.combat.turn == 0:
            return CultistIncantationIntent(self, [self.incantation])
        return AttackIntent(self, [self.damage])
