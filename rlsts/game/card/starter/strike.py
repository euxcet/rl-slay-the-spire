from ..card import Card, CardRarity, CardType, CardTargetType

class Strike(Card):
    def __init__(self, damage: int = 6) -> None:
        super().__init__(
            rarity=CardRarity.Starter,
            type=CardType.Attack,
            cost=1,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        self.attack(self.get_enemy(self.targets[0]), self.damage)

class StrikePlus(Strike):
    def __init__(self) -> None:
        super().__init__(damage=9)