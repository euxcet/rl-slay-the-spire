from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..map.map import MapRoom
    from ..character import Character
from .location import Location
from ..combat import Act1EasyCombat, Act1HardCombat
from ..game_status import GameStatus

class MonsterLocation(Location):
    def __init__(self, room: 'MapRoom', character: 'Character', game_status: GameStatus, **kwargs) -> None:
        super().__init__(room=room, character=character)
        self.num_monster_combat = game_status.num_monster_combat

    def reset(self):
        if self.num_monster_combat < 3:
            self.combat = Act1EasyCombat(character=self.character)
        else:
            self.combat = Act1HardCombat(character=self.character)
        return self.combat.reset()

    def step(self, action: int):
        return self.combat.step(action)
