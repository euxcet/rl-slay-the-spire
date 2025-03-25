from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect import Vulnerable

class Bash(Card):
    def __init__(self, damage: int = 6, debuff: int = 2) -> None:
        super().__init__(
            rarity=CardRarity.Starter,
            type=CardType.Attack,
            cost=2,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage
        self.debuff = debuff

    def finish(self) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)
        self.effect_enemy(enemy, Vulnerable(self.combat, 2))

class BashPlus(Bash):
    def __init__(self) -> None:
        super().__init__(damage=10, debuff=3)
