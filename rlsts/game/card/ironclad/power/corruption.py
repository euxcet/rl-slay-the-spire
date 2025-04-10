from ...card import Card, CardRarity, CardType
from ....effect.buff.corruption_buff import CorruptionBuff

class Corruption(Card):
    rarity = CardRarity.Rare
    type = CardType.Power
    def __init__(self, cost: int = 3) -> None:
        super().__init__(
            cost=cost,
            target_types=[],
        )

    def finish(self, energy: int) -> None:
        self.effect_character(CorruptionBuff(self.combat, 1))

class CorruptionPlus(Corruption):
    def __init__(self) -> None:
        super().__init__(cost=2)
