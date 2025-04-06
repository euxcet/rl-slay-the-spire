import os
import torch
import numpy as np
from rich.console import Console
from rlsts.game.slay_the_spire import SlayTheSpire
from rlsts.env.combat_env import CombatEnv

from ray.rllib.core import DEFAULT_MODULE_ID
from ray.rllib.core.columns import Columns
from ray.rllib.core.rl_module.rl_module import RLModule
from ray.rllib.utils.checkpoints import Checkpointable
from ray.rllib.utils.numpy import convert_to_numpy, softmax

class TestEnv():

    def get_nearest_checkpoint(self, root: str):
        for run in sorted(os.listdir(root), reverse=True):
            if run.startswith('PPO'):
                for folder in os.listdir(os.path.join(root, run)):
                    if folder.startswith('PPO'):
                        for checkpoint in sorted(os.listdir(os.path.join(root, run, folder)), reverse=True):
                            if checkpoint.startswith('checkpoint'):
                                return os.path.join(root, run, folder, checkpoint)

    def test_env(self):
        console = Console()
        result_root = '/Users/euxcet/ray_results/'
        checkpoint_path = self.get_nearest_checkpoint(result_root)
        print(checkpoint_path)

        combat_module: Checkpointable = RLModule.from_checkpoint(
            os.path.join(
                checkpoint_path,
                "learner_group",
                "learner",
                "rl_module",
                DEFAULT_MODULE_ID,
            )
        )

        num_episodes_during_inference = 1
        num_episodes = 0
        episode_return = 0.0

        env = CombatEnv()
        obs, info = env.reset()

        while num_episodes < num_episodes_during_inference:
            module_input = {
                Columns.OBS: {
                    k: torch.from_numpy(v).unsqueeze(0)
                    for k, v in obs.items()
                }
            }
            module_out = combat_module.forward(module_input)
            logits = convert_to_numpy(module_out[Columns.ACTION_DIST_INPUTS])
            action = np.random.choice(env.action_space.n, p=softmax(logits[0]))

            console.log(env.game.observe().rich())
            print(module_input[Columns.OBS]['action_mask'])
            console.log('Action:', action)

            obs, reward, terminated, truncated, _ = env.step(action)
            episode_return += reward
            if terminated or truncated:
                print(f"Episode done. Total reward = {episode_return}")
                obs, info = env.reset()
                num_episodes += 1
                episode_return = 0
