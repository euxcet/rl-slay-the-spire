from ...card import Card, CardRarity, CardType
from ....effect.buff.juggernaut_buff import JuggernautBuff

class Juggernaut(Card):
    def __init__(self, buff: int = 5) -> None:
        super().__init__(
            rarity=CardRarity.Rare,
            type=CardType.Power,
            cost=2,
            target_types=[],
        )
        self.buff = buff

    def finish(self, energy: int) -> None:
        self.effect_character(JuggernautBuff(self.combat, self.buff))

class JuggernautPlus(Juggernaut):
    def __init__(self) -> None:
        super().__init__(buff=7)
