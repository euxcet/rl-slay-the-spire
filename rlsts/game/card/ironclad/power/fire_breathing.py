from ...card import Card, CardRarity, CardType
from ....effect.buff.fire_breathing_buff import FireBreathingBuff

class FireBreathing(Card):
    def __init__(self, buff: int = 6) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Power,
            cost=1,
            target_types=[],
        )
        self.buff = buff

    def finish(self, energy: int) -> None:
        self.effect_character(FireBreathingBuff(self.combat, self.buff))

class FireBreathingPlus(FireBreathing):
    def __init__(self) -> None:
        super().__init__(buff=10)
