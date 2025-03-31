from ...card import Card, CardRarity, CardType, CardTargetType

class GhostlyArmor(Card):
    def __init__(self, block: int = 10) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Skill,
            cost=1,
            target_types=[],
            is_ethereal=True,
        )
        self.block = block

    def finish(self, energy: int) -> None:
        self.add_block(self.block)

class GhostlyArmorPlus(GhostlyArmor):
    def __init__(self) -> None:
        super().__init__(block=13)
