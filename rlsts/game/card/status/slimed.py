from ..card import Card, CardRarity, CardType, CardTargetType

class Slimed(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Status,
            cost=1,
            target_types=[],
            is_exhaust=True,
        )

    def finish(self, energy: int) -> None:
        ...
