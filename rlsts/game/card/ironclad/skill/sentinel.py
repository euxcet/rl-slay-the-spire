from ...card import Card, CardRarity, CardType, CardTargetType

class Sentinel(Card):
    def __init__(self, block: int = 5, energy: int = 2) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Skill,
            cost=1,
            target_types=[],
        )
        self.block = block
        self.energy = energy

    def finish(self, energy: int) -> None:
        self.add_block(self.block)

    def on_exhaust(self) -> None:
        super().on_exhaust()
        self.character.energy += self.energy

class SentinelPlus(Sentinel):
    def __init__(self) -> None:
        super().__init__(block=8, energy=3)
