from ..card import Card, CardRarity, CardType, CardTargetType

class Defend(Card):
    def __init__(self, block: int = 5) -> None:
        super().__init__(
            rarity=CardRarity.Starter,
            type=CardType.Skill,
            cost=1,
            target_types=[],
        )
        self.block = block

    def finish(self) -> None:
        self.add_block(self.block)

class DefendPlus(Defend):
    def __init__(self) -> None:
        super().__init__(block=8)