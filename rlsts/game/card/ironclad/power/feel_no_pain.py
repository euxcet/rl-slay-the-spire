from ...card import Card, CardRarity, CardType
from ....effect.buff.feel_no_pain_buff import FeelNoPainBuff

class FeelNoPain(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Power
    def __init__(self, buff=3) -> None:
        super().__init__(
            cost=1,
            target_types=[],
        )
        self.buff = buff

    def finish(self, energy: int) -> None:
        self.effect_character(FeelNoPainBuff(self.combat, self.buff))

class FeelNoPainPlus(FeelNoPain):
    def __init__(self) -> None:
        super().__init__(buff=4)
