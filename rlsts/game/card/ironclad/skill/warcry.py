import pydash as _
from ...card import Card, CardRarity, CardType, CardTargetType

class Warcry(Card):
    def __init__(self, draw: int = 1) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Skill,
            cost=0,
            target_types=[CardTargetType.Hand],
        )
        self.draw = draw

    def on_play(self) -> None:
        self.character.draw(self.draw)

    def finish(self, energy: int) -> None:
        _.invoke(self.choose_hand_card(self.targets[0]), 'move_to', self.draw_pile)

class WarcryPlus(Warcry):
    def __init__(self) -> None:
        super().__init__(draw=2)
