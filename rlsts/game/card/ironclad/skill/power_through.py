from ...card import Card, CardRarity, CardType, CardTargetType
from ...status.wound import Wound

class PowerThrough(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Skill
    def __init__(self, block: int = 15) -> None:
        super().__init__(
            cost=1,
            target_types=[],
        )
        self.block = block
        self.wound = 2

    def finish(self, energy: int) -> None:
        for num in range(self.wound):
            self.character.draw_to_hand(Wound().to_combat(self.combat))
        self.add_block(self.block)

class PowerThroughPlus(PowerThrough):
    def __init__(self) -> None:
        super().__init__(block=20)
