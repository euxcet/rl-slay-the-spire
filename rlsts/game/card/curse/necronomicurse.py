from ..card import Card, CardRarity, CardType
from ...effect.debuff.weak import Weak

class Necronomicurse(Card):
    rarity = CardRarity.Common
    type = CardType.Curse
    def __init__(self):
        super().__init__(
            cost=0,
            target_types=[],
            is_unplayable=True,
        )

    def finish(self, energy: int) -> None:
        ...
