import pydash as _
from ...card import Card, CardRarity, CardType, CardTargetType

class BurningPact(Card):
    def __init__(self, draw: int = 2) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Skill,
            cost=1,
            target_types=[CardTargetType.Hand],
        )
        self.draw = draw

    def finish(self, energy: int) -> None:
        _.invoke(self.choose_hand_card(self.targets[0]), 'exhaust')
        self.character.draw(self.draw)

class BurningPactPlus(BurningPact):
    def __init__(self) -> None:
        super().__init__(draw=3)
