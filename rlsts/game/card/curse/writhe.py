from ..card import Card, CardRarity, CardType

class Writhe(Card):
    rarity = CardRarity.Common
    type = CardType.Curse
    def __init__(self):
        super().__init__(
            cost=0,
            target_types=[],
            is_unplayable=True,
            is_innate=True,
        )

    def finish(self, energy: int) -> None:
        ...
