from ...card import Card, CardRarity, CardType, CardTargetType

class Bloodletting(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Skill
    def __init__(self, add_energy: int = 2) -> None:
        super().__init__(
            cost=0,
            target_types=[],
        )
        self.add_energy = add_energy
        self.hp = 3

    def finish(self, energy: int) -> None:
        self.character.energy += self.add_energy
        self.character.lose_hp(self.hp)

class BloodlettingPlus(Bloodletting):
    def __init__(self) -> None:
        super().__init__(add_energy=3)
