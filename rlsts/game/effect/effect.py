from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..combat import Combat

class Effect():
    # TODO: ID

    def __init__(
        self,
        combat: 'Combat',
        stack: int,
        decrease_per_turn: int,
    ) -> None:
        self.stack = stack
        self.decrease_per_turn = decrease_per_turn

    def modify_damage(self, damage: int) -> int:
        return damage

    def modify_received_damage(self, damage: int) -> int:
        return damage

    def modify_block(self, block: int) -> int:
        return block