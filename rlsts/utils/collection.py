import numpy as np

class Collection():
    def __init__(self) -> None:
        self.num: int = 0
        self.types: list[type] = []

    def add(self, t: type) -> None:
        t.ID = self.num
        self.types.append(t)
        self.num += 1

    def tensor(self, ts: list[type]) -> np.ndarray:
        r = np.zeros(self.num, np.int8)
        for t in ts:
            if t is not type:
                t = type(t)
            for i in range(len(self.types)):
                if self.types[i] == t:
                    r[i] += 1
        return r
    
    def __len__(self) -> int:
        return self.num