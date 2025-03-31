import pydash as _
from ...card import Card, CardRarity, CardType, CardTargetType

class TrueGrit(Card):
    def __init__(self, block: int = 7) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Skill,
            cost=1,
            target_types=[],
        )
        self.block = block

    def finish(self, energy: int) -> None:
        self.add_block(self.block)
        if len(self.targets) == 0:
            _.invoke(self.choose_hand_card(), 'exhaust')
        else:
            _.invoke(self.choose_hand_card(self.targets[0]), 'exhaust')

class TrueGritPlus(TrueGrit):
    def __init__(self) -> None:
        super().__init__(block=9)
        self.target_types = [CardTargetType.Hand]
