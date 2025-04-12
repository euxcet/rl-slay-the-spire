from inspect import isfunction
import random
from typing import Any

def choose_with_prob(choices: list[tuple[Any, float]], *args, **kwargs) -> Any:
    p_sum = sum(map(lambda x: x[1], choices))
    r = random.random()
    for v, p in choices:
        if r < p / p_sum:
            if isfunction(v):
                return v(*args, **kwargs)
            else:
                return v
        r -= p / p_sum
    raise Exception
