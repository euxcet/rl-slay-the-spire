# TODO
from copy import deepcopy
from ...card import Card, CardRarity, CardType, CardTargetType

class Metallicize(Card):
    def __init__(self, damage: int = 6) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Power,
            cost=0,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)
        self.combat.character.discard_pile.insert(deepcopy(self))

class MetallicizePlus(Metallicize):
    def __init__(self) -> None:
        super().__init__(damage=8)
