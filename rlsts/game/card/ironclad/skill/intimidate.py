from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect.debuff.weak import Weak

class Intimidate(Card):
    def __init__(self, debuff: int = 1) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Skill,
            cost=0,
            target_types=[],
            is_exhaust=True,
        )
        self.debuff = debuff

    def finish(self, energy: int) -> None:
        for enemy in self.enemies.copy():
            self.effect_enemy(enemy, Weak(self.combat, self.debuff))

class IntimidatePlus(Intimidate):
    def __init__(self) -> None:
        super().__init__(debuff=2)
