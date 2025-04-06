from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from ..target import Target
from ..card.deck import Deck
from ..card.pile import Pile
from ..effect import Effect
if TYPE_CHECKING:
    from ..enemy import Enemy
    from ..combat.combat import Combat
    from ..card import Card

class Character(Target):
    def __init__(
        self,
        hp: int,
        max_hp: int,
        gold: int,
        deck: Deck,
        orientation: bool = False, # 0: right  1: left
    ) -> None:
        super().__init__(hp=hp, max_hp=max_hp)
        self.gold = gold
        self.deck = deck
        for card in self.deck.cards:
            card.set_character(self)
        self.orientation = orientation
        self.draw_pile: Pile = None
        self.hand_pile: Pile = None
        self.exhaust_pile: Pile = None
        self.discard_pile: Pile = None
        self.energy: int = 0
        self.playing_card = None
        self.card_played_turn = 0

    def is_in_combat(self) -> bool:
        return self.combat is not None

    # TODO: move to Card
    def attack(self, enemy: 'Enemy', damage: int) -> int:
        for effect in self.effects:
            effect.on_attack(damage)
        return enemy.receive_damage(self.prepare_attack(damage), self)

    def start_combat(self, combat: 'Combat') -> None:
        super().start_combat(combat)
        self.orientation = 0
        self.draw_pile = Pile(cards=self.deck.cards, combat=combat)
        self.draw_pile.shuffle()
        self.hand_pile = Pile()
        self.exhaust_pile = Pile()
        self.discard_pile = Pile()

    def start_turn(self) -> None:
        super().start_turn()
        self.card_played_turn = 0
        num_draw = self.num_turn_draw()
        innate_cards = [card for card in self.draw_pile if card.is_innate]
        for card in innate_cards:
            self.draw_to_hand(card)
        num_draw = max(num_draw - len(innate_cards), 0)
        self.draw(num_draw)
        self.energy += self.num_turn_energy()

    def end_turn(self) -> None:
        super().end_turn()
        self.energy = 0
        for card in self.hand_pile:
            card.on_turn_end()
        for card in self.hand_pile.cards.copy():
            if card.is_ethereal:
                card.exhaust()
            else:
                card.discard(is_turn_end=True)

    def die(self) -> None:
        super().die()
        self.combat.is_over = True
        self.combat.is_game_over = True

    def draw(self, num: int) -> None:
        for effect in self.effects:
            num = effect.modify_draw(num)
        for _ in range(num):
            if len(self.draw_pile) == 0:
                for card in self.discard_pile.cards.copy():
                    card.move_to(self.draw_pile)
                self.draw_pile.shuffle()
            if len(self.draw_pile) > 0:
                self.draw_to_hand(self.draw_pile.draw())

    def draw_to_hand(self, card: 'Card') -> None:
        if len(self.hand_pile) == self.combat.MAX_NUM_HAND_CARDS:
            # TODO: trigger on_draw?
            card.move_to(self.discard_pile)
        else:
            card.on_draw()
            card.move_to(self.hand_pile)

    def num_turn_draw(self) -> int:
        num = 5
        for effect in self.effects:
            num = effect.modify_turn_draw(num)
        return num

    def num_turn_energy(self) -> int:
        num = 3
        for effect in self.effects:
            num = effect.modify_turn_energy(num)
        return num

    def is_card_playing(self) -> bool:
        return self.playing_card is not None
    
    def has_playable_card(self) -> bool:
        for card in self.hand_pile:
            if card.cost <= self.energy:
                return True
        return False

    def can_play_card(self, card_id: int) -> bool:
        # for Normality(curse)
        for card in self.hand_pile.cards:
            if not card.can_play_card(self.card_played_turn):
                return False
        return card_id >= 0 and card_id < len(self.hand_pile) and \
                not self.hand_pile.cards[card_id].is_unplayable and \
                (self.hand_pile.cards[card_id].cost is None or self.energy >= self.hand_pile.cards[card_id].cost)

    def play_card(self, card_index: int) -> None:
        if not self.can_play_card(card_index):
            print("punish")
            raise Exception
            return
        self.card_played_turn += 1
        self.playing_card = self.hand_pile.draw_index(card_index).move_to(None)
        used_energy = self.energy
        if self.playing_card.cost is None:
            self.energy = 0
        else:
            self.energy -= self.playing_card.cost
        if self.playing_card.play(used_energy):
            self.playing_card = None

    def choose_in_card(self, card_id: int) -> None:
        assert self.playing_card is not None
        if self.playing_card.choose(card_id):
            self.playing_card = None

    def remove_gold(self, g: int) -> int:
        g = min(g, self.gold)
        self.gold -= g
        return g

    def add_cards(self, cards: list['Card']) -> None:
        self.deck.add_cards(cards)

    def receive_gold(self, gold: int) -> int:
        self.gold += gold
        return self.gold
    
    def lose_gold(self, gold: int) -> int:
        self.gold = max(0, self.gold - gold)
        return self.gold