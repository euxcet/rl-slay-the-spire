from ..card import Card, CardRarity, CardType, CardTargetType

class Defend(Card):
    rarity = CardRarity.Starter
    type = CardType.Skill
    def __init__(self, block: int = 5) -> None:
        super().__init__(
            cost=1,
            target_types=[],
        )
        self.block = block

    def finish(self, energy: int) -> None:
        self.add_block(self.block)

class DefendPlus(Defend):
    def __init__(self) -> None:
        super().__init__(block=8)