from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..map.map import MapRoom
    from ..character import Character
from .location import Location
from ..combat import Act1BossCombat
from ..observation.combat_observation import CombatObservation
from ..observation.choose_card_observation import ChooseCardObservation

class BossLocation(Location):
    def __init__(self, room: 'MapRoom', character: 'Character', **kwargs) -> None:
        super().__init__(room=room, character=character)
        self.status = 0
        self.choose_card_obs = None

    def reset(self):
        self.combat = Act1BossCombat(character=self.character)
        return self.combat.reset()

    def step(self, action: int):
        if self.status == 0:
            obs = self.combat.step(action)
            # # TODO
            # if isinstance(obs, CombatObservation) and not obs.is_game_over and obs.is_over:
                # self.character.receive_gold(self.gold)
                # self.status = 1
                # self.choose_card_obs = ChooseCardObservation.monster_observation()
                # return self.choose_card_obs
            return obs 
        elif self.status == 1:
            if action > 0:
                self.character.deck.add_cards(self.choose_card_obs.options[action - 1].set_character(character=self.character))
            return None
