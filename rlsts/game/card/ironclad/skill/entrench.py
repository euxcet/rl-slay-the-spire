from ...card import Card, CardRarity, CardType, CardTargetType

class Entrench(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Skill
    def __init__(self, cost: int = 2) -> None:
        super().__init__(
            cost=cost,
            target_types=[],
        )

    def finish(self, energy: int) -> None:
        self.character.block *= 2

class EntrenchPlus(Entrench):
    def __init__(self) -> None:
        super().__init__(cost=1)
