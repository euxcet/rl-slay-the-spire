from ...card import Card, CardRarity, CardType, CardTargetType

class Armaments(Card):
    def __init__(self) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Skill,
            cost=1,
            target_types=[CardTargetType.Hand],
        )

    def finish(self, energy: int) -> None:
        from ... import upgrade
        if len(self.target_types) == 0:
            upgraded_cards = [upgrade(card).to(self.combat) for card in self.hand_pile]
            self.hand_pile.clear()
            self.hand_pile.extend(upgraded_cards)
        else:
            if self.targets[0] != None:
                self.hand_pile.cards[self.targets[0]] = upgrade(self.choose_hand_card(self.targets[0])).to(self.combat)

class ArmamentsPlus(Armaments):
    def __init__(self) -> None:
        super().__init__()
        self.target_types = []
