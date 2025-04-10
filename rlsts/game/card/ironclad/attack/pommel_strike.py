from ...card import Card, CardRarity, CardType, CardTargetType

class PommelStrike(Card):
    rarity = CardRarity.Common
    type = CardType.Attack
    def __init__(self, damage: int = 9, draw: int = 1) -> None:
        super().__init__(
            cost=1,
            target_types=[CardTargetType.Enemy],
        )
        self.damage = damage
        self.draw = draw

    def finish(self, energy: int) -> None:
        enemy = self.get_enemy(self.targets[0])
        self.attack(enemy, self.damage)
        self.combat.character.draw(self.draw)

class PommelStrikePlus(PommelStrike):
    def __init__(self) -> None:
        super().__init__(damage=10, draw=2)
