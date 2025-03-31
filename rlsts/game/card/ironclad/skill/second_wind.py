from ...card import Card, CardRarity, CardType, CardTargetType

class SecondWind(Card):
    def __init__(self, block: int = 5) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Skill,
            cost=1,
            target_types=[],
        )
        self.block = block

    def finish(self, energy: int) -> None:
        for card in self.hand_pile.cards.copy():
            if card.type != CardType.Attack:
                card.exhaust()
                self.add_block(self.block)

class SecondWindPlus(SecondWind):
    def __init__(self) -> None:
        super().__init__(block=7)
