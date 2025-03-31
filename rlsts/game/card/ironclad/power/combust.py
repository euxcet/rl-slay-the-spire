from ...card import Card, CardRarity, CardType
from ....effect.buff.combust_buff import CombustBuff

class Combust(Card):
    def __init__(self, damage: int = 5) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Power,
            cost=1,
            target_types=[],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        self.effect_character(CombustBuff(self.combat, 1, self.damage))

class CombustPlus(Combust):
    def __init__(self) -> None:
        super().__init__(damage=7)
