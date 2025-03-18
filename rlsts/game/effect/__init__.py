from .effect import Effect

from .buff.buff import Buff
from .buff.ritual import Ritual
from .buff.strength import Strength
from .buff.curl_up import CurlUp

from .debuff.debuff import Debuff
from .debuff.vulnerable import Vulnerable

from ...utils.collection import Collection

effect_collection = Collection()
effect_collection.add(Ritual)
effect_collection.add(Vulnerable)