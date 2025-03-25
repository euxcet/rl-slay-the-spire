from inspect import isfunction
import random
from typing import Any

def choose_with_prob(choices: list[tuple[Any, float]]) -> Any:
    p_sum = sum(map(lambda x: x[1], choices))
    r = random.random()
    for v, p in choices:
        if r < p / p_sum:
            if isfunction(v):
                return v()
            else:
                return v
        r -= p / p_sum
    raise Exception
