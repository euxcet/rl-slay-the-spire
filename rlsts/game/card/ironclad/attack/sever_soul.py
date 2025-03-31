from ...card import Card, CardRarity, CardType, CardTargetType

class SeverSoul(Card):
    def __init__(self, damage: int = 16) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Attack,
            cost=2,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)
        for card in self.hand_pile.cards.copy():
            if card.type != CardType.Attack:
                card.exhaust()

class SeverSoulPlus(SeverSoul):
    def __init__(self) -> None:
        super().__init__(damage=22)
