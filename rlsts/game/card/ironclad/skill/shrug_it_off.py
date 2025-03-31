from ...card import Card, CardRarity, CardType, CardTargetType

class ShrugItOff(Card):
    def __init__(self, block: int = 6) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Skill,
            cost=1,
            target_types=[],
        )
        self.block = block
        self.draw = 1

    def finish(self, energy: int) -> None:
        self.character.add_block(self.block)
        self.character.draw(self.draw)

class ShrugItOffPlus(ShrugItOff):
    def __init__(self) -> None:
        super().__init__(block=11)
