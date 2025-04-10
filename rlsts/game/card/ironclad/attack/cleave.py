from ...card import Card, CardRarity, CardType, CardTargetType

class Cleave(Card):
    rarity = CardRarity.Common
    type = CardType.Attack
    def __init__(self, damage: int = 8) -> None:
        super().__init__(
            cost=1,
            target_types=[],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        for enemy in self.enemies.copy():
            self.attack(enemy, self.damage)

class CleavePlus(Cleave):
    def __init__(self) -> None:
        super().__init__(damage=8)
