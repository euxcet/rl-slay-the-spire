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

    def enemy_die(self) -> None:
        self.enemies = [enemy for enemy in self.enemies if not enemy.died]

    def observe(self) -> CombatObservation:
        return CombatObservation(
            character_hp=self.character.hp,
            character_block=self.character.block,
        )

    def reset(self) -> CombatObservation:
        print(type(self.character), 'run')
        self.character.start_combat(self)
        print('done')
        for enemy in self.enemies:
            print(type(enemy))
            enemy.start_combat(self)
        return self.observe()

    def observe(self) -> CombatObservation:
        # use potion
        # play card
        # end turn

        # self.character.play()
        # for enemy in self.enemies:
        #     enemy.move()
        ...

    def end_turn(self) -> CombatObservation:
        ...

    def step(self, action: int) -> CombatObservation:
        if action == self.action_shape - 1: # end_turn
            return self.end_turn()
            # for enemy in self.enemies:
            #     enemy.perform()
            # # TODO: check dead
            # self.turn += 1

        # if not self.character.has_playable_card():
        #     for enemy in self.enemies:
        #         enemy.perform()
        #     # TODO: check dead
        #     self.turn += 1

        if not self.character.is_card_played():
            self.character.play_card(action)
        else:
            self.character.choose_in_card(action)
