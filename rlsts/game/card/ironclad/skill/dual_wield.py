from copy import deepcopy
from ...card import Card, CardRarity, CardType, CardTargetType

class DualWield(Card):
    rarity = CardRarity.Uncommon
    type = CardType.Skill
    def __init__(self, num: int = 1) -> None:
        super().__init__(
            cost=1,
            target_types=[(CardTargetType.Hand, lambda x: x.type in [CardType.Attack, CardType.Power])],
        )
        self.num = num

    def finish(self, energy: int) -> None:
        if self.targets[0] != None and (card := self.choose_hand_card(self.targets[0])) != None:
            for n in range(self.num):
                self.character.draw_to_hand(deepcopy(card))

class DualWieldPlus(DualWield):
    def __init__(self) -> None:
        super().__init__(num=2)
