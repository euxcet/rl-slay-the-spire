import random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..map.map import MapRoom
    from ..character import Character
from .location import Location
from ..combat import Act1EasyCombat, Act1HardCombat
from ..game_status import GameStatus
from ..observation.combat_observation import CombatObservation
from ..observation.choose_card_observation import ChooseCardObservation

class MonsterLocation(Location):
    def __init__(self, room: 'MapRoom', character: 'Character', game_status: GameStatus, **kwargs) -> None:
        super().__init__(room=room, character=character)
        self.num_monster_combat = game_status.num_monster_combat
        self.gold = random.randint(10, 20)
        # 0 combat
        # 1 choose card
        self.status = 0
        self.choose_card_obs = None

    def reset(self):
        if self.num_monster_combat < 3:
            self.combat = Act1EasyCombat(character=self.character)
        else:
            self.combat = Act1HardCombat(character=self.character)
        return self.combat.reset()

    def step(self, action: int):
        if self.status == 0:
            obs = self.combat.step(action)
            if isinstance(obs, CombatObservation) and not obs.is_game_over and obs.is_over:
                self.character.receive_gold(self.gold)
                # TODO: potion
                self.status = 1
                self.choose_card_obs = ChooseCardObservation.monster_observation()
                return self.choose_card_obs
            return obs 
        elif self.status == 1:
            self.character.deck.add_cards(self.choose_card_obs.options[action].set_character(character=self.character))
            return None
