from ...card import Card, CardRarity, CardType, CardTargetType

class BloodForBlood(Card):
    def __init__(self, cost: int = 4, damage: int = 18) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Attack,
            cost=cost,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)

    @property
    def cost(self) -> int:
        return max(self._cost - self.combat.character.num_lose_hp, 0)

class BloodForBloodPlus(BloodForBlood):
    def __init__(self) -> None:
        super().__init__(cost=3, damage=22)
