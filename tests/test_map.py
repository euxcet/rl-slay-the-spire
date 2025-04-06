from rlsts.game.map import Map

class TestMap():
    def test_map(self):
        m = Map.generate()
        print()
        print(m)