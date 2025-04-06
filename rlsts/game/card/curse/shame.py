from ..card import Card, CardRarity, CardType
from ...effect.debuff.frail import Frail

class Shame(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Curse,
            cost=0,
            target_types=[],
            is_unplayable=True,
        )
        self.weak = 1

    def on_turn_end(self) -> None:
        self.character.receive_effect(Frail(self.combat, self.weak))

    def finish(self, energy: int) -> None:
        ...
