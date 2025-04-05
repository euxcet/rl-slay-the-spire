import random
from ..enemy import Enemy
from ..intent import Intent, AttackIntent, BlockIntent, TheGuardianVentSteamIntent, TheGuardianDefensiveModeIntent, TheGuardianTwinSlamIntent
from ...effect.buff.mode_shift import ModeShift
from ...effect.buff.sharp_hide import SharpHide
from enum import Enum

class TheGuardianMode(Enum):
    OFFENSIVE = 0
    DEFENSIVE = 1

class TheGuardian(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(240, 240) if hp is None else hp)
        # offensive
        self.charging_up = 9
        self.fierce_bash = 32
        self.vent_stream = 2
        self.whirlwind_damage = 5
        self.whirlwind_repeat = 4
        # defensive
        self.sharp_hide = 3
        self.roll_attack = 9
        self.twin_slam_damage = 8
        self.twin_slam_times = 2

        self.mode_start_turn = 0
        self.mode = TheGuardianMode.OFFENSIVE

        self.defensive_block = 20
        self.mode_shift = 20

    def start_combat(self, combat) -> None:
        super().start_combat(combat)
        self.receive_effect(ModeShift(self.combat, self.mode_shift))

    def get_intent(self) -> Intent:
        if self.mode == TheGuardianMode.OFFENSIVE:
            pattern = (self.combat.turn - self.mode_start_turn) % 4
            if (self.combat.turn > 4 and pattern == 1) or self.combat.turn == 0:
                return BlockIntent(self, [self.charging_up])
            elif (self.combat.turn > 4 and pattern == 2) or self.combat.turn == 1:
                return AttackIntent(self, [self.fierce_bash], is_multi=False)
            elif (self.combat.turn > 4 and pattern == 3) or self.combat.turn == 2:
                return TheGuardianVentSteamIntent(self, [self.vent_stream])
            else:
                return AttackIntent(self, [self.whirlwind_damage, self.whirlwind_repeat], is_multi=True)
        else:
            pattern = (self.combat.turn - self.mode_start_turn) % 3
            if pattern == 0:
                return TheGuardianDefensiveModeIntent(self, [self.sharp_hide])
            elif pattern == 1:
                return AttackIntent(self, [self.roll_attack], is_multi=False)
            elif pattern == 2:
                return TheGuardianTwinSlamIntent(self, [self.twin_slam_damage, self.twin_slam_times])

    def shift_mode(self) -> None:
        if self.mode == TheGuardianMode.OFFENSIVE:
            self.mode = TheGuardianMode.DEFENSIVE
            self.add_block(self.defensive_block)
            self.mode_start_turn = self.combat.turn
        else:
            self.mode = TheGuardianMode.OFFENSIVE
            self.mode_shift += 10
            self.remove_effect(SharpHide)
            self.receive_effect(ModeShift(self.combat, self.mode_shift))
            self.mode_start_turn = self.combat.turn + 1
