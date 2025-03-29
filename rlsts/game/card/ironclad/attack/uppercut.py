from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect import Vulnerable, Weak

class Uppercut(Card):
    def __init__(self, weak: int = 1, vulnerable: int = 1) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Attack,
            cost=2,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = 13
        self.weak = weak
        self.vulnerable = vulnerable

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)
        self.effect_enemy(enemy, Weak(self.combat, self.weak))
        self.effect_enemy(enemy, Vulnerable(self.combat, self.vulnerable))

class UppercutPlus(Uppercut):
    def __init__(self) -> None:
        super().__init__(weak=2, vulnerable=2)
