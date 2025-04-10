from ...card import Card, CardRarity, CardType, CardTargetType
from ....effect.buff.rage_buff import RageBuff

class Rage(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Skill
    def __init__(self, buff: int = 3) -> None:
        super().__init__(
            cost=0,
            target_types=[],
        )
        self.buff = buff

    def finish(self, energy: int) -> None:
        self.effect_character(RageBuff(self.combat, self.buff))

class RagePlus(Rage):
    def __init__(self) -> None:
        super().__init__(buff=5)
