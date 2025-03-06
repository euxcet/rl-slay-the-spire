NUM_CARD = 0

def add_num():
    NUM_CARD += 1
    return NUM_CARD

from .starter import Strike, Defend

Strike.ID = add_num()
Defend.ID = add_num()