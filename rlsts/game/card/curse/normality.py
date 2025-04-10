from ..card import Card, CardRarity, CardType
from ...effect.debuff.weak import Weak

class Normality(Card):
    rarity = CardRarity.Common
    type = CardType.Curse
    def __init__(self):
        super().__init__(
            cost=0,
            target_types=[],
            is_unplayable=True,
        )

    def can_play_card(self, card_played_turn: int) -> bool:
        return card_played_turn < 3

    def finish(self, energy: int) -> None:
        ...
