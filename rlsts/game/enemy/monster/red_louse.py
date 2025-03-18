import random
from ..enemy import Enemy
from ...effect import Strength, CurlUp
from ..intent import Intent, IntentType

class RedLouse(Enemy):
    def __init__(self) -> None:
        super().__init__(hp=random.randint(10, 15))
        self.bite_damage = random.randint(5, 7)
        self.grow = 3
        self.intents = []
        for i in range(self.MAX_INTENTS):
            if i >= 2 and self.intents[-1] == IntentType.LOUSE_GROW  and self.intents[-2] == IntentType.LOUSE_GROW:
                self.intents.append(IntentType.ATTACK)
            elif i >= 2 and self.intents[-1] == IntentType.ATTACK and self.intents[-2] == IntentType.ATTACK:
                self.intents.append(IntentType.LOUSE_GROW)
            elif random.randint(1, 4) == 1:
                self.intents.append(IntentType.LOUSE_GROW)
            else:
                self.intents.append(IntentType.ATTACK)

    def start_combat(self, combat) -> None:
        super().start_combat(combat)
        self.receive_effect(CurlUp(self.combat, random.randint(3, 7)))

    def get_intent(self) -> Intent:
        if self.intents[self.combat.turn % self.MAX_INTENTS] == IntentType.LOUSE_GROW:
            return Intent(IntentType.LOUSE_GROW, [self.grow])
        else:
            return Intent(IntentType.ATTACK, [self.estimate_attack(self.bite_damage), 1])

    def perform(self) -> None:
        if self.intents[self.combat.turn % self.MAX_INTENTS] == IntentType.LOUSE_GROW:
            self.receive_effect(Strength(self.combat, self.grow))
        else:
            self.attack(self.bite_damage)
