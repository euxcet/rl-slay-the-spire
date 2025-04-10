from ...card import Card, CardRarity, CardType, CardTargetType

class Clash(Card):
    rarity = CardRarity.Common
    type = CardType.Attack
    def __init__(self, damage: int = 14) -> None:
        super().__init__(
            cost=0,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)

    @property
    def is_unplayable(self) -> bool:
        for card in self.hand_pile:
            if card.type != CardType.Attack:
                return True
        return False

class ClashPlus(Clash):
    def __init__(self) -> None:
        super().__init__(damage=18)
