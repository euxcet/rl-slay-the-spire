import numpy as np
import random
from .character import Character, Ironclad
from .card import Deck
from .enemy import Cultist, JawWorm
from .combat import Combat, random_combat
from .map import Map, MapRoom, MapLocation
from enum import Enum
from .location import Location, create_location
from .location.event_location import EventLocation
from .location.monster_location import MonsterLocation
from .location.merchant_location import MerchantLocation
from .location.treasure_location import TreasureLocation
from .observation.choose_room_observation import ChooseRoomObservation
from .observation.combat_observation import CombatObservation
from .game_status import GameStatus

class SlayTheSpire():
    def __init__(self, character: Character = None) -> None:
        self.character = character or Ironclad(Deck.ironclad_starter_deck())
        self.locations = {}
        self.game_status = GameStatus(
            floor=0,
            is_in_room=True,
            num_monster_combat=0,
            num_event_not_monster=0,
            num_event_not_treasure=0,
            num_event_not_merchant=0,
        )

    @property
    def current_room(self) -> MapRoom:
        return self.map.current_room

    @property
    def current_location(self) -> Location:
        if self.current_room not in self.locations:
            new_location = create_location(
                room=self.current_room,
                character=self.character,
                game_status=self.game_status,
            )
            if isinstance(new_location, MonsterLocation):
                self.game_status.num_monster_combat += 1
            if self.current_room.location == MapLocation.Event:
                if not isinstance(new_location, MonsterLocation):
                    self.game_status.num_event_not_monster += 1
                elif not isinstance(new_location, MerchantLocation):
                    self.game_status.num_event_not_merchant += 1
                elif not isinstance(new_location, TreasureLocation):
                    self.game_status.num_event_not_treasure += 1
            self.locations[self.current_room] = new_location
        return self.locations[self.current_room]

    def get_random_combat(self) -> Combat:
        return random_combat(character=self.character)

    def observe_choose_room(self):
        return ChooseRoomObservation(
            options=self.current_room.edges,
            action_mask=np.array([edge != None for edge in self.current_room.edges]),
        )

    def reset(self, *, seed = None, options = None) -> tuple:
        random.seed(seed)
        self.map = Map.generate(act=1)
        self.game_status.is_in_room = True
        return self.current_location.reset()

    def step(self, action: int):
        if self.game_status.is_choose_room:
            self.map.step(action)
            self.game_status.floor = self.current_room.floor
            self.game_status.is_in_room = True
            return self.current_location.reset()
        else:
            obs = self.current_location.step(action)
            if obs == None:
                self.game_status.is_in_room = False
                # return self.observe_choose_room()
                # for test, skip room selection
                obs = self.observe_choose_room()
                for i in range(10):
                    if obs.action_mask[i] > 0:
                        return self.step(i)
            return obs
