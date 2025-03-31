from ...card import Card, CardRarity, CardType
from ....effect.buff.evolve_buff import EvolveBuff

class Evolve(Card):
    def __init__(self, buff: int = 1) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Power,
            cost=1,
            target_types=[],
        )
        self.buff = buff

    def finish(self, energy: int) -> None:
        self.effect_character(EvolveBuff(self.combat, self.buff))

class EvolvePlus(Evolve):
    def __init__(self) -> None:
        super().__init__(buff=2)
