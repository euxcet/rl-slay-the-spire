from ...card import Card, CardRarity, CardType, CardTargetType

class Offering(Card):
    def __init__(self, draw: int = 3) -> None:
        super().__init__(
            rarity=CardRarity.Rare,
            type=CardType.Skill,
            cost=0,
            target_types=[],
            is_exhaust=True,
        )
        self.lose = 6
        self.add_energy = 2
        self.draw = draw

    def finish(self, energy: int) -> None:
        self.character.lose_hp(self.lose)
        self.character.energy += self.add_energy
        self.character.draw(self.draw)

class OfferingPlus(Offering):
    def __init__(self) -> None:
        super().__init__(draw=5)
