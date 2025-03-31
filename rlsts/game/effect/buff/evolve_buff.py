from .buff import Buff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat
    from ...card import Card

class EvolveBuff(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def on_draw(self, card: 'Card') -> 'Card':
        from ...card.card import CardType
        if card.type == CardType.Status:
            self.combat.character.draw(self.stack)
