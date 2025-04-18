import torch
from torch.nn import Linear, ReLU
from ray.rllib.core.columns import Columns
from ray.rllib.core.rl_module.multi_rl_module import MultiRLModule
from ray.rllib.core.rl_module.torch.torch_rl_module import TorchRLModule
from ray.rllib.core.rl_module.apis.value_function_api import ValueFunctionAPI
from ray.rllib.utils.torch_utils import FLOAT_MIN
from ray.rllib.utils.annotations import override

class SlayTheSpireModule(MultiRLModule):
    def setup(self):
        rl_modules = {}
        for module_id, module_spec in self.config.modules.items():
            rl_modules[module_id] = module_spec.module_class(
                config=self.config.modules[module_id].get_rl_module_config(),
            )
        self._rl_modules = rl_modules
