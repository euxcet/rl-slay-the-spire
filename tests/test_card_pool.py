from rlsts.game.card.card_pool import CardPool, card_pool, merchant_card_pool
from rlsts.game.card import CardRarity
from rich.console import Console

class TestCardPool():
    def test_card_pool(self):
        console = Console()
        pool = card_pool
        common = 0
        uncommon = 0
        rare = 0
        count = 100000
        for i in range(count):
            x = pool.next_card()
            common += x.rarity == CardRarity.Common
            uncommon += x.rarity == CardRarity.Uncommon
            rare += x.rarity == CardRarity.Rare
        print(common / count, uncommon / count, rare / count)

        pool = merchant_card_pool
        common = 0
        uncommon = 0
        rare = 0
        count = 100000
        for i in range(count):
            x = pool.next_card()
            common += x.rarity == CardRarity.Common
            uncommon += x.rarity == CardRarity.Uncommon
            rare += x.rarity == CardRarity.Rare
        print(common / count, uncommon / count, rare / count)