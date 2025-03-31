from copy import deepcopy
from ...card import Card, CardRarity, CardType, CardTargetType

class DualWield(Card):
    def __init__(self, num: int = 1) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Skill,
            cost=1,
            target_types=[(CardTargetType.Hand, lambda x: x.type in [CardType.Attack, CardType.Power])],
        )
        self.num = num

    def finish(self, energy: int) -> None:
        if (card := self.choose_hand_card(self.targets[0])) != None:
            for n in range(self.num):
                self.character.draw_to_hand(deepcopy(card))

class DualWieldPlus(DualWield):
    def __init__(self) -> None:
        super().__init__(num=2)
