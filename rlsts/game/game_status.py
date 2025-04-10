class GameStatus():
    def __init__(
        self,
        floor: int = 0,
        is_in_room: bool = False,
        num_monster_combat: int = 0,
        num_event_not_monster: int = 0,
        num_event_not_treasure: int = 0,
        num_event_not_merchant: int = 0,
        card_removal_service_price: int = 75,
    ) -> None:
        self.floor = floor
        self.is_in_room = is_in_room
        self.num_monster_combat = num_monster_combat
        self.num_event_not_monster = num_event_not_monster
        self.num_event_not_merchant = num_event_not_merchant
        self.num_event_not_treasure = num_event_not_treasure
        self.card_removal_service_price = card_removal_service_price

    @property
    def is_choose_room(self) -> bool:
        return not self.is_in_room