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

    def observe(self) -> CombatObservation:
        ...

    def reset(self) -> CombatObservation:
        self.character.start_combat(self)
        for enemy in self.enemies:
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

    def step(self, action: int) -> CombatObservation:
        if not self.character.has_playable_card():
            for enemy in self.enemies:
                enemy.perform()
            # TODO: check dead
            self.turn += 1
        if not self.character.is_card_played():
            self.character.play_card(action)
        else:
            self.character.choose_in_card(action)
