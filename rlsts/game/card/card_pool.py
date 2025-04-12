import random
from ...utils.random import choose_with_prob
from . import ironclad_common_cards, ironclad_uncommon_cards, ironclad_rare_cards, ironclad_all_cards
from . import ironclad_attack_cards, ironclad_skill_cards, ironclad_power_cards
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

    def next_card(self, cards: list[type] = ironclad_all_cards()) -> Card:
        uncommon, rare = self.uncommon_prob, self.rare_prob
        common = 1 - uncommon - rare
        card: Card = random.choice(
            choose_with_prob([
                (ironclad_common_cards, common),
                (ironclad_uncommon_cards, uncommon),
                (ironclad_rare_cards, rare),
            ], cards=cards)
        )()
        if card.rarity == CardRarity.Common:
            self.num_common += 1
        else:
            self.num_common = 0
        return card

    def next_attack_card(self) -> Card:
        return self.next_card(ironclad_attack_cards())

    def next_skill_card(self) -> Card:
        return self.next_card(ironclad_skill_cards())

    def next_power_card(self) -> Card:
        return self.next_card(ironclad_power_cards())

    def next_common_card(self) -> Card:
        return random.choice(ironclad_common_cards())
        
    def next_uncommon_card(self) -> Card:
        return random.choice(ironclad_uncommon_cards())

    def next_rare_card(self) -> Card:
        return random.choice(ironclad_rare_cards())


monster_card_pool = CardPool(rare_prob_func=lambda t: max(0, t - 2) / 100)
merchant_card_pool = CardPool(rare_prob_func=lambda t: (t + 4) / 100)