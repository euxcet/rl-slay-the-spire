from ..card import Card, CardRarity, CardType
from ...effect.debuff.weak import Weak

class Doubt(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Curse,
            cost=0,
            target_types=[],
            is_unplayable=True,
        )
        self.weak = 1

    def on_turn_discard(self):
        self.character.receive_effect(Weak(self.combat, self.weak))

    def finish(self, energy: int) -> None:
        ...
