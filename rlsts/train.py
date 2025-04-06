import os
import ray
import fire
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

def _train(
    num_env_runners: int = 1,
    num_envs_per_env_runner: int = 1,
    num_cpus_per_env_runner: int | float = 1,
    num_gpus_per_env_runner: int | float = 0.05,
    num_learners: int = 1,
    num_cpus_per_learner: int | float | str = 1,
    num_gpus_per_learner: int | float = 0,
    train_batch_size: int = 16384,
    minibatch_size: int = 128,
    entropy_coeff: float = 0.01,
    kl_coeff: float = 0.2,
    kl_target: float = 0.004,
    training_iteration: int = 10000,
) -> None:
    ray.init(ignore_reinit_error=True)
    config = (
        PPOConfig()
        .framework("torch")
        .environment(CombatEnv)
        .api_stack(
            enable_rl_module_and_learner=True,
            enable_env_runner_and_connector_v2=True,
        )
        .env_runners(
            num_env_runners=num_env_runners,
            num_envs_per_env_runner=num_envs_per_env_runner,
            num_cpus_per_env_runner=num_cpus_per_env_runner,
            num_gpus_per_env_runner=num_gpus_per_env_runner,
        )
        .learners(
            num_learners=num_learners,
            num_cpus_per_learner=num_cpus_per_learner,
            num_gpus_per_learner=num_gpus_per_learner,
        )
        .rl_module(
            rl_module_spec=RLModuleSpec(
                module_class=CombatModule,
                model_config={},
            ),
        )
        .training(
            train_batch_size=train_batch_size,
            minibatch_size=minibatch_size,
            entropy_coeff=entropy_coeff,
            kl_coeff=kl_coeff,
            kl_target=kl_target,
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
                "training_iteration": training_iteration,
            },
            verbose=True,
            callbacks=[],
            checkpoint_config=tune.CheckpointConfig(
                checkpoint_frequency=25,
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

def train():
    fire.Fire(_train)

if __name__ == "__main__":
    fire.Fire(_train)