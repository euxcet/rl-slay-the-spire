from .card import Card, CardTargetType
from .pile import Pile
from ...utils.collection import Collection

card_collection = Collection()

# ./starter
from .starter.defend import Defend, DefendPlus
from .starter.strike import Strike, StrikePlus

# ./status
from .status.void import Void
from .status.wound import Wound
from .status.slimed import Slimed
from .status.dazed import Dazed
from .status.burn import Burn

# ./ironclad/attack
from .ironclad.attack.wild_strike import WildStrike, WildStrikePlus
from .ironclad.attack.pummel import Pummel, PummelPlus
from .ironclad.attack.dropkick import Dropkick, DropkickPlus
from .ironclad.attack.hemokinesis import Hemokinesis, HemokinesisPlus
from .ironclad.attack.immolate import Immolate, ImmolatePlus
from .ironclad.attack.sword_boomerang import SwordBoomerang, SwordBoomerangPlus
from .ironclad.attack.twin_strike import TwinStrike, TwinStrikePlus
from .ironclad.attack.fiend_fire import FiendFire, FiendFirePlus
from .ironclad.attack.heavy_blade import HeavyBlade, HeavyBladePlus
from .ironclad.attack.clash import Clash, ClashPlus
from .ironclad.attack.iron_wave import IronWave, IronWavePlus
from .ironclad.attack.whirlwind import Whirlwind, WhirlwindPlus
from .ironclad.attack.bash import Bash, BashPlus
from .ironclad.attack.uppercut import Uppercut, UppercutPlus
from .ironclad.attack.clothesline import Clothesline, ClotheslinePlus
from .ironclad.attack.feed import Feed, FeedPlus
from .ironclad.attack.cleave import Cleave, CleavePlus
from .ironclad.attack.reckless_charge import RecklessCharge, RecklessChargePlus
from .ironclad.attack.blood_for_blood import BloodForBlood, BloodForBloodPlus
from .ironclad.attack.rampage import Rampage, RampagePlus
from .ironclad.attack.bludgeon import Bludgeon, BludgeonPlus
from .ironclad.attack.headbutt import Headbutt, HeadbuttPlus
from .ironclad.attack.body_slam import BodySlam, BodySlamPlus
from .ironclad.attack.perfected_strike import PerfectedStrike, PerfectedStrikePlus
from .ironclad.attack.reaper import Reaper, ReaperPlus
from .ironclad.attack.thunderclap import Thunderclap, ThunderclapPlus
from .ironclad.attack.sever_soul import SeverSoul, SeverSoulPlus
from .ironclad.attack.carnage import Carnage, CarnagePlus
from .ironclad.attack.anger import Anger, AngerPlus
from .ironclad.attack.pommel_strike import PommelStrike, PommelStrikePlus
from .ironclad.attack.searing_blow import SearingBlow, SearingBlowPlus

# ./ironclad/skill
from .ironclad.skill.ghostly_armor import GhostlyArmor, GhostlyArmorPlus
from .ironclad.skill.entrench import Entrench, EntrenchPlus
from .ironclad.skill.disarm import Disarm, DisarmPlus
from .ironclad.skill.seeing_red import SeeingRed, SeeingRedPlus
from .ironclad.skill.shrug_it_off import ShrugItOff, ShrugItOffPlus
from .ironclad.skill.havoc import Havoc, HavocPlus
from .ironclad.skill.intimidate import Intimidate, IntimidatePlus
from .ironclad.skill.spot_weakness import SpotWeakness, SpotWeaknessPlus
from .ironclad.skill.armaments import Armaments, ArmamentsPlus
from .ironclad.skill.infernal_blade import InfernalBlade, InfernalBladePlus
from .ironclad.skill.rage import Rage, RagePlus
from .ironclad.skill.flame_barrier import FlameBarrier, FlameBarrierPlus
from .ironclad.skill.limit_break import LimitBreak, LimitBreakPlus
from .ironclad.skill.second_wind import SecondWind, SecondWindPlus
from .ironclad.skill.power_through import PowerThrough, PowerThroughPlus
from .ironclad.skill.true_grit import TrueGrit, TrueGritPlus
from .ironclad.skill.burning_pact import BurningPact, BurningPactPlus
from .ironclad.skill.double_tap import DoubleTap, DoubleTapPlus
from .ironclad.skill.battle_trance import BattleTrance, BattleTrancePlus
from .ironclad.skill.exhume import Exhume, ExhumePlus
from .ironclad.skill.bloodletting import Bloodletting, BloodlettingPlus
from .ironclad.skill.warcry import Warcry, WarcryPlus
from .ironclad.skill.impervious import Impervious, ImperviousPlus
from .ironclad.skill.flex import Flex, FlexPlus
from .ironclad.skill.dual_wield import DualWield, DualWieldPlus
from .ironclad.skill.sentinel import Sentinel, SentinelPlus
from .ironclad.skill.offering import Offering, OfferingPlus
from .ironclad.skill.shockwave import Shockwave, ShockwavePlus

# ./ironclad/power
from .ironclad.power.juggernaut import Juggernaut, JuggernautPlus
from .ironclad.power.evolve import Evolve, EvolvePlus
from .ironclad.power.demon_form import DemonForm, DemonFormPlus
from .ironclad.power.rupture import Rupture, RupturePlus
from .ironclad.power.brutality import Brutality, BrutalityPlus
from .ironclad.power.dark_embrace import DarkEmbrace, DarkEmbracePlus
from .ironclad.power.corruption import Corruption, CorruptionPlus
from .ironclad.power.fire_breathing import FireBreathing, FireBreathingPlus
from .ironclad.power.metallicize import Metallicize, MetallicizePlus
from .ironclad.power.inflame import Inflame, InflamePlus
from .ironclad.power.berserk import Berserk, BerserkPlus
from .ironclad.power.barricade import Barricade, BarricadePlus
from .ironclad.power.combust import Combust, CombustPlus
from .ironclad.power.feel_no_pain import FeelNoPain, FeelNoPainPlus

# ./starter
card_collection.add([Defend, DefendPlus])
card_collection.add([Strike, StrikePlus])

# ./status
card_collection.add(Void)
card_collection.add(Wound)
card_collection.add(Slimed)
card_collection.add(Dazed)
card_collection.add(Burn)

# ./ironclad/attack
card_collection.add([WildStrike, WildStrikePlus])
card_collection.add([Pummel, PummelPlus])
card_collection.add([Dropkick, DropkickPlus])
card_collection.add([Hemokinesis, HemokinesisPlus])
card_collection.add([Immolate, ImmolatePlus])
card_collection.add([SwordBoomerang, SwordBoomerangPlus])
card_collection.add([TwinStrike, TwinStrikePlus])
card_collection.add([FiendFire, FiendFirePlus])
card_collection.add([HeavyBlade, HeavyBladePlus])
card_collection.add([Clash, ClashPlus])
card_collection.add([IronWave, IronWavePlus])
card_collection.add([Whirlwind, WhirlwindPlus])
card_collection.add([Bash, BashPlus])
card_collection.add([Uppercut, UppercutPlus])
card_collection.add([Clothesline, ClotheslinePlus])
card_collection.add([Feed, FeedPlus])
card_collection.add([Cleave, CleavePlus])
card_collection.add([RecklessCharge, RecklessChargePlus])
card_collection.add([BloodForBlood, BloodForBloodPlus])
card_collection.add([Rampage, RampagePlus])
card_collection.add([Bludgeon, BludgeonPlus])
card_collection.add([Headbutt, HeadbuttPlus])
card_collection.add([BodySlam, BodySlamPlus])
card_collection.add([PerfectedStrike, PerfectedStrikePlus])
card_collection.add([Reaper, ReaperPlus])
card_collection.add([Thunderclap, ThunderclapPlus])
card_collection.add([SeverSoul, SeverSoulPlus])
card_collection.add([Carnage, CarnagePlus])
card_collection.add([Anger, AngerPlus])
card_collection.add([PommelStrike, PommelStrikePlus])
card_collection.add([SearingBlow, SearingBlowPlus])

# ./ironclad/skill
card_collection.add([GhostlyArmor, GhostlyArmorPlus])
card_collection.add([Entrench, EntrenchPlus])
card_collection.add([Disarm, DisarmPlus])
card_collection.add([SeeingRed, SeeingRedPlus])
card_collection.add([ShrugItOff, ShrugItOffPlus])
card_collection.add([Havoc, HavocPlus])
card_collection.add([Intimidate, IntimidatePlus])
card_collection.add([SpotWeakness, SpotWeaknessPlus])
card_collection.add([Armaments, ArmamentsPlus])
card_collection.add([InfernalBlade, InfernalBladePlus])
card_collection.add([Rage, RagePlus])
card_collection.add([FlameBarrier, FlameBarrierPlus])
card_collection.add([LimitBreak, LimitBreakPlus])
card_collection.add([SecondWind, SecondWindPlus])
card_collection.add([PowerThrough, PowerThroughPlus])
card_collection.add([TrueGrit, TrueGritPlus])
card_collection.add([BurningPact, BurningPactPlus])
card_collection.add([DoubleTap, DoubleTapPlus])
card_collection.add([BattleTrance, BattleTrancePlus])
card_collection.add([Exhume, ExhumePlus])
card_collection.add([Bloodletting, BloodlettingPlus])
card_collection.add([Warcry, WarcryPlus])
card_collection.add([Impervious, ImperviousPlus])
card_collection.add([Flex, FlexPlus])
card_collection.add([DualWield, DualWieldPlus])
card_collection.add([Sentinel, SentinelPlus])
card_collection.add([Offering, OfferingPlus])
card_collection.add([Shockwave, ShockwavePlus])

# ./ironclad/power
card_collection.add([Juggernaut, JuggernautPlus])
card_collection.add([Evolve, EvolvePlus])
card_collection.add([DemonForm, DemonFormPlus])
card_collection.add([Rupture, RupturePlus])
card_collection.add([Brutality, BrutalityPlus])
card_collection.add([DarkEmbrace, DarkEmbracePlus])
card_collection.add([Corruption, CorruptionPlus])
card_collection.add([FireBreathing, FireBreathingPlus])
card_collection.add([Metallicize, MetallicizePlus])
card_collection.add([Inflame, InflamePlus])
card_collection.add([Berserk, BerserkPlus])
card_collection.add([Barricade, BarricadePlus])
card_collection.add([Combust, CombustPlus])
card_collection.add([FeelNoPain, FeelNoPainPlus])

def upgrade(card: Card) -> Card:
    if card.__class__.__name__.endswith('Plus'):
        return card
    card_plus_class = globals().get(card.__class__.__name__ + 'Plus')
    upgraded: Card = card_plus_class()
    upgraded.cost = card.cost
    return upgraded
