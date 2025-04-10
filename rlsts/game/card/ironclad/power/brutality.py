from ...card import Card, CardRarity, CardType
from ....effect.buff.brutality_buff import BrutalityBuff

class Brutality(Card):
    rarity = CardRarity.Rare
    type = CardType.Power
    def __init__(self) -> None:
        super().__init__(
            cost=0,
            target_types=[],
        )

    def finish(self, energy: int) -> None:
        self.effect_character(BrutalityBuff(self.combat, 1))

# TODO: innate
class BrutalityPlus(Brutality):
    def __init__(self) -> None:
        super().__init__()
