import torch
from torch.nn import Linear, ReLU
from ray.rllib.core.columns import Columns
from ray.rllib.core.rl_module.torch.torch_rl_module import TorchRLModule
from ray.rllib.core.rl_module.apis.value_function_api import ValueFunctionAPI
from ray.rllib.utils.torch_utils import FLOAT_MIN
from ray.rllib.utils.annotations import override

class ChooseCardModule(TorchRLModule, ValueFunctionAPI):

    @override(TorchRLModule)
    def setup(self) -> None:
        input_dim = 5957
        output_dim = self.action_space.n
        self._policy_net = torch.nn.Sequential(
            Linear(input_dim, 128),
            ReLU(),
            Linear(128, 64),
            ReLU(),
            Linear(64, 32),
            ReLU(),
            Linear(32, output_dim),
        )
        self._value_net = torch.nn.Sequential(
            Linear(input_dim, 128),
            ReLU(),
            Linear(128, 64),
            ReLU(),
            Linear(64, 32),
            ReLU(),
            Linear(32, 1),
        )

    def _get_input_tensor(self, batch):
        obs = batch[Columns.OBS]
        character_hp: torch.Tensor = obs['character_hp']
        character_max_hp: torch.Tensor = obs['character_max_hp']
        deck: torch.Tensor = obs['deck']
        options: torch.Tensor = obs['options']
        action_mask: torch.Tensor = obs['action_mask']

        input_tensor = torch.cat((
            character_hp.flatten(start_dim=1),
            character_max_hp.flatten(start_dim=1),
            deck.flatten(start_dim=1),
            options.flatten(start_dim=1),
            action_mask.flatten(start_dim=1),
        ), dim=1)
        return input_tensor, obs['action_mask']

    def _mask_action_logits(self, batch: dict, action_mask: torch.Tensor) -> dict:
        inf_mask = torch.clamp(torch.log(action_mask), min=FLOAT_MIN)
        batch[Columns.ACTION_DIST_INPUTS] += inf_mask
        return batch

    @override(TorchRLModule)
    def _forward(self, batch, **kwargs) -> None:
        input_tensor, action_mask = self._get_input_tensor(batch)
        action_logits = self._policy_net(input_tensor)
        return self._mask_action_logits({ Columns.ACTION_DIST_INPUTS: action_logits }, action_mask)

    @override(ValueFunctionAPI)
    def compute_values(self, batch, **kwargs):
        input_tensor, _ = self._get_input_tensor(batch)
        v = self._value_net(input_tensor).squeeze(-1)
        return v
