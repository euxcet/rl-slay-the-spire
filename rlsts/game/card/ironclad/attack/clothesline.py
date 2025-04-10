from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect.debuff.weak import Weak

class Clothesline(Card):
    rarity = CardRarity.Common
    type = CardType.Attack
    def __init__(self, damage: int = 12, debuff: int = 2) -> None:
        super().__init__(
            cost=2,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage
        self.debuff = debuff

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)
        self.effect_enemy(enemy, Weak(self.combat, self.debuff))

class ClotheslinePlus(Clothesline):
    def __init__(self) -> None:
        super().__init__(damage=14, debuff=3)
