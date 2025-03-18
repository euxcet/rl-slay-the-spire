from .combat_observation import CombatObservation
from ..character import Character
from ..enemy import Enemy

class Combat():
    def __init__(
        self,
        character: Character,
        enemies: list[Enemy],
    ) -> None:
        self.character = character
        self.enemies = enemies
        self.turn = 0
        self.action_shape = 10
        self.is_over = False
        self.is_game_over = False
        self.update_enemy()

    def update_enemy(self) -> None:
        for position, enemy in enumerate(self.enemies):
            enemy.position = position

    def add_enemy(self, position: int, enemy: Enemy) -> None:
        self.enemies.insert(position, enemy)
        self.update_enemy()

    def remove_enemy(self, enemy: Enemy) -> None:
        self.enemies.remove(enemy)
        self.update_enemy()
        if len(self.enemies) == 0:
            self.is_over = True

    def reset(self) -> CombatObservation:
        self.combat_over = False
        self.turn = 0
        self.character.start_combat(self)
        for enemy in self.enemies:
            enemy.start_combat(self)
        self.character.start_turn()
        return self.observe()

    def observe(self) -> CombatObservation:
        # use potion
        # play card
        # end turn
        return CombatObservation(
            is_over=self.is_over,
            is_game_over=self.is_game_over,
            character_type=type(self.character),
            character_hp=self.character.hp,
            character_block=self.character.block,
            character_effects=self.character.effects,
            character_energy=self.character.energy,
            hand_cards=self.character.hand_pile.cards,
            playing_card=self.character.playing_card,
            playing_step=0 if self.character.playing_card is None else self.character.playing_card.current_target_id,
            enemies_type=[type(enemy) for enemy in self.enemies],
            enemies_hp=[enemy.hp for enemy in self.enemies],
            enemies_block=[enemy.block for enemy in self.enemies],
            enemies_effects=[enemy.effects for enemy in self.enemies],
            enemies_intent=[enemy.get_intent() for enemy in self.enemies],
            sum_enemies_attack=sum([enemy.get_intent().get_damage() for enemy in self.enemies]),
        )

    def end_turn(self) -> CombatObservation:
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
        # TODO: check dead
        self.turn += 1
        self.character.start_turn()
        return self.observe()

    def step(self, action: int) -> CombatObservation:
        if action == self.action_shape - 1: # end_turn
            if self.character.is_card_playing():
                print("Error action.")
                return self.observe()
            return self.end_turn()
        if not self.character.is_card_playing():
            if not self.character.can_play_card(action):
                print('Error action.')
                return self.observe()
            self.character.play_card(action)
        else:
            self.character.choose_in_card(action)
        return self.observe()
