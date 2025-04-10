from ..card import Card, CardRarity, CardType

class AscendarsBane(Card):
    rarity = CardRarity.Common
    type = CardType.Curse
    def __init__(self):
        super().__init__(
            cost=0,
            target_types=[],
            is_ethereal=True,
            is_unplayable=True,
        )

    def can_remove(self) -> bool:
        return False

    def finish(self, energy: int) -> None:
        ...
