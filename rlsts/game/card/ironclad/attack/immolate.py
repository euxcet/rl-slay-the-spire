from ...card import Card, CardRarity, CardType, CardTargetType
from ...status.burn import Burn

class Immolate(Card):
    def __init__(self, damage: int = 21) -> None:
        super().__init__(
            rarity=CardRarity.Rare,
            type=CardType.Attack,
            cost=2,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        for enemy in self.combat.enemies.copy():
            self.attack(enemy, self.damage)
        Burn().to(self.combat).move_to(self.discard_pile)

class ImmolatePlus(Immolate):
    def __init__(self) -> None:
        super().__init__(damage=28)
