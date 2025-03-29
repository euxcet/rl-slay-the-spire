from ...card import Card, CardRarity, CardType, CardTargetType

class Headbutt(Card):
    def __init__(self, damage: int = 9) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Attack,
            cost=1,
            target_types=[CardTargetType.Enemy, CardTargetType.Discard],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)
        if self.targets[1] != None:
            self.discard_pile[self.targets[1]].move_to(self.draw_pile)

class HeadbuttPlus(Headbutt):
    def __init__(self) -> None:
        super().__init__(damage=12)
