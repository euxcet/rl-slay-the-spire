from ...card import Card, CardRarity, CardType
from ....effect import Vulnerable

class Thunderclap(Card):
    def __init__(self, damage: int = 4) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Attack,
            cost=1,
            target_types=[],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        for enemy in self.combat.enemies:
            self.attack(enemy, self.damage)
            self.effect_enemy(enemy, Vulnerable(self.combat, 1))

class ThunderclapPlus(Thunderclap):
    def __init__(self) -> None:
        super().__init__(damage=7)
