from ..card import Card, CardRarity, CardType
from ...effect.debuff.weak import Weak

class Pain(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Curse,
            cost=0,
            target_types=[],
            is_unplayable=True,
        )
        self.lose_hp = 1

    def on_other_play(self) -> None:
        self.character.lose_hp(self.lose_hp)

    def finish(self, energy: int) -> None:
        ...
