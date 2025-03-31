from ...card import Card, CardRarity, CardType, CardTargetType

class Havoc(Card):
    def __init__(self, cost: int = 1) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Skill,
            cost=cost,
            target_types=[],
        )

    def finish(self, energy: int) -> None:
        if len(self.draw_pile) > 0 and (top := self.draw_pile.draw()) != None:
            top.random_play(self.character.energy)
            top.exhaust()

class HavocPlus(Havoc):
    def __init__(self) -> None:
        super().__init__(cost=0)
