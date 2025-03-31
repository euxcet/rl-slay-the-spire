from .buff import Buff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat
    from ...card import Card

class CorruptionBuff(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def modify_card_cost(self, card: 'Card', cost: int) -> int:
        from ...card.card import CardType
        if card.type == CardType.Skill:
            return 0
        return cost

    def on_play_card(self, card: 'Card') -> None:
        from ...card.card import CardType
        if card.type == CardType.Skill:
            card.exhaust()