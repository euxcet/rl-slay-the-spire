import random
from ...utils.random import choose_with_prob
from . import ironclad_common_cards, ironclad_uncommon_cards, ironclad_rare_cards
from .card import Card, CardRarity

class CardPool():
    def __init__(
        self,
        uncommon_prob: float = 0.37,
        rare_prob_func = None,
    ) -> None:
        self.num_common = 0
        self.uncommon_prob = uncommon_prob
        self.rare_prob_func = rare_prob_func

    @property
    def rare_prob(self) -> float:
        return self.rare_prob_func(self.num_common)

    def next_card(self) -> Card:
        uncommon, rare = self.uncommon_prob, self.rare_prob
        common = 1 - uncommon - rare
        card: Card = random.choice(
            choose_with_prob([
                (ironclad_common_cards, common),
                (ironclad_uncommon_cards, uncommon),
                (ironclad_rare_cards, rare),
            ])
        )()
        if card.rarity == CardRarity.Common:
            self.num_common += 1
        else:
            self.num_common = 0
        return card

card_pool = CardPool(rare_prob_func=lambda t: max(0, t - 2) / 100)
merchant_card_pool = CardPool(rare_prob_func=lambda t: (t + 4) / 100)