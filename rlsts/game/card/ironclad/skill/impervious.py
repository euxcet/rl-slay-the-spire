from ...card import Card, CardRarity, CardType, CardTargetType

class Impervious(Card):
    def __init__(self, block: int = 30) -> None:
        super().__init__(
            rarity=CardRarity.Rare,
            type=CardType.Skill,
            cost=2,
            target_types=[],
            is_exhaust=True
        )
        self.block = block

    def finish(self, energy: int) -> None:
        self.add_block(self.block)

class ImperviousPlus(Impervious):
    def __init__(self) -> None:
        super().__init__(block=40)
