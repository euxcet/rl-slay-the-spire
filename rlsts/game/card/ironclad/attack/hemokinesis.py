from ...card import Card, CardRarity, CardType, CardTargetType

class Hemokinesis(Card):
    def __init__(self, damage: int = 15) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Attack,
            cost=1,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.combat.character.lose_hp(2)
        self.attack(enemy, self.damage)

class HemokinesisPlus(Hemokinesis):
    def __init__(self) -> None:
        super().__init__(damage=20)
