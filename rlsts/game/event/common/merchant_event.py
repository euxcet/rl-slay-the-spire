import random
import numpy as np
from ..event import save_obs
from ...observation.merchant_observation import MerchantObservation
from ..event import Event
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...character import Character
    from ...card import Card, CardRarity
    from ...game_status import GameStatus
from ...card.card_pool import merchant_card_pool

class MerchantEvent(Event):
    act = []
    is_regular = False

    # 5 Colored Cards (Class-Specific)
    # 2 Colorless Cards
    # 3 Relics
    # 3 Potions
    # Card Removal Service
    # leave

    def __init__(self, character: 'Character', game_status: 'GameStatus') -> None:
        super().__init__(character=character)
        self.cards = [self.spawn_card(i) for i in range(7)]
        self.card_removal_service = True
        self.card_removal_service_price = game_status.card_removal_service_price

    def spawn_relic(self):
        return None

    def spawn_card(self, slot: int) -> tuple['Card', int]:
        if slot < 2:
            card = merchant_card_pool.next_attack_card()
        elif slot < 4:
            card = merchant_card_pool.next_skill_card()
        elif slot < 5:
            card = merchant_card_pool.next_power_card()
        else:
            card = None
        if card == None:
            cost = 0
        elif card.rarity == CardRarity.Common:
            cost = random.randint(45, 55)
        elif card.rarity == CardRarity.Uncommon:
            cost = random.randint(68, 82)
        elif card.rarity == CardRarity.Rare:
            cost = random.randint(135, 165)
        return (card, cost)

    @save_obs
    def observe(self) -> MerchantObservation:
        action_mask = np.ones(15)
        action_mask[7:13] = 0
        # cards
        for i in range(len(self.cards)):
            if self.cards[i][0] == None or self.cards[i][1] > self.character.gold:
                action_mask[i] = 0
        # relics

        # potions

        return MerchantObservation(
            cards=[card[0] for card in self.cards],
            cards_price=[card[1] for card in self.cards],
            card_removal_service=self.card_removal_service,
            card_removal_service_price=self.card_removal_service_price,
            action_mask=action_mask
        )

    @save_obs
    def reset(self) -> MerchantObservation:
        return self.observe()

    def step(self, action: int) -> MerchantObservation:
        if super().step(action):
            return self.observe()
        if action < 7: # cards
            if self.cards[action][0] != None and self.cards[action][1] <= self.character.gold:
                self.character.lose_gold(self.cards[action][1])
                self.character.deck.add_cards(self.cards[action][0])
        elif action == 13: # card removal service
            return self.remove_card_obs()
        elif action == 14: # leave
            return None
        return self.observe()