from __future__ import annotations
from abc import ABC, abstractmethod
from .effect import Effect
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .combat import Combat

class Target(ABC):
    def __init__(
        self,
        hp: int,
        max_hp: int,
    ) -> None:
        self.hp = hp
        self.max_hp = max_hp
        self.block: int = 0
        self.effects: list[Effect] = []
        self.combat: Combat = None
        self.died: bool = False

    def start_combat(self, combat: 'Combat') -> Target:
        self.combat = combat
        self.effects.clear()
        self.num_lose_hp = 0
        return self

    def die(self) -> None:
        self.hp = 0
        self.died = True

    def start_turn(self) -> None:
        for effect in self.effects:
            effect.on_turn_start()
        remove_block = self.block
        for effect in self.effects:
            remove_block = effect.modify_remove_block_turn(remove_block)
        self.block -= remove_block
        self.update_effects()

    def end_turn(self) -> None:
        for effect in self.effects:
            effect.on_turn_end()
        self.update_effects()

    def add_block(self, block: int, do_effect: bool = True) -> int:
        if do_effect:
            for effect in self.effects:
                block = effect.modify_block(block)
        self.block += block
        for effect in self.effects:
            effect.on_block(block)

    def receive_damage(self, damage: int, attacker: Target, do_effect: bool = True) -> int:
        if self.died:
            return 0
        for effect in self.effects:
            effect.on_attacked(damage, attacker)
        if do_effect:
            damage = self.estimate_received_damage(damage)
        if damage <= 0:
            return 0
        # TODO: relics ...
        if damage <= self.block:
            self.block -= damage
            return 0
        damage -= self.block
        self.block = 0
        self.num_lose_hp += 1
        if damage >= self.hp:
            hp = self.hp
            self.die()
            return hp
        self.hp -= damage
        for effect in self.effects:
            effect.on_receive_damage(damage, attacker)
        self.on_receive_damage(damage, attacker)
        return damage

    def receive_effect(self, new_effect: Effect) -> None:
        if self.died or new_effect == None or new_effect.stack == 0:
            return
        for effect in self.effects:
            new_effect = effect.modify_received_effect(new_effect)
        if new_effect == None or new_effect.stack == 0:
            return
        
        new_effect.target = self
        for effect in self.effects:
            if type(effect) == type(new_effect):
                effect.merge(new_effect)
                # effect.set_stack(effect.stack + new_effect.stack)
                if effect.stack == 0:
                    self.update_effects()
                return
        self.effects.append(new_effect)

    def prepare_attack(self, damage: int) -> int:
        for effect in self.effects:
            damage = effect.modify_damage(damage)
        return damage

    def update_effects(self) -> None:
        self.effects = [effect for effect in self.effects if effect.stack != 0]

    def estimate_received_damage(self, damage: int) -> int:
        for effect in self.effects:
            damage = effect.modify_received_damage(damage)
        # TODO: relics ...
        return damage

    def has_effect(self, effect_type: type) -> int:
        if (effect := self.get_effect(effect_type)) != None:
            return effect.stack
        return 0

    def get_effect(self, effect_type: type) -> Effect:
        for effect in self.effects:
            if isinstance(effect, effect_type):
                return effect
        return None

    def lose_hp(self, hp: int) -> int:
        if hp > 0:
            self.hp -= hp
            self.num_lose_hp += 1
            if self.hp <= 0:
                self.die()
            else:
                for effect in self.effects:
                    effect.on_lose_hp(hp)

    def on_receive_damage(self, damage: int, attacker: Target) -> None:
        ...
