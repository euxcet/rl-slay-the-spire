from ...card import Card, CardRarity, CardType
from ....effect.buff.ritual import Ritual

class DemonForm(Card):
    rarity = CardRarity.Rare
    type = CardType.Power
    def __init__(self, buff: int = 2) -> None:
        super().__init__(
            cost=3,
            target_types=[],
        )
        self.buff = buff

    def finish(self, energy: int) -> None:
        self.effect_character(Ritual(self.combat, self.buff, 0))

class DemonFormPlus(DemonForm):
    def __init__(self) -> None:
        super().__init__(buff=3)