from .effect import Effect

from .buff.buff import Buff
from .buff.ritual import Ritual
from .buff.strength import Strength
from .buff.curl_up import CurlUp
from .buff.angry import Angry
from .buff.thievery import Thievery
from .buff.flame_barrier_buff import FlameBarrierBuff
from .buff.rage_buff import RageBuff
from .buff.barricade_buff import BarricadeBuff
from .buff.berserk_buff import BerserkBuff
from .buff.brutality_buff import BrutalityBuff
from .buff.combust_buff import CombustBuff
from .buff.corruption_buff import CorruptionBuff
from .buff.dark_embrace_buff import DarkEmbraceBuff
from .buff.evolve_buff import EvolveBuff
from .buff.feel_no_pain_buff import FeelNoPainBuff
from .buff.fire_breathing_buff import FireBreathingBuff
from .buff.flame_barrier_buff import FlameBarrierBuff
from .buff.juggernaut_buff import JuggernautBuff
from .buff.metallicize_buff import MetallicizeBuff
from .buff.rupture_buff import RuptureBuff

from .debuff.debuff import Debuff
from .debuff.vulnerable import Vulnerable
from .debuff.weak import Weak
from .debuff.frail import Frail
from .debuff.entangled import Entangled
from .debuff.dexterity_down import DexterityDown
from .debuff.strength_down import StrengthDown
from .debuff.no_draw import NoDraw
from .debuff.confused import Confused

from ...utils.collection import Collection

effect_collection = Collection()

effect_collection.add(Ritual)
effect_collection.add(Strength)
effect_collection.add(CurlUp)
effect_collection.add(Angry)
effect_collection.add(Thievery)
effect_collection.add(FlameBarrierBuff)
effect_collection.add(RageBuff)
effect_collection.add(BarricadeBuff)
effect_collection.add(BerserkBuff)
effect_collection.add(BrutalityBuff)
effect_collection.add(CombustBuff)
effect_collection.add(CorruptionBuff)
effect_collection.add(DarkEmbraceBuff)
effect_collection.add(EvolveBuff)
effect_collection.add(FeelNoPainBuff)
effect_collection.add(FireBreathingBuff)
effect_collection.add(FlameBarrierBuff)
effect_collection.add(JuggernautBuff)
effect_collection.add(MetallicizeBuff)
effect_collection.add(RuptureBuff)

effect_collection.add(Vulnerable)
effect_collection.add(Weak)
effect_collection.add(Frail)
effect_collection.add(StrengthDown)
effect_collection.add(Entangled)
effect_collection.add(DexterityDown)
effect_collection.add(NoDraw)
effect_collection.add(Confused)