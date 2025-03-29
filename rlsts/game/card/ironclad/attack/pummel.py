from ...card import Card, CardRarity, CardType, CardTargetType

class Pummel(Card):
    def __init__(self, times: int = 4) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Attack,
            cost=1,
            target_types=[CardTargetType.Enemy],
            is_exhaust=True,
        )
        self.damage = 2
        self.times = times

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        for _ in range(self.times):
            self.attack(enemy, self.damage)

class PummelPlus(Pummel):
    def __init__(self) -> None:
        super().__init__(times=5)
