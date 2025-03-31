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
        len_episode = 0
        episode_return = 0
        history = []

        while True:
            action_mask = obs['action_mask']
            action = random.choice([i for i in range(len(action_mask)) if action_mask[i] > 0])
            history.append(env.game.observe().rich())
            history.append(action)
            # obs, reward, terminated, truncated, _ = env.step(action)
            try:
                obs, reward, terminated, truncated, _ = env.step(action)
            except Exception as e:
                for h in history[-10:]:
                    console.print(h)
                raise e
                # print('Exception', e)

            episode_return += reward
            len_episode += 1
            # if len_episode > 100:
            #     for h in history[:30]:
            #         console.print(h)
            #     print('Too many steps')
            #     break
            if terminated or truncated:
                print(f"Episode[{num_episodes}] done. Total reward = {episode_return} Length = {len_episode}")
                obs, info = env.reset()
                num_episodes += 1
                episode_return = 0
                len_episode = 0
                history = []
