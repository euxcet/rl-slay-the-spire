from ..card import Card, CardRarity, CardType, CardTargetType

class Strike(Card):
    def __init__(self) -> None:
        super().__init__(
            rarity=CardRarity.Starter,
            type=CardType.Attack,
            energy=1,
            playable=True,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = 6

    def finish(self) -> None:
        self.attack(self.targets[0], self.damage)