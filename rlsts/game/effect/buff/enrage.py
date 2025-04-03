from .buff import Buff
from .strength import Strength

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat
    from ...card import Card

class Enrage(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def on_play_card(self, card: 'Card') -> None:
        from ...card.card import CardType
        if card.type == CardType.Skill:
            self.target.receive_effect(Strength(self.combat, self.stack))
    