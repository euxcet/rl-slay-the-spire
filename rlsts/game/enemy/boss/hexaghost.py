import random
from ..enemy import Enemy
from ..intent import Intent, SkipIntent, AttackIntent
from ..intent import HexaghostInflameIntent, HexaghostDividerIntent, HexaghostInfernoIntent, HexaghostSearIntent

class Hexaghost(Enemy):
    def __init__(self, hp: int = None) -> None:
        super().__init__(hp=random.randint(140, 140) if hp is None else hp)
        self.upgrade_burn = False
        self.inferno_damage = 2
        self.inferno_times = 6
        self.inferno_burn = 3
        self.tackle_damage = 5
        self.tackle_times = 2
        self.sear_damage = 6
        self.sear_burn = 1
        self.inflame_strength = 2
        self.inflame_block = 12
        self.divider_damage = 0 # depend on character's hp
        self.divider_times = 6

    def get_intent(self) -> Intent:
        pattern = (self.combat.turn - 2) % 7
        if self.combat.turn == 0:
            return SkipIntent(self, [])
        elif self.combat.turn == 1:
            return HexaghostDividerIntent(self, [self.divider_damage, self.divider_times])
        elif pattern == 0:
            return HexaghostSearIntent(self, [self.sear_damage, self.sear_burn])
        elif pattern == 1:
            return AttackIntent(self, [self.tackle_damage, self.tackle_times], is_multi=True)
        elif pattern == 2:
            return HexaghostSearIntent(self, [self.sear_damage, self.sear_burn])
        elif pattern == 3:
            return HexaghostInflameIntent(self, [self.inflame_strength, self.inflame_block])
        elif pattern == 4:
            return AttackIntent(self, [self.tackle_damage, self.tackle_times], is_multi=True)
        elif pattern == 5:
            return HexaghostSearIntent(self, [self.sear_damage, self.sear_burn])
        elif pattern == 6:
            return HexaghostInfernoIntent(self, [self.inferno_damage, self.inferno_times, self.inferno_burn])
