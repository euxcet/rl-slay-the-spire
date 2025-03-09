import random
from ..enemy import Enemy
from ...effect import Ritual
from ..intent import Intent, IntentType

class Cultist(Enemy):
    def __init__(self) -> None:
        super().__init__(hp=random.randint(48, 54))

    def get_intent(self) -> None:
        if self.combat.turn == 0:
            return Intent(IntentType.CULTIST_INCANTATION, [])
        else:
            return Intent(IntentType.ATTACK, [6])

    def perform(self) -> None:
        if self.combat.turn == 0:
            self.receive_effect(Ritual(self.combat, 3))
        else:
            self.attack(6)
