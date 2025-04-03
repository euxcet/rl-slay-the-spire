from .buff import Buff

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..effect import Effect
    from ...combat import Combat

class Artifact(Buff):
    def __init__(
        self,
        combat: 'Combat',
        stack: int,
    ) -> None:
        super().__init__(combat=combat, stack=stack, decrease_per_turn=0)

    def modify_received_effect(self, effect: 'Effect') -> 'Effect':
        from ..debuff.debuff import Debuff
        if effect != None and isinstance(effect, Debuff) and self.stack > 0:
            self.stack -= 1
            return None
        return effect