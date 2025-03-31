from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect.debuff.vulnerable import Vulnerable

class Dropkick(Card):
    def __init__(self, damage: int = 5) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Attack,
            cost=1,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        if enemy.has_effect(Vulnerable):
            self.character.energy += 1
        self.attack(enemy, self.damage)

class DropkickPlus(Dropkick):
    def __init__(self) -> None:
        super().__init__(damage=8)
