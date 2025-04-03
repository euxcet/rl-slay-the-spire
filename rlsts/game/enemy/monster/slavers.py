import random
from ..enemy import Enemy
from ..intent import Intent, AttackIntent, SmashIntent, RedSlaverEntangleIntent, ScrapeIntent

class BlueSlaver(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(46, 50) if hp is None else hp)
        self.damage = 12
        self.smash_damage = 7
        self.smash_weak = 1

    def get_intent(self) -> Intent:
        return self.choose_intent([
            (AttackIntent(self, [self.damage], is_multi=False), 0.6, 3),
            (SmashIntent(self, [self.smash_damage, self.smash_weak]), 0.4, 3),
        ])

class RedSlaver(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(46, 50) if hp is None else hp)
        self.damage = 13
        self.scrape_damage = 8
        self.scrape_vulnerable = 1
        self.entangled = False

    def get_intent(self) -> Intent:
        if self.combat.turn == 0:
            return AttackIntent(self, [self.damage], is_multi=False)
        self.entangled = self.entangled or type(self.intent_history[-1]) is RedSlaverEntangleIntent
        if self.entangled:
            return self.choose_intent([
                (AttackIntent(self, [self.damage], is_multi=False), 0.45, 3),
                (ScrapeIntent(self, [self.scrape_damage, self.scrape_vulnerable]), 0.55, 3),
            ])
        else:
            if self.intent_pool.peek(self.combat.turn) < 0.25:
                return RedSlaverEntangleIntent(self, [1])
            else:
                if self.combat.turn % 3 == 0:
                    return AttackIntent(self, [self.damage], is_multi=False)
                else:
                    return ScrapeIntent(self, [self.scrape_damage, self.scrape_vulnerable])
