from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect.buff.strength import Strength

class LimitBreak(Card):
    def __init__(self, is_exhaust: bool = True) -> None:
        super().__init__(
            rarity=CardRarity.Rare,
            type=CardType.Skill,
            cost=1,
            target_types=[],
            is_exhaust=is_exhaust,
       )

    def finish(self, energy: int) -> None:
        if (effect := self.character.get_effect(Strength)) != None:
            effect.set_stack(effect.stack * 2)

class LimitBreakPlus(LimitBreak):
    def __init__(self) -> None:
        super().__init__(is_exhaust=False)
