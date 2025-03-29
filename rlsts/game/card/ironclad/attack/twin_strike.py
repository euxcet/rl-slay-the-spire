from ...card import Card, CardRarity, CardType, CardTargetType

class TwinStrike(Card):
    def __init__(self, damage: int = 5) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Attack,
            cost=1,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)
        self.attack(enemy, self.damage)

class TwinStrikePlus(TwinStrike):
    def __init__(self) -> None:
        super().__init__(damage=7)
