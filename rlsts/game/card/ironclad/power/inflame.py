from ...card import Card, CardRarity, CardType
from ....effect.buff.strength import Strength

class Inflame(Card):
    def __init__(self, buff: int = 2) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Power,
            cost=1,
            target_types=[],
        )
        self.buff = buff

    def finish(self, energy: int) -> None:
        self.effect_character(Strength(self.combat, self.buff))

class InflamePlus(Inflame):
    def __init__(self) -> None:
        super().__init__(buff=3)
