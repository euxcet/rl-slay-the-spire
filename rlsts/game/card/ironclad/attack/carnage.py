# TODO
from copy import deepcopy
from ...card import Card, CardRarity, CardType, CardTargetType

class Carnage(Card):
    def __init__(self, damage: int = 20) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Attack,
            cost=2,
            target_types=[CardTargetType.Enemy],
            is_ethereal=True,
        )
        self.damage = damage

    def finish(self) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)

class CarnagePlus(Carnage):
    def __init__(self) -> None:
        super().__init__(damage=28)
