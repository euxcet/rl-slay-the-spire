from ..card import Card, CardRarity, CardType
from ...effect.debuff.weak import Weak

class Regret(Card):
    rarity = CardRarity.Common
    type = CardType.Curse
    def __init__(self):
        super().__init__(
            cost=0,
            target_types=[],
            is_unplayable=True,
        )

    def on_turn_end(self) -> None:
        self.character.lose_hp(len(self.draw_pile))

    def finish(self, energy: int) -> None:
        ...
