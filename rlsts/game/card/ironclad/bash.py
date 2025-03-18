from ..card import Card, CardRarity, CardType, CardTargetType
from ...effect import Vulnerable

class Bash(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Starter,
            type=CardType.Attack,
            cost=2,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = 8
        self.debuff = 2

    def finish(self) -> None:
        self.attack(self.targets[0], self.damage)
        self.effect_enemy(self.targets[0], Vulnerable(self.combat, 2))