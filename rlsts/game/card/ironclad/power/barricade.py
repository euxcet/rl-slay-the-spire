from ...card import Card, CardRarity, CardType
from ....effect.buff.barricade_buff import BarricadeBuff

class Barricade(Card):
    rarity = CardRarity.Rare
    type = CardType.Power
    def __init__(self, cost: int = 3) -> None:
        super().__init__(
            cost=cost,
            target_types=[],
        )

    def finish(self, energy: int) -> None:
        self.effect_character(BarricadeBuff(self.combat, 1))

class BarricadePlus(Barricade):
    def __init__(self) -> None:
        super().__init__(cost=2)
