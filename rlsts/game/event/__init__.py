from ...utils.random import choose_with_prob
from .event import Event
from ...utils.collection import Collection

# act1
from .act1.neow_event import NeowEvent
from .act1.big_fish_event import BigFishEvent
from .act1.golden_idol_event import GoldenIdolEvent
from .act1.living_wall_event import LivingWallEvent
from .act1.scrap_ooze_event import ScrapOozeEvent
from .act1.shining_light_event import ShiningLightEvent
from .act1.the_cleric_event import TheClericEvent
from .act1.the_ssssserpent_event import TheSsssserpentEvent
from .act1.world_of_goop_event import WorldOfGoopEvent

# common
from .common.duplicator_event import DuplicatorEvent
from .common.golden_shrine_event import GoldenShrineEvent
from .common.ominous_forge_event import OminousForgeEvent
from .common.purifier_event import PurifierEvent
from .common.transmogrifier_event import TransmogrifierEvent
from .common.upgrade_shrine_event import UpgradeShrineEvent
from .common.wheel_of_change_event import WheelOfChangeEvent

event_collection = Collection()
event_collection.add(NeowEvent)
event_collection.add(BigFishEvent)
event_collection.add(GoldenIdolEvent)
event_collection.add(LivingWallEvent)
event_collection.add(ScrapOozeEvent)
event_collection.add(ShiningLightEvent)
event_collection.add(TheClericEvent)
event_collection.add(TheSsssserpentEvent)
event_collection.add(WorldOfGoopEvent)
event_collection.add(DuplicatorEvent)
event_collection.add(GoldenShrineEvent)
event_collection.add(OminousForgeEvent)
event_collection.add(PurifierEvent)
event_collection.add(TransmogrifierEvent)
event_collection.add(UpgradeShrineEvent)
event_collection.add(WheelOfChangeEvent)

act1_event_collection = event_collection.find(lambda x: 1 in x.act)

def choose_event(collection: list[type]) -> type:
    return choose_with_prob(list(map(lambda x: (x, 0.75 if x.is_regular else 0.25), collection)))