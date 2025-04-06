from ..card import Card, CardRarity, CardType
from ...effect.debuff.weak import Weak

class Necronomicurse(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Curse,
            cost=0,
            target_types=[],
            is_unplayable=True,
        )

    def finish(self, energy: int) -> None:
        ...
