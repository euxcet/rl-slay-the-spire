from .debuff import Debuff
from ..buff.dexterity import Dexterity

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat
    from ...card.card import Card, CardType

class Entangled(Debuff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=1)

    def can_play_card(self, card: 'Card') -> bool:
        return card.type != CardType.Attack
