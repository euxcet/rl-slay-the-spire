import time
from rlsts.game.map import Map

class TestMap():
    def test_map(self):
        runs = 10000
        t = time.time()
        for i in range(runs):
            m = Map.generate(i)
        cost = time.time() - t
        print(f'Time cost: {cost}s  Runs: {runs}  Maps/s: {runs / (time.time() - t)}')