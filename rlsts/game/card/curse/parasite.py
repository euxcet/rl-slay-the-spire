from ..card import Card, CardRarity, CardType
from ...effect.debuff.weak import Weak

class Parasite(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Curse,
            cost=0,
            target_types=[],
            is_unplayable=True,
        )
        self.lose_max_hp = 3

    def on_remove(self):
        self.character.max_hp -= self.lose_max_hp

    def finish(self, energy: int) -> None:
        ...
