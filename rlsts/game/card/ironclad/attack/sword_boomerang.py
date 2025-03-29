import random
from ...card import Card, CardRarity, CardType

class SwordBoomerang(Card):
    def __init__(self, times: int = 3) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Attack,
            cost=1,
            target_types=[],
        )
        self.damage = 3
        self.times = times

    def finish(self, energy: int) -> None:
        for _ in range(self.times):
            if len(self.combat.enemies) > 0:
                self.attack(random.choice(self.combat.enemies), self.damage)

class SwordBoomerangPlus(SwordBoomerang):
    def __init__(self) -> None:
        super().__init__(times=4)
