from .buff import Buff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat

class SharpHide(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)
    
    def on_play_card(self, card):
        from ...card.card import CardType
        if card.type == CardType.Attack:
            self.combat.character.receive_damage(self.stack, self, do_effect=False)