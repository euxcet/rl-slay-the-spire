from ...card import Card, CardRarity, CardType, CardTargetType

class SeeingRed(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Skill
    def __init__(self, cost: int = 1) -> None:
        super().__init__(
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
