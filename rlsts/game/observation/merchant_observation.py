import numpy as np
from ..card import Card

class MerchantObservation():
    # 5 Colored Cards (Class-Specific)
    # 2 Colorless Cards
    # 3 Relics
    # 3 Potions
    # Card Removal Service

    # action_mask
    # id    action
    # 0     leave
    # 1     card removal service
    # 2     colored card 0
    # 3     colored card 1
    # 4     colored card 2
    # 5     colored card 3
    # 6     colored card 4
    # 7     colorless card 0
    # 8     colorless card 1
    # 9     relic 0
    # 10    relic 1
    # 11    relic 2
    # 12    potion 0
    # 13    potion 1
    # 14    potion 2

    def __init__(
        self,
        cards: list[Card],
        cards_price: list[int],
        # relics: list[Relic],
        # relics_price: list[int],
        # potions: list[Potion],
        # potions_price: list[int],
        card_removal_service: bool,
        card_removal_service_price: int,
        action_mask: np.ndarray,
    ) -> None:
        self.cards = cards
        self.cards_price = cards_price
        self.card_removal_service = card_removal_service
        self.card_removal_service_price = card_removal_service_price
        self.action_mask = action_mask