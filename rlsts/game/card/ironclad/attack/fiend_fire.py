from ...card import Card, CardRarity, CardType, CardTargetType

class FiendFire(Card):
    def __init__(self, damage: int = 7) -> None:
        super().__init__(
            rarity=CardRarity.Rare,
            type=CardType.Attack,
            cost=2,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        num = len(self.hand_pile)
        for card in self.hand_pile:
            card.exhaust()
        for _ in range(num):
            self.attack(enemy, self.damage)

class FiendFirePlus(FiendFire):
    def __init__(self) -> None:
        super().__init__(damage=10)
