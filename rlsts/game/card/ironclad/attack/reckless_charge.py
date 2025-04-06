from ...card import Card, CardRarity, CardType, CardTargetType
from ...status.dazed import Dazed

class RecklessCharge(Card):
    def __init__(self, damage: int = 7) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Attack,
            cost=0,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)
        Dazed().to_combat(self.combat).move_to(self.draw_pile)

class RecklessChargePlus(RecklessCharge):
    def __init__(self) -> None:
        super().__init__(damage=10)
