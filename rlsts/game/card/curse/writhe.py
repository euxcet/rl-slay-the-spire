from ..card import Card, CardRarity, CardType

class Writhe(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Curse,
            cost=0,
            target_types=[],
            is_unplayable=True,
            is_innate=True,
        )

    def finish(self, energy: int) -> None:
        ...
