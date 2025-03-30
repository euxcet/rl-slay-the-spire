import random
from .debuff import Debuff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...combat import Combat
    from ...card import Card

class Confused(Debuff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=1)
    
    def on_draw(self, card: 'Card') -> 'Card':
        card.cost = random.randint(0, 3)
        return card
