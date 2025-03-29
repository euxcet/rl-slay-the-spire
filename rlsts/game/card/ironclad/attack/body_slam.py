from copy import deepcopy
from ...card import Card, CardRarity, CardType, CardTargetType

class BodySlam(Card):
    def __init__(self, cost: int = 1) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Attack,
            cost=cost,
            target_types=[CardTargetType.Enemy],
        )

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.combat.character.block)

class BodySlamPlus(BodySlam):
    def __init__(self) -> None:
        super().__init__(cost=0)
