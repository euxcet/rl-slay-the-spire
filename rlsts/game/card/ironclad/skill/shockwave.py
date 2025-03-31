from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect.debuff.weak import Weak
from ....effect.debuff.vulnerable import Vulnerable

class Shockwave(Card):
    def __init__(self, debuff: int = 3) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Skill,
            cost=2,
            target_types=[],
        )
        self.debuff = debuff

    def finish(self, energy: int) -> None:
        for enemy in self.enemies.copy():
            self.effect_enemy(enemy, Weak(self.combat, self.debuff))
            self.effect_enemy(enemy, Vulnerable(self.combat, self.debuff))

class ShockwavePlus(Shockwave):
    def __init__(self) -> None:
        super().__init__(debuff=5)
