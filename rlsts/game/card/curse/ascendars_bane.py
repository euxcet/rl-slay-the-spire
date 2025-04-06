from ..card import Card, CardRarity, CardType

class AscendarsBane(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Curse,
            cost=0,
            target_types=[],
            is_ethereal=True,
            is_unplayable=True,
        )

    def can_remove(self) -> bool:
        return False

    def finish(self, energy: int) -> None:
        ...
