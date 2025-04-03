import random
from ..enemy import Enemy
from ..intent import Intent, AttackIntent, ScrapeIntent, GremlinNobBellowIntent

class GremlinNob(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(82, 86) if hp is None else hp)
        self.bellow = 2
        self.damage = 14
        self.scrape_damage = 6
        self.scrape_debuff = 2

    def get_intent(self) -> Intent:
        if self.combat.turn == 0:
            return GremlinNobBellowIntent(self, [self.bellow])
        return self.choose_intent([
            (AttackIntent(self, [self.damage], is_multi=False), 0.67, 3),
            (ScrapeIntent(self, [self.scrape_damage, self.scrape_debuff]), 0.33, 100),
        ])
