from ....effect.debuff.no_draw import NoDraw
from ...card import Card, CardRarity, CardType

class BattleTrance(Card):
    def __init__(self, draw: int = 3) -> None:
        super().__init__(
            rarity=CardRarity.Uncommon,
            type=CardType.Skill,
            cost=0,
            target_types=[],
        )
        self.draw = draw

    def finish(self, energy: int) -> None:
        self.character.draw(self.draw)
        self.effect_character(NoDraw(self.combat, 1))

class BattleTrancePlus(BattleTrance):
    def __init__(self) -> None:
        super().__init__(draw=4)
