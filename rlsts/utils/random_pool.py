import numpy as np

class RandomPool():
    def __init__(self):
        self.generator = np.random.default_rng()
        self.pool = []

    def _fill(self, l: int) -> None:
        while len(self.pool) < l:
            self.pool.append(self.generator.random())

    def get(self) -> float:
        self._fill(1)
        return self.pool.pop(0)

    def get_list(self, l: int) -> list[float]:
        self._fill(l)
        result = self.pool[:l]
        self.pool = self.pool[l:]
        return result

    # return a random integer within [a, b)
    def get_int(self, a: int, b: int) -> int:
        return int(a + (b - a) * self.get())

    def get_int_list(self, l: int, a: int, b: int) -> int:
        return list(map(lambda x: int(a + (b - a) * x), self.get_list(l)))

    def peek(self, offset: int = 0) -> float:
        self._fill(offset + 1)
        return self.pool[offset]