from ray import tune
from ray.rllib.utils.test_utils import (
    add_rllib_example_script_args,
    run_rllib_example_script_experiment,
)
from ray.tune.registry import get_trainable_cls

parser = add_rllib_example_script_args(
    default_iters=50, default_reward=180, default_timesteps=100000
)
parser.set_defaults(
    enable_new_api_stack=True,
    num_env_runners=2,
)


if __name__ == "__main__":
    args = parser.parse_args()

    base_config = (
        get_trainable_cls(args.algo)
        .get_default_config()
        # This script only works on the new API stack.
        .api_stack(
            enable_rl_module_and_learner=True,
            enable_env_runner_and_connector_v2=True,
        )
        .environment("CartPole-v1")
        # Define EnvRunner scaling.
        .env_runners(num_env_runners=args.num_env_runners)
        # Define Learner scaling.
        .learners(
            # How many Learner workers do we need? If you have more than 1 GPU,
            # set this parameter to the number of GPUs available.
            num_learners=args.num_learners,
            # How many GPUs does each Learner need? If you have more than 1 GPU or only
            # one Learner, you should set this to 1, otherwise, set this to some
            # fraction.
            num_gpus_per_learner=args.num_gpus_per_learner,
        )
        # 4 tune trials altogether.
        .training(lr=tune.grid_search([0.005, 0.003, 0.001, 0.0001]))
    )

    run_rllib_example_script_experiment(base_config, args, keep_config=True)