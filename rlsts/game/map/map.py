from __future__ import annotations
from enum import Enum
import random

class MapLocation(Enum):
    Monster = 0
    Event = 1
    Elite = 2
    RestSite = 3
    Merchant = 4
    Treasure = 5
    Boss = 6
    Neow = 7

    @staticmethod
    def prob() -> tuple[list, list]:
        # ascension level >= 1
        return [MapLocation.Monster, MapLocation.Event, MapLocation.Elite, MapLocation.RestSite, MapLocation.Merchant, MapLocation.Treasure], \
               [0.45, 0.22, 0.16, 0.12, 0.05, 0]
        # return [MapLocation.Monster, MapLocation.Event, MapLocation.Elite, MapLocation.RestSite, MapLocation.Merchant, MapLocation.Treasure], \
        #        [0.49, 0.22, 0.16, 0.08, 0.05, 0]

class MapRoom():
    def __init__(self, floor: int, column: int, location: MapLocation = MapLocation.Monster) -> None:
        self.floor = floor
        self.column = column
        if location == MapLocation.Neow:
            self.edges: list[MapRoom] = []
        else:
            self.edges: list[MapRoom] = [None, None, None]
        self.vis = False
        self.location = location
        self.fathers: list[MapRoom] = []

    def set_left_sibling(self, sibling: MapRoom):
        self.left_sibling = sibling

    def set_right_sibling(self, sibling: MapRoom):
        self.right_sibling = sibling

    @property
    def valid(self) -> list[bool]:
        if self.location == MapLocation.Neow:
            return [True] * len(self.edges)
        return [self.column > 0 and self.left_sibling.edges[2] == None, True, self.column < 6 and self.right_sibling.edges[0] == None]

    def __eq__(self, other: MapRoom) -> bool:
        if other is None:
            return False
        return self.floor == other.floor and self.column == other.column

    def __str__(self) -> str:
        if not self.vis:
            return ' '
        return ['M', '?', 'E', 'R', '$', 'T'][self.location.value]

class Map():
    def __init__(self, rooms: list[list[MapRoom]], neow_room: MapRoom, boss_room: MapRoom) -> None:
        self.rooms = rooms
        self.neow_room = neow_room
        self.boss_room = boss_room
        self.current_room = neow_room

    @staticmethod
    def is_valid_location(room: MapRoom, location: MapLocation, exist: list[MapLocation]) -> bool:
        if room.floor == 0:
            return location == MapLocation.Monster
        if room.floor == 8:
            return location == MapLocation.Treasure
        if room.floor == 14:
            return location == MapLocation.RestSite
        if location in [MapLocation.Elite, MapLocation.Merchant, MapLocation.RestSite]:
            for father in room.fathers:
                if father.location == location:
                    return False
        if location in [MapLocation.Elite, MapLocation.RestSite] and room.floor < 5:
            return False
        if location in exist:
            return False
        if room.floor == 13 and location == MapLocation.RestSite:
            return False
        return True

    @staticmethod
    def generate() -> Map:
        rooms = [[MapRoom(i, j) for j in range(7)] for i in range(15)]
        for i in range(15):
            for j in range(6):
                rooms[i][j].set_right_sibling(rooms[i][j + 1])
                rooms[i][j + 1].set_left_sibling(rooms[i][j])
        for step in range(6):
            current = random.choice(rooms[0])
            while step == 1 and current.vis:
                current = random.choice(rooms[0])
            current.vis = True
            for i in range(14):
                edge = random.choice([0, 1, 2])
                while not current.valid[edge]:
                    edge = random.choice([0, 1, 2])
                if edge == 0:
                    current.edges[edge] = rooms[current.floor + 1][current.column - 1]
                elif edge == 1:
                    current.edges[edge] = rooms[current.floor + 1][current.column]
                elif edge == 2:
                    current.edges[edge] = rooms[current.floor + 1][current.column + 1]
                current.edges[edge].fathers.append(current)
                current = current.edges[edge]
                current.vis = True
        for j in range(7):
            rooms[0][j].location = MapLocation.Monster
        for i in range(14):
            for j in range(7):
                if rooms[i][j].vis:
                    exist = []
                    for son in rooms[i][j].edges:
                        if son != None:
                            if son.floor == 8:
                                location = MapLocation.Treasure
                            else:
                                location = random.choices(MapLocation.prob()[0], weights=MapLocation.prob()[1])[0]
                                while not Map.is_valid_location(son, location, exist):
                                    location = random.choices(MapLocation.prob()[0], MapLocation.prob()[1])[0]
                            son.location = location
                            exist.append(location)
        neow_room = MapRoom(floor=-1, column=0, locaiton=MapLocation.Neow)
        boss_room = MapRoom(floor=15, column=0, locaiton=MapLocation.Boss)
        for j in range(7):
            if rooms[0][j].vis:
                neow_room.edges.append(rooms[0][j])
            if rooms[14][j].vis:
                rooms[14][j].edges[1] = boss_room
        return Map(rooms=rooms, neow_room=neow_room, boss_room=boss_room)
    
    def __str__(self) -> str:
        result = ''
        for i in reversed(range(15)):
            if i < 14:
                for x in range(13):
                    j = x // 2
                    if x % 2 == 0:
                        result += '|' if self.rooms[i][j].edges[1] != None else ' '
                    else:
                        assert(not (self.rooms[i][j].edges[2] != None and self.rooms[i][j + 1].edges[0] != None))
                        if self.rooms[i][j].edges[2] != None:
                            result += '/'
                        elif self.rooms[i][j + 1].edges[0] != None:
                            result += '\\'
                        else:
                            result += ' '
                result += '\n'
            result += ' '.join(map(str, self.rooms[i])) + '\n'
        return result
