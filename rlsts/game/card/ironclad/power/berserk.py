from ...card import Card, CardRarity, CardType
from ....effect.buff.berserk_buff import BerserkBuff
from ....effect.debuff.vulnerable import Vulnerable

class Berserk(Card):
    rarity = CardRarity.Rare
    type = CardType.Power
    def __init__(self, debuff: int = 2) -> None:
        super().__init__(
            cost=0,
            target_types=[],
        )
        self.debuff = debuff

    def finish(self, energy: int) -> None:
        self.effect_character(Vulnerable(self.combat, self.debuff))
        self.effect_character(BerserkBuff(self.combat, 1))

class BerserkPlus(Berserk):
    def __init__(self) -> None:
        super().__init__(debuff=1)
