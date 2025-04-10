from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect.buff.strength import Strength

class Disarm(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Skill
    def __init__(self, debuff: int = 2) -> None:
        super().__init__(
            cost=1,
            target_types=[CardTargetType.Enemy],
            is_exhaust=True,
        )
        self.debuff = debuff

    def finish(self, energy: int) -> None:
        self.effect_enemy(self.get_enemy(self.targets[0]), Strength(self.combat, -self.debuff))

class DisarmPlus(Disarm):
    def __init__(self) -> None:
        super().__init__(debuff=3)
