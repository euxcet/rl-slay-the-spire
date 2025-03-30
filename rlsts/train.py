import os
import ray
from ray import tune
from ray.rllib.core.rl_module.rl_module import RLModuleSpec
from ray.tune import CLIReporter
from ray.rllib.algorithms.ppo import PPOConfig
from ray.rllib.utils.metrics import (
    DIFF_NUM_GRAD_UPDATES_VS_SAMPLER_POLICY,
    ENV_RUNNER_RESULTS,
    ENV_RUNNER_RESULTS,
    EPISODE_RETURN_MEAN,
    FAULT_TOLERANCE_STATS,
    EVALUATION_RESULTS,
    LEARNER_RESULTS,
    NUM_ENV_STEPS_TRAINED,
    NUM_ENV_STEPS_SAMPLED_LIFETIME,
    TIMERS,
)
from ray.tune.result import TRAINING_ITERATION

from .env.combat_env import CombatEnv
from .module.combat_module import CombatModule

def train():
    ray.init(num_cpus=4, ignore_reinit_error=True)
    config = (
        PPOConfig()
        .framework("torch")
        .environment(CombatEnv)
        .api_stack(
            enable_rl_module_and_learner=True,
            enable_env_runner_and_connector_v2=True,
        )
        .env_runners(
            num_env_runners=1,
            num_envs_per_env_runner=1,
        )
        .learners(
            num_learners=1,
            num_gpus_per_learner=0,
        )
        .rl_module(
            rl_module_spec=RLModuleSpec(
                module_class=CombatModule,
                model_config={},
            ),
        )
        .training(
            train_batch_size=8192,
            minibatch_size=128,
            entropy_coeff=0.01,
            kl_coeff=0.2,
            kl_target=0.004,
        )
    )
    os.environ["RAY_AIR_NEW_OUTPUT"] = "0"

    progress_reporter = CLIReporter(
        metric_columns={
            **{
                TRAINING_ITERATION: "iter",
                "time_total_s": "total time (s)",
                NUM_ENV_STEPS_SAMPLED_LIFETIME: "ts",
                f"{ENV_RUNNER_RESULTS}/{EPISODE_RETURN_MEAN}": "combined return",
            },
            **{
                (
                    f"{ENV_RUNNER_RESULTS}/module_episode_returns_mean/" f"{pid}"
                ): f"return {pid}"
                for pid in config.policies
            },
        },
    )

    results = tune.Tuner(
        "PPO",
        param_space=config,
        run_config=tune.RunConfig(
            stop= {
                "training_iteration": 1000,
            },
            verbose=True,
            callbacks=[],
            checkpoint_config=tune.CheckpointConfig(
                checkpoint_frequency=1,
                checkpoint_at_end=True,
            ),
            progress_reporter=progress_reporter,
        ),
        tune_config=tune.TuneConfig(
            num_samples=1,
            max_concurrent_trials=None,
            scheduler=None,
        ),
    ).fit()
    ray.shutdown()

if __name__ == "__main__":
    train()