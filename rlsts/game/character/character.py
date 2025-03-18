from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from ..target import Target
from ..card.deck import Deck
from ..card.pile import Pile
from ..effect import Effect
if TYPE_CHECKING:
    from ..combat.combat import Combat

class Character(Target):
    def __init__(
        self,
        hp: int,
        gold: int,
        deck: Deck,
        orientation: bool = False, # 0: right  1: left
    ) -> None:
        super().__init__(hp)
        self.gold = gold
        self.deck = deck
        self.orientation = orientation
        self.draw_pile: Pile = None
        self.hand_pile: Pile = None
        self.exhaust_pile: Pile = None
        self.discard_pile: Pile = None
        self.energy: int = 0
        self.playing_card = None

    def is_in_combat(self) -> bool:
        return self.combat is not None

    def attack(self, target: int, damage: int) -> int:
        for effect in self.effects:
            effect.on_attack()
        return self.combat.enemies[target].receive_damage(self.prepare_attack(damage))

    def start_combat(self, combat: 'Combat') -> None:
        super().start_combat(combat)
        self.orientation = 0
        self.draw_pile = Pile(deck=self.deck, combat=combat)
        self.draw_pile.shuffle()
        self.hand_pile = Pile()
        self.exhaust_pile = Pile()
        self.discard_pile = Pile()

    def start_turn(self) -> None:
        super().start_turn()
        self.draw(self.num_turn_draw())
        self.energy += self.num_turn_energy()

    def end_turn(self) -> None:
        super().end_turn()
        self.energy = 0
        for _ in range(len(self.hand_pile)):
            card = self.hand_pile.draw()
            card.on_turn_discard()
            self.discard_pile.insert(card)

    def die(self) -> None:
        super().die()
        self.combat.is_over = True
        self.combat.is_game_over = True

    def draw(self, num: int) -> None:
        for _ in range(num):
            # print(f'Draw draw_pile {len(self.draw_pile)}  discard_pile {len(self.discard_pile)}  exhaust_pile {len(self.exhaust_pile)}')
            if len(self.draw_pile) == 0:
                for __ in range(len(self.discard_pile)):
                    card = self.discard_pile.draw()
                    self.draw_pile.insert(card)
                self.draw_pile.shuffle()
            if len(self.draw_pile) > 0:
                card = self.draw_pile.draw()
                card.on_draw()
                self.hand_pile.insert(card)

    def num_turn_draw(self) -> int:
        return 5

    def num_turn_energy(self) -> int:
        return 3

    def is_card_playing(self) -> bool:
        return self.playing_card is not None
    
    def has_playable_card(self) -> bool:
        for card in self.hand_pile:
            if card.energy <= self.energy:
                return True
        return False

    def can_play_card(self, card_id: int) -> bool:
        return card_id >= 0 and card_id < len(self.hand_pile) and self.energy >= self.hand_pile.cards[card_id].cost

    def play_card(self, card_index: int) -> None:
        if not self.can_play_card(card_index):
            print("punish")
            return
        self.playing_card = self.hand_pile.draw_index(card_index)
        self.energy -= self.playing_card.cost
        if self.playing_card.play():
            self.playing_card = None

    def choose_in_card(self, card_id: int) -> None:
        assert self.playing_card is not None
        if self.playing_card.choose(card_id):
            self.playing_card = None

    def remove_gold(self, g: int) -> int:
        g = min(g, self.gold)
        self.gold -= g
        return g
