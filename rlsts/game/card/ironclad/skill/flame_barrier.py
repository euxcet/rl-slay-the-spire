from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect import FlameBarrierBuff

class FlameBarrier(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Skill
    def __init__(self, block: int = 12, buff: int = 4) -> None:
        super().__init__(
            cost=2,
            target_types=[],
        )
        self.block = block
        self.buff = buff

    def finish(self, energy: int) -> None:
        self.add_block(self.block)
        self.effect_character(FlameBarrierBuff(self.combat, self.buff))

class FlameBarrierPlus(FlameBarrier):
    def __init__(self) -> None:
        super().__init__(block=16, buff=6)
