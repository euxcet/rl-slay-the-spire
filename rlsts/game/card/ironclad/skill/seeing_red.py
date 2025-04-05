from ...card import Card, CardRarity, CardType, CardTargetType

class SeeingRed(Card):
    def __init__(self, cost: int = 1) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Skill,
            cost=cost,
            target_types=[],
            is_exhaust=True,
        )
        self.add_energy = 2

    def finish(self, energy: int) -> None:
        self.character.energy += self.add_energy

class SeeingRedPlus(SeeingRed):
    def __init__(self) -> None:
        super().__init__(cost=0)
