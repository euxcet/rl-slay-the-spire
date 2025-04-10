from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character
    from ..enemy import Enemy
    from ..combat import Combat
    from ...game.game_status import GameStatus
    from ..card import Card
    from ..target import Target
    from ..effect import Effect

class Relic(ABC):
    def __init__(self, character: 'Character', game_status: 'GameStatus') -> None:
        self.character = character
        self.game_status = game_status
        self.combat = None

    def to_combat(self, combat: 'Combat') -> Relic:
        self.combat = combat
        return self

    def leave_combat(self) -> Relic:
        self.combat = None
        return self

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

    def modify_received_hp(self, hp: int) -> int:
        return hp

    def modify_block(self, block: int) -> int:
        return block

    def modify_remove_block_turn(self, block: int) -> int:
        return block

    def modify_card_cost(self, card: 'Card', cost: int) -> int:
        return cost

    def on_combat_start(self) -> None:
        ...

    def on_combat_end(self) -> None:
        ...


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

    @property
    def enemies(self) -> list['Enemy']:
        return self.combat.enemies
    
    def __str__(self) -> str:
        return f"{type(self).__name__}"

    def __repr__(self) -> str:
        return self.__str__()

    def rich(self) -> str:
        return f"{type(self).__name__}"