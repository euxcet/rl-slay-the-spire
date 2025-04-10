import random
from ...card import Card, CardRarity, CardType

class SwordBoomerang(Card):
    rarity = CardRarity.Common
    type = CardType.Attack
    def __init__(self, times: int = 3) -> None:
        super().__init__(
            cost=1,
            target_types=[],
        )
        self.damage = 3
        self.times = times

    def finish(self, energy: int) -> None:
        for _ in range(self.times):
            if len(self.enemies) > 0:
                self.attack(random.choice(self.enemies), self.damage)

class SwordBoomerangPlus(SwordBoomerang):
    def __init__(self) -> None:
        super().__init__(times=4)
