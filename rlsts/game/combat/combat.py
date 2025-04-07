import numpy as np
from ..observation.combat_observation import CombatObservation
from ..character import Character
from ..enemy import Enemy
from copy import deepcopy

class Combat():
    MAX_NUM_HAND_CARDS = 10
    MAX_ACTION = 15

    def __init__(
        self,
        character: Character,
        enemies_type: list[type],
    ) -> None:
        self.character = character
        self.enemies_type = enemies_type

    def update_enemies(self) -> None:
        for position, enemy in enumerate(self.enemies):
            enemy.position = position
        if len(self.enemies) == 0:
            self.is_over = True

    def add_enemy(self, position: int, enemy: Enemy) -> None:
        self.enemies.insert(position, enemy)
        self.update_enemies()

    def remove_enemy(self, enemy: Enemy) -> None:
        self.enemies.remove(enemy)
        self.update_enemies()

    def check_enemies(self) -> None:
        self.enemies = [enemy for enemy in self.enemies if enemy.hp > 0]
        self.update_enemies()

    @staticmethod
    def create_enemy(t: type | tuple) -> Enemy:
        if isinstance(t, type):
            return t()
        else:
            return t[0](**t[1])

    def reset(self) -> CombatObservation:
        self.turn = 0
        self.is_over = False
        self.is_game_over = False
        self.enemies: list[Enemy] = [self.create_enemy(enemy) for enemy in self.enemies_type]
        self.enemies.sort()
        for enemy in self.enemies:
            enemy.start_combat(self)
            enemy.hp = 1
        self.character.start_combat(self)
        self.character.start_turn()
        self.update_enemies()
        return self.observe()

    def get_action_mask(self) -> np.ndarray:
        if self.character.is_card_playing():
            return self.character.playing_card.get_action_mask()
        else:
            mask = np.zeros((self.MAX_ACTION,), dtype=np.float32)
            # end turn
            mask[0] = 1
            for i, card in enumerate(self.character.hand_pile.cards):
                if self.character.can_play_card(i):
                    try:
                        mask[i + 1] = all(effect.can_play_card(card) for effect in self.character.effects)
                    except:
                        print(self.character.hand_pile.cards, i, card, len(self.character.hand_pile))
                        exit(0)
            return mask

    def observe(self, initial_hp: int = None, error: str = None) -> CombatObservation:
        # use potion
        # play card
        # end turn
        return CombatObservation(
            is_over=self.is_over,
            is_game_over=self.is_game_over,
            character_type=type(self.character),
            character_hp=self.character.hp,
            character_max_hp=self.character.max_hp,
            character_block=self.character.block,
            character_effects=self.character.effects,
            character_energy=self.character.energy,
            character_hp_lost=0 if initial_hp is None else initial_hp - self.character.hp,
            hand_pile=self.character.hand_pile,
            draw_pile=self.character.draw_pile,
            discard_pile=self.character.discard_pile,
            exhaust_pile=self.character.exhaust_pile,
            playing_card=self.character.playing_card,
            playing_step=0 if self.character.playing_card is None else self.character.playing_card.step,
            enemies_type=[type(enemy) for enemy in self.enemies],
            enemies_hp=[enemy.hp for enemy in self.enemies],
            enemies_max_hp=[enemy.max_hp for enemy in self.enemies],
            enemies_block=[enemy.block for enemy in self.enemies],
            enemies_effects=[enemy.effects for enemy in self.enemies],
            enemies_intent=[enemy.get_intent() for enemy in self.enemies],
            sum_enemies_attack=sum([enemy.get_intent().get_damage() for enemy in self.enemies]),
            action_mask=self.get_action_mask(),
            error=error,
        )

    def end_turn(self) -> None:
        self.character.end_turn()
        for enemy in self.enemies:
            enemy.start_turn()
        # The actions of enemies may cause changes to the list.
        for enemy in self.enemies.copy():
            enemy.perform()
        for enemy in self.enemies:
            enemy.end_turn()
        # Some intents need to be determined at the start of the turn.
        for enemy in self.enemies:
            enemy.get_intent()
        self.turn += 1
        self.character.start_turn()

    def step(self, action: int) -> CombatObservation:
        # print(self.turn, self.observe(), action)
        initial_hp = self.character.hp
        if self.character.is_card_playing():
            if not self.character.playing_card.can_choose(action):
                print("Invalid target", action, len(self.enemies), self.is_over, self.get_action_mask())
                return self.observe(error="Invalid target.")
            self.character.choose_in_card(action)
        else:
            if action == 0: # end_turn
                self.end_turn()
            else:
                if not self.character.can_play_card(action - 1):
                    print("Invalid action", action)
                    return self.observe(error="Invalid action.")
                self.character.play_card(action - 1)
        self.check_enemies()
        return self.observe(initial_hp=initial_hp)
