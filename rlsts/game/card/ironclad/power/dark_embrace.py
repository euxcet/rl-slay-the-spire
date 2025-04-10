from ...card import Card, CardRarity, CardType
from ....effect.buff.dark_embrace_buff import DarkEmbraceBuff

class DarkEmbrace(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Power
    def __init__(self, cost: int = 2) -> None:
        super().__init__(
            cost=cost,
            target_types=[],
        )

    def finish(self, energy: int) -> None:
        self.effect_character(DarkEmbraceBuff(self.combat, 1))

class DarkEmbracePlus(DarkEmbrace):
    def __init__(self) -> None:
        super().__init__(cost=1)

