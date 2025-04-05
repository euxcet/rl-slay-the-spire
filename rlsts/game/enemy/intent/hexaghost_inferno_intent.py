from .attack_intent import AttackIntent
from typing import TYPE_CHECKING
from ...card.status.burn import Burn, BurnPlus
if TYPE_CHECKING:
    from .. import Enemy

class HexaghostInfernoIntent(AttackIntent):
    def __init__(self, enemy: 'Enemy', values: list[int]) -> None:
        super().__init__(enemy=enemy, values=values, is_multi=True)
        
    def perform(self) -> None:
        super().perform()
        self.enemy.upgrade_burn = True
        self.character.draw_pile.cards = [
            BurnPlus().to(self.combat).to_pile(self.character.draw_pile) if isinstance(card, Burn) else card
            for card in self.character.draw_pile.cards
        ]
        self.character.discard_pile.cards = [
            BurnPlus().to(self.combat).to_pile(self.character.discard_pile) if isinstance(card, Burn) else card
            for card in self.character.discard_pile.cards
        ]
        self.character.exhaust_pile.cards = [
            BurnPlus().to(self.combat).to_pile(self.character.exhaust_pile) if isinstance(card, Burn) else card
            for card in self.character.exhaust_pile.cards
        ]
        self.character.hand_pile.cards = [
            BurnPlus().to(self.combat).to_pile(self.character.hand_pile) if isinstance(card, Burn) else card
            for card in self.character.hand_pile.cards
        ]
        for _ in range(self.values[2]):
            if self.enemy.upgrade_burn:
                BurnPlus().to(self.combat).move_to(self.character.discard_pile, is_random=True)
            else:
                Burn().to(self.combat).move_to(self.character.discard_pile, is_random=True)