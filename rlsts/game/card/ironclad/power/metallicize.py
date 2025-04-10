from ...card import Card, CardRarity, CardType
from ....effect.buff.metallicize_buff import MetallicizeBuff

class Metallicize(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Power
    def __init__(self, buff: int = 3) -> None:
        super().__init__(
            cost=1,
            target_types=[],
        )
        self.buff = buff

    def finish(self, energy: int) -> None:
        self.effect_character(MetallicizeBuff(self.combat, self.buff))

class MetallicizePlus(Metallicize):
    def __init__(self) -> None:
        super().__init__(buff=4)
