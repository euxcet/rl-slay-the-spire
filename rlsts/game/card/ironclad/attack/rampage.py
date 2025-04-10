from ...card import Card, CardRarity, CardType, CardTargetType

class Rampage(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Attack
    def __init__(self, damage_inc: int = 5) -> None:
        super().__init__(
            cost=1,
            target_types=[CardTargetType.Enemy],
        )
        self.damage_inc = damage_inc
        self.damage = 8

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)
        self.damage += self.damage_inc

class RampagePlus(Rampage):
    def __init__(self) -> None:
        super().__init__(damage_inc=8)
