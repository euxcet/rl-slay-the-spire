from .character import Character, Ironclad
from .enemy import Cultist, JawWorm
from .combat import Combat, Act1EasyCombat, Act1HardCombat

class SlayTheSpire():
    def __init__(self, character: Character = None) -> None:
        self.character = character or Ironclad()

    def get_combat(self, enemies: list[type]) -> Combat:
        return Combat(character=self.character, enemies_type=enemies)

    def get_act1_easy_combat(self) -> Combat:
        return Act1EasyCombat(character=self.character)

    def get_act1_hard_combat(self) -> Combat:
        return Act1HardCombat(character=self.character)
