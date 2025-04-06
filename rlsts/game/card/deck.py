from __future__ import annotations

import random
from .card import Card

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

class Deck():
    def __init__(self, cards: list[Card]) -> None:
        self.cards = cards

    def add_cards(self, cards: Card | list[Card]) -> None:
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)

    @staticmethod
    def ironclad_starter_deck() -> Deck:
        return Deck([
            Strike(), Strike(), Strike(), Strike(), Strike(),
            Defend(), Defend(), Defend(), Defend(),
            Bash(),
        ])

    @staticmethod
    def ironclad_random_deck() -> Deck:
        # return Deck([Shockwave(), SpotWeakness(), TrueGrit(), ArmamentsPlus(), BodySlam(), Cleave(), \
        #              Clothesline(), Headbutt(), PommelStrike(), Thunderclap(), TwinStrike(), WildStrike(),\
        #              Bludgeon(), FiendFire(), Immolate()])
        card_types = {
            "strike": ([Strike], random.randint(3, 5), 10, 0),
            
            "defend": ([Defend], random.randint(5, 5), 10, 0),

            "bash": ([Bash], random.randint(1, 1), 10, 0),

            "attack": ([
                Anger, BodySlam, Clash, Cleave, Clothesline, Headbutt,
                IronWave, PommelStrike, SwordBoomerang, Thunderclap, TwinStrike,
                WildStrike, BloodForBlood, Carnage, Dropkick, Hemokinesis,
                Pummel, Rampage, RecklessCharge, SeverSoul, Uppercut,
                Whirlwind, Bludgeon, FiendFire, Immolate,
                # TODO: HeavyBlade Feed Reaper SearingBlow
            ], random.randint(0, 4), 2, 0.1),

            "skill": ([
                Armaments, BattleTrance, Bloodletting, BurningPact, Disarm,
                DualWield, Entrench, Exhume, FlameBarrier, Flex, GhostlyArmor,
                Havoc, Impervious, InfernalBlade, Intimidate, LimitBreak, Offering,
                PowerThrough, Rage, SecondWind, SeeingRed, Sentinel, Shockwave,
                ShrugItOff, SpotWeakness, TrueGrit, Warcry,
                # TODO: DoubleTap InfernalBlade
            ], random.randint(0, 4), 2, 0.1),

            "power": ([
                Juggernaut, Evolve, DemonForm, Rupture, Brutality, DarkEmbrace,
                Corruption, FireBreathing, Metallicize, Inflame, Berserk,
                Barricade, Combust, FeelNoPain
            ], random.randint(0, 3), 2, 0.1),
        }

        cards = []
        for k, v in card_types.items():
            types, num, duplicate, upgrade_p = v
            for i in range(num):
                while True:
                    card_type = random.choice(types)
                    if sum(map(lambda x: isinstance(x, card_type), cards)) < duplicate:
                        if random.random() < upgrade_p:
                            from . import upgrade
                            cards.append(upgrade(card_type()))
                        else:
                            cards.append(card_type())
                        break
        return Deck(cards)
