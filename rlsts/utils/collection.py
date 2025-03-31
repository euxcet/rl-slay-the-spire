import numpy as np

class Collection():
    def __init__(self) -> None:
        self.num: int = 1 # 0 for Placeholder(None)
        self.types: dict[type, int] = {}

    def add(self, t: type | list) -> None:
        if isinstance(t, list):
            for x in t:
                self.add(x)
            return
        if t in self.types:
            return
        t.ID = self.num
        self.types[t] = self.num
        self.num += 1

    def tensor(self, ts: list[type], dtype: type = np.int32, values: list[int] = None) -> np.ndarray:
        r = np.zeros(self.num, dtype=dtype)
        values = values or [1 for _ in range(len(ts))]
        for t, v in zip(ts, values):
            if t is None:
                r[0] += v
            elif isinstance(t, type):
                r[self.types[t]] += v
            else:
                r[self.types[type(t)]] += v
        return r
    
    def __len__(self) -> int:
        return self.num
