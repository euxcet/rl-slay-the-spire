from ..card import Card, CardRarity, CardType

class Decay(Card):
    rarity = CardRarity.Common
    type = CardType.Curse
    def __init__(self):
        super().__init__(
            cost=0,
            target_types=[],
            is_unplayable=True,
        )
        self.damage = 2

    def on_turn_end(self) -> None:
        self.character.receive_damage(self.damage, self, do_effect=False)

    def finish(self, energy: int) -> None:
        ...
