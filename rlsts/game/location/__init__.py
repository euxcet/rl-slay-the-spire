from ...utils.random import choose_with_prob
from .location import Location
from .monster_location import MonsterLocation
from .neow_location import NeowLocation
from .boss_location import BossLocation
from .elite_location import EliteLocation
from .merchant_location import MerchantLocation
from .treasure_location import TreasureLocation
from .event_location import EventLocation
from ..map import MapRoom, MapLocation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

def create_location(
    room: MapRoom,
    character: 'Character',
    num_monster_combat: int,
    num_event_not_monster: int,
    num_event_not_treasure: int,
    num_event_not_merchant: int,
) -> Location:
    return EventLocation(room=room, character=character, num_monster_combat=num_monster_combat)
    if room.location == MapLocation.Monster:
        return MonsterLocation(room=room, character=character, num_monster_combat=num_monster_combat)
    elif room.location == MapLocation.Neow:
        return NeowLocation(room=room, character=character)
    elif room.location == MapLocation.Boss:
        return BossLocation(room=room, character=character)
    elif room.location == MapLocation.Elite:
        return EliteLocation(room=room, character=character)
    elif room.location == MapLocation.Merchant:
        return MerchantLocation(room=room, character=character)
    elif room.location == MapLocation.Treasure:
        return TreasureLocation(room=room, character=character)
    elif room.location == MapLocation.Event:
        event_prob = 1 - 0.1 - 0.1 * num_event_not_monster \
                     - 0.02 - 0.02 * num_event_not_treasure \
                     - 0.03 - 0.03 * num_event_not_merchant
        location = choose_with_prob([
            (MonsterLocation, 0.1 + 0.1 * num_event_not_monster),
            (TreasureLocation, 0.02 + 0.02 * num_event_not_treasure),
            (MerchantLocation, 0.03 + 0.03 * num_event_not_merchant),
            (EventLocation, event_prob),
        ])
        return location(room=room, character=character, num_monster_combat=num_monster_combat)

    # Monster = 0
    # Event = 1
    # Elite = 2
    # RestSite = 3
    # Merchant = 4
    # Treasure = 5
    # Boss = 6
    # Neow = 7