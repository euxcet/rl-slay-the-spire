import random
import numpy as np
from typing import Optional
import gymnasium as gym
from gymnasium.spaces import Discrete, Box, Dict
from ray.rllib.env.multi_agent_env import MultiAgentEnv
from ..game.slay_the_spire import SlayTheSpire
from ..game.observation.combat_observation import CombatObservation
from ..game.observation.choose_card_observation import ChooseCardObservation
from ..game.combat import Combat, random_combat
from ..game.combat import Act1EasyCombat, Act1BossCombat, Act1EliteCombat, Act1HardCombat
from ..game.character import Ironclad
from ..game.enemy import Cultist
from ..game.enemy.intent import intent_collection
from ..game.card import card_collection, CardTargetType, Deck
from ..game.enemy import enemy_collection
from ..game.enemy.intent import intent_collection
from ..game.effect import effect_collection, Effect


class SlayTheSpireEnv(MultiAgentEnv):

    dtype = np.float32

    MAX_HAND_CARDS = 10
    MAX_ENEMIES = 10
    MAX_CHARACTER_HP = 999
    MAX_ENEMY_HP = 999
    MAX_BLOCK = 999
    MAX_EFFECT_STACK = 999
    MAX_CARD_STEP = 4
    MAX_ENERGY = 5
    MAX_STEP = 300

    MAX_CHOOSE_CARD_OPTIONS = 5
    MAX_DECK_CARDS = 30

    def __init__(self, config: Optional[dict] = None) -> None:
        super().__init__()
        config = config or {}
        # self.possible_agents = ["combat_agent", "choose_room_agent", "event_agent", "choose_card_agent"]
        self.agents = self.possible_agents = ["combat_agent", "choose_card_agent"]
        self.observation_space = Dict({
            "combat_agent": Dict({
                "character_hp": Box(low=0, high=self.MAX_CHARACTER_HP, shape=(1,), dtype=self.dtype),
                "character_max_hp": Box(low=0, high=self.MAX_CHARACTER_HP, shape=(1,), dtype=self.dtype),
                "character_block": Box(low=0, high=self.MAX_BLOCK, shape=(1,), dtype=self.dtype),
                "character_effects": Box(low=0, high=self.MAX_EFFECT_STACK, shape=(len(effect_collection),), dtype=self.dtype),
                "hand_pile_id": Box(low=0, high=1, shape=(self.MAX_HAND_CARDS, len(card_collection)), dtype=self.dtype),
                "hand_pile_cost": Box(low=-1, high=self.MAX_ENERGY, shape=(self.MAX_HAND_CARDS,), dtype=self.dtype),
                "enemy_type": Box(low=0, high=1, shape=(self.MAX_ENEMIES, len(enemy_collection)), dtype=self.dtype),
                "enemy_hp": Box(low=0, high=self.MAX_ENEMY_HP, shape=(self.MAX_ENEMIES,), dtype=self.dtype),
                "enemy_block": Box(low=0, high=self.MAX_BLOCK, shape=(self.MAX_ENEMIES,), dtype=self.dtype),
                "enemy_effect": Box(low=0, high=self.MAX_EFFECT_STACK, shape=(self.MAX_ENEMIES, len(effect_collection)), dtype=self.dtype),
                "enemy_intent": Box(low=0, high=1, shape=(self.MAX_ENEMIES, len(intent_collection)), dtype=self.dtype),
                "playing_card": Box(low=0, high=1, shape=(len(card_collection),), dtype=self.dtype),
                "playing_card_step": Box(low=0, high=1, shape=(self.MAX_CARD_STEP,), dtype=self.dtype),
                "card_target_type": Box(low=0, high=1, shape=(len(CardTargetType),), dtype=self.dtype),
                "sum_enemies_attack": Box(low=0, high=self.MAX_CHARACTER_HP, shape=(1,), dtype=self.dtype),
                "action_mask": Box(low=0, high=1, shape=(Combat.MAX_ACTION,), dtype=self.dtype),
            }),
            "choose_card_agent": Dict({
                "character_hp": Box(low=0, high=self.MAX_CHARACTER_HP, shape=(1,), dtype=self.dtype),
                "character_max_hp": Box(low=0, high=self.MAX_CHARACTER_HP, shape=(1,), dtype=self.dtype),
                "deck": Box(low=0, high=1, shape=(self.MAX_DECK_CARDS, len(card_collection)), dtype=self.dtype),
                "options": Box(low=0, high=1, shape=(self.MAX_CHOOSE_CARD_OPTIONS, len(card_collection)), dtype=self.dtype),
                "action_mask": Box(low=0, high=1, shape=(self.MAX_CHOOSE_CARD_OPTIONS,), dtype=self.dtype)
            }),
        })
        self.action_space = Dict({
            "combat_agent": Discrete(Combat.MAX_ACTION),
            "choose_card_agent": Discrete(self.MAX_CHOOSE_CARD_OPTIONS),
        })
        self.last_obs = None
        self.hp_before_combat = 0

    def fix_shape(self, data: np.ndarray, target: list[int]) -> np.ndarray:
        while len(data.shape) < len(target):
            data = np.expand_dims(data, axis=-1)
        width = [(0, target[i] - data.shape[i]) for i in range(len(data.shape))]
        result = np.pad(data, width, mode='constant', constant_values=0.0)
        slices = tuple(slice(0, min(t, s)) for s, t in zip(result.shape, target))
        return result[slices]

    def to_effect_obs(self, effects: list[Effect]) -> np.ndarray:
        return effect_collection.tensor(
            [type(effect) for effect in effects],
            dtype=self.dtype,
            values=[effect.stack for effect in effects],
        )

    def to_env_obs(self, obs: CombatObservation | ChooseCardObservation) -> dict:
        if isinstance(obs, CombatObservation):
            return {
                "combat_agent": {
                    "character_hp": np.array([obs.character_hp], self.dtype),
                    "character_max_hp": np.array([obs.character_max_hp], self.dtype),
                    "character_block": np.array([obs.character_block], self.dtype),
                    "character_effects": self.to_effect_obs(obs.character_effects),
                    "hand_pile_id": self.fix_shape(np.array([card_collection.tensor([card]) for card in obs.hand_pile.cards], self.dtype), (self.MAX_HAND_CARDS, len(card_collection))),
                    "hand_pile_cost": self.fix_shape(np.array([-1 if card.cost == None else card.cost for card in obs.hand_pile.cards], self.dtype), (self.MAX_HAND_CARDS,)),
                    "enemy_type": self.fix_shape(np.array([enemy_collection.tensor([enemy]) for enemy in obs.enemies_type], self.dtype), (self.MAX_ENEMIES, len(enemy_collection))),
                    "enemy_hp": self.fix_shape(np.array(obs.enemies_hp, self.dtype), (self.MAX_ENEMIES,)),
                    "enemy_block": self.fix_shape(np.array(obs.enemies_block, self.dtype), (self.MAX_ENEMIES,)),
                    "enemy_effect": self.fix_shape(np.array([self.to_effect_obs(effects) for effects in obs.enemies_effects], self.dtype), (self.MAX_ENEMIES, len(effect_collection))),
                    "enemy_intent": self.fix_shape(np.array([intent_collection.tensor([intent]) for intent in obs.enemies_intent], self.dtype), (self.MAX_ENEMIES, len(intent_collection))),
                    "playing_card": card_collection.tensor([obs.playing_card], dtype=self.dtype),
                    "playing_card_step": np.zeros(self.MAX_CARD_STEP, self.dtype) if obs.playing_card is None else np.eye(self.MAX_CARD_STEP, dtype=self.dtype)[obs.playing_card.step],
                    "card_target_type": np.zeros(len(CardTargetType), self.dtype) if obs.playing_card is None else np.eye(len(CardTargetType), dtype=self.dtype)[obs.playing_card.target_type().value],
                    "sum_enemies_attack": np.array([obs.sum_enemies_attack], self.dtype),
                    "action_mask": obs.action_mask.astype(self.dtype),
                }
            }
        elif isinstance(obs, ChooseCardObservation):
            return {
                "choose_card_agent": {
                    "character_hp": np.array([obs.character_hp], self.dtype),
                    "character_max_hp": np.array([obs.character_max_hp], self.dtype),
                    "deck": self.fix_shape(np.array([card_collection.tensor([card]) for card in obs.deck], self.dtype), (self.MAX_DECK_CARDS, len(card_collection))),
                    "options": self.fix_shape(np.array([card_collection.tensor([card]) for card in obs.options], self.dtype), (self.MAX_CHOOSE_CARD_OPTIONS, len(card_collection))),
                    "action_mask": self.fix_shape(obs.action_mask, (self.MAX_CHOOSE_CARD_OPTIONS,)).astype(self.dtype),
                }
            }

    def reset(self, *, seed = None, options = None) -> tuple:
        random.seed(seed)
        self.num_step = 0
        self.game = SlayTheSpire()
        obs = self.game.reset()
        return self.to_env_obs(obs), {"env_state": "reset"}

    def step(self, action: dict) -> tuple:
        assert len(action) == 1
        self.num_step += 1
        for k, v in action.items():
            obs = self.game.step(v)
        terminated = {"__all__": obs.is_over}
        truncated = {}
        infos = {}

        # combat start
        if isinstance(obs, CombatObservation) and (self.last_obs == None or not isinstance(self.last_obs, CombatObservation)):
            self.hp_before_combat = obs.character_hp

        combat_reward = choose_card_reward = 0
        if isinstance(obs, CombatObservation):
            combat_reward = -obs.character_hp_lost / obs.character_max_hp
        # combat end
        if not isinstance(obs, CombatObservation) and isinstance(self.last_obs, CombatObservation):
            choose_card_reward = (obs.character_hp - self.hp_before_combat) / obs.character_max_hp
        reward = {"combat_agent": combat_reward, "choose_card_agent": choose_card_reward}

        self.last_obs = obs

        if self.num_step > self.MAX_STEP:
            reward = -2
            terminated = True
            truncated = True

        return self.to_env_obs(obs), reward, terminated, truncated, infos
