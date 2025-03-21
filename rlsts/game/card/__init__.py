import numpy as np
from .card import Card, CardTargetType
from .starter import Strike, Defend
from .ironclad import Bash
from .status import Slimed
from ...utils.collection import Collection

card_collection = Collection()

card_collection.add(Strike)
card_collection.add(Defend)
card_collection.add(Bash)

card_collection.add(Slimed)
