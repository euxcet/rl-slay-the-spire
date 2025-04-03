from ..card import Card, CardRarity, CardType, CardTargetType

class Void(Card):
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

    def on_draw(self):
        self.character.energy = max(0, self.character.energy - 1)
