from ..card import Card, CardRarity, CardType

class Clumsy(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Curse,
            cost=0,
            target_types=[],
            is_ethereal=True,
            is_unplayable=True,
        )

    def finish(self, energy: int) -> None:
        ...
