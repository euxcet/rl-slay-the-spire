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
        from ..buff.buff import Buff
        from ..debuff.debuff import Debuff
        if self.stack > 0 and effect != None and \
            ((isinstance(effect, Debuff) and effect.stack > 0) or (isinstance(effect, Buff) and effect.stack < 0)):
            self.stack -= 1
            return None
        return effect