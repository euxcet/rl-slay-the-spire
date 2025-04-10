from ..card import Card, CardRarity, CardType, CardTargetType

class Slimed(Card):
    rarity = CardRarity.Common
    type = CardType.Status
    def __init__(self):
        super().__init__(
            cost=1,
            target_types=[],
            is_exhaust=True,
        )

    def finish(self, energy: int) -> None:
        ...
