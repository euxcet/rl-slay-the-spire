from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from ..card.deck import Deck
from ..card.pile import Pile
if TYPE_CHECKING:
    from ..combat.combat import Combat

class Character(ABC):
    def __init__(
        self,
        hp: int,
        gold: int,
        deck: Deck = Deck(),
        orientation: bool = False, # 0: right  1: left
    ) -> None:
        self.hp = hp
        self.gold = gold
        self.deck = deck
        self.orientation = orientation
        self.combat = None
        self.draw_pile: Pile = None
        self.hand_pile: Pile = None
        self.exhaust_pile: Pile = None
        self.discard_pile: Pile = None
        self.energy: int = 0
        self.played_card = None

    def is_in_combat(self) -> bool:
        return self.combat is not None

    def start_combat(self, combat: Combat) -> None:
        self.combat = combat
        self.orientation = 0
        self.draw_pile = Pile(deck=self.deck)
        self.draw_pile.shuffle()
        self.exhaust_pile = Pile()
        self.discard_pile = Pile()

    def start_turn(self) -> None:
        assert self.is_in_combat()
        self.draw(self.num_turn_draw())
        self.energy += self.num_turn_energy()

    def end_turn(self) -> None:
        for i in range(len(self.hand_pile)):
            card = self.hand_pile.draw()
            card.on_turn_discard()
            self.discard_pile.insert(card)

    def draw(self, num: int) -> None:
        for i in range(num):
            if len(self.draw_pile) == 0:
                for j in range(len(self.discard_pile)):
                    card = self.discard_pile.draw()
                    self.draw_pile.insert(card)
                self.draw_pile.shuffle()
            card = self.draw_pile.draw()
            card.on_draw()
            self.hand_pile.insert(card)

    def num_turn_draw(self) -> int:
        return 5

    def num_turn_energy(self) -> int:
        return 3

    def is_card_played(self) -> bool:
        return self.played_card is not None

    def has_playable_card(self) -> bool:
        for card in self.hand_pile:
            if card.energy <= self.energy:
                return True
        return False

    def play_card(self, card_id: int) -> None:
        self.played_card = self.hand_pile.draw_by_id(card_id)
        if self.played_card is None or not self.played_card.playable or self.played_card.energy > self.energy:
            # TODO: punish
            ...
        else:
            self.played_card.play()

    def choose_in_card(self, card_id: int) -> None:
        assert self.played_card is not None
        self.played_card.choose(card_id)

