from .character import Character
from ..card.deck import Deck

class Ironclad(Character):
    def __init__(self):
        super().__init__(
            hp=80,
            gold=100,
            deck=Deck.ironclad_starter_deck(),
        )