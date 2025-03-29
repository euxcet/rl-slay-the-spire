from ...card import Card, CardRarity, CardType, CardTargetType

class Whirlwind(Card):
    def __init__(self, damage: int = 5) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Attack,
            cost=None, # x
            target_types=[],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        for _ in range(energy):
            for enemy in self.combat.enemies.copy():
                self.attack(enemy, self.damage)

class WhirlwindPlus(Whirlwind):
    def __init__(self) -> None:
        super().__init__(damage=8)
