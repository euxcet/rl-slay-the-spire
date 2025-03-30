import torch
from torch.nn import Linear, ReLU
from ray.rllib.core.columns import Columns
from ray.rllib.core.rl_module.torch.torch_rl_module import TorchRLModule
from ray.rllib.core.rl_module.apis.value_function_api import ValueFunctionAPI
from ray.rllib.utils.torch_utils import FLOAT_MIN
from ray.rllib.utils.annotations import override

class CombatModule(TorchRLModule, ValueFunctionAPI):

    @override(TorchRLModule)
    def setup(self) -> None:
        input_dim = 2277
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
            Linear(128, 1),
        )

    def _get_input_tensor(self, batch):
        obs = batch[Columns.OBS]

        character_hp: torch.Tensor = obs['character_hp']
        # character_max_hp: torch.Tensor = obs['character_max_hp']
        character_block: torch.Tensor = obs['character_block']
        character_effects: torch.Tensor = obs['character_effects']
        hand_pile_id: torch.Tensor = obs['hand_pile_id']
        hand_pile_cost: torch.Tensor = obs['hand_pile_cost']
        enemy_type: torch.Tensor = obs['enemy_type']
        enemy_hp: torch.Tensor = obs['enemy_hp']
        # enemy_max_hp: torch.Tensor = obs['enemy_max_hp']
        enemy_block: torch.Tensor = obs['enemy_block']
        enemy_effect: torch.Tensor = obs['enemy_effect']
        enemy_intent: torch.Tensor = obs['enemy_intent']
        playing_card: torch.Tensor = obs['playing_card']
        playing_card_step: torch.Tensor = obs['playing_card_step']
        card_target_type: torch.Tensor = obs['card_target_type']

        #     "character_hp": (1,),
        #     "character_max_hp": (1,),
        #     "character_block": (1,),
        #     "character_effects": (9,),
        #     "hand_pile_id": (10, 5),
        #     "hand_pile_cost": (10,),
        #     "enemy_type": (10, 10),
        #     "enemy_hp": (10,),
        #     "enemy_max_hp": (10,),
        #     "enemy_block": (10,),
        #     "enemy_effect": (10, 9),
        #     "enemy_intent": (10, 20),
        #     "playing_card": (5,),
        #     "playing_card_step": (4,),
        #     "card_target_type": (5,),
        #     "action_mask": (10,)

        input_tensor = torch.cat((
            character_hp.flatten(start_dim=1),
            # character_max_hp.flatten(start_dim=1),
            character_block.flatten(start_dim=1),
            character_effects.flatten(start_dim=1),
            hand_pile_id.flatten(start_dim=1),
            hand_pile_cost.flatten(start_dim=1),
            enemy_type.flatten(start_dim=1),
            enemy_hp.flatten(start_dim=1),
            # enemy_max_hp.flatten(start_dim=1),
            enemy_block.flatten(start_dim=1),
            enemy_effect.flatten(start_dim=1),
            enemy_intent.flatten(start_dim=1),
            playing_card.flatten(start_dim=1),
            playing_card_step.flatten(start_dim=1),
            card_target_type.flatten(start_dim=1),
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
