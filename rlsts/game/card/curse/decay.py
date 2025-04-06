from ..card import Card, CardRarity, CardType

class Decay(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Curse,
            cost=0,
            target_types=[],
            is_unplayable=True,
        )
        self.damage = 2

    def on_turn_end(self) -> None:
        self.character.receive_damage(self.damage, self, do_effect=False)

    def finish(self, energy: int) -> None:
        ...
