from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..combat import Combat
    from ..enemy import Enemy
    from ..character import Character

class Effect():
    # TODO: ID

    def __init__(
        self,
        combat: 'Combat',
        stack: int,
        decrease_per_turn: int,
    ) -> None:
        self.stack = stack
        self.combat = combat
        self.decrease_per_turn = decrease_per_turn
        self.target_enemy: 'Enemy' = None

    def modify_damage(self, damage: int) -> int:
        return damage

    def modify_received_damage(self, damage: int) -> int:
        return damage

    def modify_block(self, block: int) -> int:
        return block

    @property
    def target(self) -> 'Enemy | Character':
        return self.combat.character if self.target_enemy is None else self.target_enemy