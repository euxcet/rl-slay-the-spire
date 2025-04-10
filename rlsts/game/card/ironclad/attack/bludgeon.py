from copy import deepcopy
from ...card import Card, CardRarity, CardType, CardTargetType

class Bludgeon(Card):
    rarity = CardRarity.Rare
    type = CardType.Attack
    def __init__(self, damage: int = 32) -> None:
        super().__init__(
            cost=3,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)

class BludgeonPlus(Bludgeon):
    def __init__(self) -> None:
        super().__init__(damage=42)
