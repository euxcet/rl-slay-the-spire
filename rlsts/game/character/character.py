from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from ..card.deck import Deck
from ..card.pile import Pile
from ..effect import Effect
if TYPE_CHECKING:
    from ..combat.combat import Combat

class Character(ABC):
    def __init__(
        self,
        hp: int,
        gold: int,
        deck: Deck,
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
        self.playing_card = None
        self.block: int = 0
        self.effects: list[Effect] = []

    def is_in_combat(self) -> bool:
        return self.combat is not None

    def start_combat(self, combat: 'Combat') -> None:
        self.combat = combat
        self.orientation = 0
        self.draw_pile = Pile(deck=self.deck, combat=combat)
        self.draw_pile.shuffle()
        self.hand_pile = Pile()
        self.exhaust_pile = Pile()
        self.discard_pile = Pile()
        self.block = 0
        self.effects.clear()

    def start_turn(self) -> None:
        assert self.is_in_combat()
        self.draw(self.num_turn_draw())
        self.energy += self.num_turn_energy()
        self.block = 0

    def end_turn(self) -> None:
        self.energy = 0
        for effect in self.effects:
            effect.stack -= effect.decrease_per_turn
        self.effects = [effect for effect in self.effects if effect.stack > 0]
        for i in range(len(self.hand_pile)):
            card = self.hand_pile.draw()
            card.on_turn_discard()
            self.discard_pile.insert(card)

    def die(self) -> None:
        self.hp = 0
        self.combat.is_over = True
        self.combat.is_game_over = True

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

    def is_card_playing(self) -> bool:
        return self.playing_card is not None
    
    def has_playable_card(self) -> bool:
        for card in self.hand_pile:
            if card.energy <= self.energy:
                return True
        return False

    def can_play_card(self, card_id: int) -> bool:
        return card_id >= 0 and card_id < len(self.hand_pile) and self.energy >= self.hand_pile.cards[card_id].energy

    def play_card(self, card_index: int) -> None:
        if not self.can_play_card(card_index):
            print("punish")
            return
        self.playing_card = self.hand_pile.draw_index(card_index)
        self.energy -= self.playing_card.energy
        if self.playing_card.play():
            self.playing_card = None

    def choose_in_card(self, card_id: int) -> None:
        assert self.playing_card is not None
        if self.playing_card.choose(card_id):
            self.playing_card = None

    def prepare_attack(self, damage: int) -> int:
        for effect in self.effects:
            damage = effect.modify_damage(damage)
        return damage

    def add_block(self, block: int) -> int:
        for effect in self.effects:
            block = effect.modify_block(block)
        self.block += block

    def receive_effect(self, new_effect: Effect) -> None:
        new_effect.target_enemy = None
        for effect in self.effects:
            if type(effect) == type(new_effect):
                effect.stack += new_effect.stack
                return
        self.effects.append(new_effect)

    def estimate_damage(self, damage: int) -> int:
        for effect in self.effects:
            damage = effect.modify_received_damage(damage)
        # TODO: relics ...
        return damage
    
    def receive_damage(self, damage: int) -> int:
        damage = self.estimate_damage(damage)
        if damage <= self.block:
            self.block -= damage
            return 0
        damage -= self.block
        self.block = 0
        if damage >= self.hp:
            hp = self.hp
            self.die()
            return hp
        self.hp -= damage
        return damage