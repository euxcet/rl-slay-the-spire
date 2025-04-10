from ..relic import Relic
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character
    from ...enemy import Enemy
    from ...combat import Combat
    from ....game.game_status import GameStatus
    from ...card import Card
    from ...target import Target
    from ...effect import Effect

class BlackBloodRelic(Relic):
    def __init__(
        self,
        character: 'Character',
        game_status: 'GameStatus',
    ) -> None:
        super().__init__(
            character=character,
            game_status=game_status
        )

    def on_combat_end(self):
        self.charac
