from .buff import Buff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat
    from ...card import Card

class RageBuff(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def on_play_card(self, card: 'Card') -> None:
        from ...card.card import CardType
        if card.type == CardType.Attack:
            self.target.add_block(self.stack)
    
    def on_turn_end(self):
        self.stack = 0
