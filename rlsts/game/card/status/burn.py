from ..card import Card, CardRarity, CardType, CardTargetType

class Burn(Card):
    def __init__(self, damage: int = 2) -> None:
        super().__init__(
            rarity=CardRarity.Common,
            type=CardType.Status,
            cost=0,
            target_types=[],
            is_unplayable=True,
        )
        self.damage = damage

    def finish(self, energy: int) -> None:
        ...

    def on_turn_discard(self):
        self.character.receive_damage(self.damage, None, do_effect=False)

class BurnPlus(Burn):
    def __init__(self) -> None:
        super().__init__(damage=4)
