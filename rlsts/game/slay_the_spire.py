import random
from .character import Character, Ironclad
from .card import Deck
from .enemy import Cultist, JawWorm
from .combat import Combat, random_combat
from .map import Map

class SlayTheSpire():
    def __init__(self, character: Character = None) -> None:
        self.character = character or Ironclad(Deck.ironclad_starter_deck())
        self.map = Map.generate()

    def get_random_combat(self) -> Combat:
        return random_combat(character=self.character)

    def reset(self, *, seed = None, options = None) -> tuple:
        random.seed(seed)
        self.map = Map.generate()
        return self.map.current_room

    def step(self, action: int):
        ...