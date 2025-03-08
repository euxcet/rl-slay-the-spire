from rlsts.game.slay_the_spire import SlayTheSpire

class TestGame():
    def test_game(self):
        game = SlayTheSpire()
        combat = game.get_combat()

        obs = combat.reset()
        print(obs)