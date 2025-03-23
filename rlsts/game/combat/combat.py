from .combat_observation import CombatObservation
from ..character import Character
from ..enemy import Enemy

class Combat():
    MAX_ACTION = 10

    def __init__(
        self,
        character: Character,
        enemies: list[Enemy],
    ) -> None:
        self.character = character
        self.enemies = enemies
        self.turn = 0
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
            error=error,
        )

    def end_turn(self, initial_hp: int = None) -> CombatObservation:
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
        return self.observe(initial_hp=initial_hp)

    def step(self, action: int) -> CombatObservation:
        initial_hp = self.character.hp

        if self.character.is_card_playing():
            if not self.character.playing_card.can_choose(action):
                return self.observe(error="Invalid target.")
            self.character.choose_in_card(action)
        else:
            if action == 0: # end_turn
                return self.end_turn(initial_hp=initial_hp)
            else:
                if not self.character.can_play_card(action):
                    return self.observe(error="Invalid action.")
                self.character.play_card(action - 1)
        return self.observe(initial_hp=initial_hp)
