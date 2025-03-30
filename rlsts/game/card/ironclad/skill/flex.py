from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect import Strength, StrengthDown

class Flex(Card):
    def __init__(self, strength: int = 2) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Skill,
            cost=0,
            target_types=[],
        )
        self.strength = strength

    def finish(self, energy: int) -> None:
        self.effect_character(Strength(self.strength))
        self.effect_character(StrengthDown(self.strength))

class FlexPlus(Flex):
    def __init__(self) -> None:
        super().__init__(strength=4)
