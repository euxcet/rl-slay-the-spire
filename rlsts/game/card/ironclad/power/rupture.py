from ...card import Card, CardRarity, CardType
from ....effect.buff.rupture_buff import RuptureBuff

class Rupture(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Power
    def __init__(self, buff: int = 1) -> None:
        super().__init__(
            cost=1,
            target_types=[],
        )
        self.buff = buff

    def finish(self, energy: int) -> None:
        self.effect_character(RuptureBuff(self.combat, self.buff))

class RupturePlus(Rupture):
    def __init__(self) -> None:
        super().__init__(buff=2)
