from ...card import Card, CardRarity, CardType, CardTargetType
from ...status.wound import Wound

class WildStrike(Card):
    def __init__(self, damage: int = 12) -> None:
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
        self.draw_pile.insert(Wound().to_combat(self.combat))

class WildStrikePlus(WildStrike):
    def __init__(self) -> None:
        super().__init__(damage=17)
