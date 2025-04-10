from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect.buff.strength import Strength

class SpotWeakness(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Skill
    def __init__(self, buff: int = 3) -> None:
        super().__init__(
            cost=1,
            target_types=[CardTargetType.Enemy],
        )
        self.buff = buff

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        if enemy.get_intent().is_attack():
            self.effect_character(Strength(self.combat, self.buff))

class SpotWeaknessPlus(SpotWeakness):
    def __init__(self) -> None:
        super().__init__(buff=4)
