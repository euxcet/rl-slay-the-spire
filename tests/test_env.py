from rich.console import Console
from rlsts.game.slay_the_spire import SlayTheSpire
from rlsts.env.combat_env import CombatEnv

class TestEnv():
    def test_env(self):
        env = CombatEnv()
        obs = env.reset()
        print(obs)
        obs = env.step(0)
        print(obs)
