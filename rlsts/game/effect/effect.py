from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..combat import Combat
    from ..target import Target
    from ..card import Card

class Effect():
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
        self.max_stack = 999
        self.min_stack = -999

    def set_stack(self, stack: int) -> None:
        self.stack = min(max(stack, self.min_stack), self.max_stack)

    def modify_draw(self, num: int) -> int:
        return num

    def modify_turn_draw(self, num: int) -> int:
        return num

    def modify_turn_energy(self, energy: int) -> int:
        return energy

    def modify_num_draw(self, num: int) -> int:
        return num

    def modify_damage(self, damage: int) -> int:
        return damage

    def modify_received_damage(self, damage: int) -> int:
        return damage

    def modify_received_effect(self, effect: Effect) -> Effect:
        return effect

    def modify_block(self, block: int) -> int:
        return block

    def modify_remove_block_turn(self, block: int) -> int:
        return block

    def modify_card_cost(self, card: 'Card', cost: int) -> int:
        return cost

    def on_turn_start(self) -> None:
        ...

    def on_turn_end(self) -> None:
        self.stack -= self.decrease_per_turn

    def on_play_card(self, card: 'Card') -> None:
        ...

    def on_receive_damage(self, damage: int, attacker: 'Target') -> None:
        ...

    def on_lose_hp(self, hp: int) -> None:
        ...

    def on_attack(self, damage: int) -> None:
        ...

    def on_attacked(self, damage: int, attacker: 'Target') -> None:
        ...

    def on_block(self, block: int) -> None:
        ...

    def on_draw(self, card: 'Card') -> 'Card':
        return card

    def on_exhaust(self, card: 'Card') -> None:
        ...

    def can_play_card(self, card: 'Card') -> bool:
        return True

    def merge(self, effect: Effect) -> None:
        # TODO: check
        self.stack = max(min(self.max_stack, self.stack + effect.stack), self.min_stack)
