import torch
from torch.nn import Linear, ReLU
from ray.rllib.core.columns import Columns
from ray.rllib.core.rl_module.torch.torch_rl_module import TorchRLModule
from ray.rllib.core.rl_module.apis.value_function_api import ValueFunctionAPI
from ray.rllib.utils.annotations import override

class CombatModule(TorchRLModule, ValueFunctionAPI):

    @override(TorchRLModule)
    def setup(self) -> None:
        input_dim = 506
        output_dim = self.action_space.n
        self._policy_net = torch.nn.Sequential(
            Linear(input_dim, 128),
            ReLU(),
            Linear(128, output_dim),
        )
        self._value_net = torch.nn.Sequential(
            Linear(input_dim, 128),
            ReLU(),
            Linear(128, 1),
        )

    def get_input_tensor(self, batch):
        obs = batch[Columns.OBS]
        character_hp: torch.Tensor = obs['character_hp']
        character_max_hp: torch.Tensor = obs['character_max_hp']
        character_block: torch.Tensor = obs['character_block']
        character_effects: torch.Tensor = obs['character_effects']
        hand_pile_id: torch.Tensor = obs['hand_pile_id']
        hand_pile_cost: torch.Tensor = obs['hand_pile_cost']
        enemy_type: torch.Tensor = obs['enemy_type']
        enemy_hp: torch.Tensor = obs['enemy_hp']
        enemy_max_hp: torch.Tensor = obs['enemy_max_hp']
        enemy_block: torch.Tensor = obs['enemy_block']
        enemy_effect: torch.Tensor = obs['enemy_effect']
        enemy_intent: torch.Tensor = obs['enemy_intent']
        playing_card: torch.Tensor = obs['playing_card']
        playing_card_step: torch.Tensor = obs['playing_card_step']
        card_target_type: torch.Tensor = obs['card_target_type']

        input_tensor = torch.cat((
            character_hp.flatten(start_dim=1),
            character_max_hp.flatten(start_dim=1),
            character_block.flatten(start_dim=1),
            character_effects.flatten(start_dim=1),
            hand_pile_id.flatten(start_dim=1),
            hand_pile_cost.flatten(start_dim=1),
            enemy_type.flatten(start_dim=1),
            enemy_hp.flatten(start_dim=1),
            enemy_max_hp.flatten(start_dim=1),
            enemy_block.flatten(start_dim=1),
            enemy_effect.flatten(start_dim=1),
            enemy_intent.flatten(start_dim=1),
            playing_card.flatten(start_dim=1),
            playing_card_step.flatten(start_dim=1),
            card_target_type.flatten(start_dim=1),
        ), dim=1)
        return input_tensor

    @override(TorchRLModule)
    def _forward(self, batch, **kwargs) -> None:
        action_logits = self._policy_net(self.get_input_tensor(batch))
        return { Columns.ACTION_DIST_INPUTS: action_logits }

    @override(ValueFunctionAPI)
    def compute_values(self, batch, **kwargs):
        v = self._value_net(self.get_input_tensor(batch)).squeeze(-1)
        return v
