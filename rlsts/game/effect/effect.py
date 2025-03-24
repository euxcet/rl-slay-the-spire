from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..combat import Combat
    from ..target import Target

class Effect():
    # TODO: ID

    def __init__(
        self,
        combat: 'Combat',
        stack: int,
        decrease_per_turn: int,
        skip: int = 0,
    ) -> None:
        self.stack = stack
        self.combat = combat
        self.decrease_per_turn = decrease_per_turn
        self.target: Target = None
        self.skip = skip

    def modify_damage(self, damage: int) -> int:
        return damage

    def modify_received_damage(self, damage: int) -> int:
        return damage

    def modify_block(self, block: int) -> int:
        return block

    def on_turn_end(self) -> None:
        ...

    def on_receive_damage(self, damage: int) -> None:
        ...

    def on_attack(self) -> None:
        ...
