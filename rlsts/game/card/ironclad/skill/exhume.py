from ...card import Card, CardRarity, CardType, CardTargetType

class Exhume(Card):
    rarity = CardRarity.Rare
    type = CardType.Skill
    def __init__(self, cost: int = 1) -> None:
        super().__init__(
            cost=cost,
            target_types=[CardTargetType.Exhaust],
            is_exhaust=True,
        )

    def finish(self, energy: int) -> None:
        if self.targets[0] != None:
            self.exhaust_pile[self.targets[0]].move_to(self.hand_pile)

class ExhumePlus(Exhume):
    def __init__(self) -> None:
        super().__init__(cost=0)
