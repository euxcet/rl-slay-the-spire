import random
import numpy as np
from rich.console import Console
from rlsts.env.combat_env import CombatEnv

from ray.rllib.core import DEFAULT_MODULE_ID
from ray.rllib.core.columns import Columns
from ray.rllib.utils.numpy import convert_to_numpy, softmax

class TestRandomAction():

    def test_env(self):
        console = Console()
        env = CombatEnv()
        obs, info = env.reset()
        num_episodes = 0
        episode_return = 0

        while True:
            action_mask = obs['action_mask']
            action = random.choice([i for i in range(len(action_mask)) if action_mask[i] > 0])
            obs, reward, terminated, truncated, _ = env.step(action)
            episode_return += reward
            if terminated or truncated:
                print(f"Episode[{num_episodes}] done. Total reward = {episode_return}")
                obs, info = env.reset()
                num_episodes += 1
                episode_return = 0
