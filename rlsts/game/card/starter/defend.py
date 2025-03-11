from ..card import Card, CardRarity, CardType, CardTargetType

class Defend(Card):
    def __init__(self):
        super().__init__(
            rarity=CardRarity.Starter,
            type=CardType.Skill,
            energy=1,
            playable=True,
            target_types=[],
        )
        self.block = 5

    def finish(self) -> None:
        self.add_block(self.block)
