from .location import Location
from .monster_location import MonsterLocation
from .neow_location import NeowLocation
from ..map import MapRoom, MapLocation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

def create_location(room: MapRoom, character: 'Character'):
    if room.location == MapLocation.Monster:
        return MonsterLocation(floor=room.floor, character=character)
    elif room.location == MapLocation.Neow:
        return NeowLocation(floor=room.floor, character=character)

    # Monster = 0
    # Event = 1
    # Elite = 2
    # RestSite = 3
    # Merchant = 4
    # Treasure = 5
    # Boss = 6
    # Neow = 7