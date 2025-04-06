from copy import deepcopy
from ...card import Card, CardRarity, CardType, CardTargetType

class Anger(Card):
    def __init__(self, damage: int = 6) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Attack,
            cost=0,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)
        deepcopy(self).to_combat(self.combat).move_to(self.discard_pile)

class AngerPlus(Anger):
    def __init__(self) -> None:
        super().__init__(damage=8)
