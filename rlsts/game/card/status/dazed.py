from ..card import Card, CardRarity, CardType, CardTargetType

class Dazed(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Status,
            cost=0,
            target_types=[],
            is_ethereal=True,
            is_unplayable=True,
        )

    def finish(self, energy: int) -> None:
        ...
