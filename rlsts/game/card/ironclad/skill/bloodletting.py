from ...card import Card, CardRarity, CardType, CardTargetType

class Bloodletting(Card):
    def __init__(self, energy: int = 2) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Skill,
            cost=0,
            target_types=[],
        )
        self.energy = energy
        self.hp = 3

    def finish(self, energy: int) -> None:
        self.character.energy += self.energy
        self.character.lose_hp(self.hp)

class BloodlettingPlus(Bloodletting):
    def __init__(self) -> None:
        super().__init__(energy=3)
