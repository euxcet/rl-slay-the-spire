from ..card import Card, CardRarity, CardType, CardTargetType

class Strike(Card):
    def __init__(self) -> None:
        super().__init__(
            rarity=CardRarity.Starter,
            type=CardType.Attack,
            cost=1,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = 6

    def finish(self) -> None:
        self.attack(self.get_enemy(self.targets[0]), self.damage)