import gymnasium as gym
from gymnasium.spaces import Discrete, Box, Dict
import numpy as np
import random
from typing import Optional
from ..game.combat import Combat, CombatObservation
from ..game.character import Ironclad
from ..game.enemy import Cultist
from ..game.enemy.intent import intent_collection
from ..game.card import card_collection, CardTargetType
from ..game.enemy import enemy_collection
from ..game.enemy.intent import intent_collection
from ..game.effect import effect_collection, Effect


class CombatEnv(gym.Env):
    MAX_NUM_HAND_CARDS = 10
    MAX_NUM_ENEMIES = 10
    MAX_CHARACTER_HP = 999
    MAX_ENEMY_HP = 999
    MAX_BLOCK = 999
    MAX_EFFECT_STACK = 999
    MAX_CARD_STEP = 4
    MAX_ENERGY = 5

    def __init__(self, config: Optional[dict] = None) -> None:
        config = config or {}
        self.game = Combat(Ironclad(), [Cultist()])
        self.observation_space = Dict({
            "character_hp": Box(low=0, high=self.MAX_CHARACTER_HP, shape=(1,), dtype=np.float32),
            "character_max_hp": Box(low=0, high=self.MAX_CHARACTER_HP, shape=(1,), dtype=np.float32),
            "character_block": Box(low=0, high=self.MAX_BLOCK, shape=(1,), dtype=np.float32),
            "character_effects": Box(low=0, high=self.MAX_EFFECT_STACK, shape=(len(effect_collection),), dtype=np.float32),
            "hand_pile_id": Box(low=0, high=1, shape=(self.MAX_NUM_HAND_CARDS, len(card_collection)), dtype=np.float32),
            "hand_pile_cost": Box(low=0, high=self.MAX_ENERGY, shape=(self.MAX_NUM_HAND_CARDS,), dtype=np.float32),
            "enemy_type": Box(low=0, high=1, shape=(self.MAX_NUM_ENEMIES, len(enemy_collection)), dtype=np.float32),
            "enemy_hp": Box(low=0, high=self.MAX_ENEMY_HP, shape=(self.MAX_NUM_ENEMIES,), dtype=np.float32),
            "enemy_max_hp": Box(low=0, high=self.MAX_ENEMY_HP, shape=(self.MAX_NUM_ENEMIES,), dtype=np.float32),
            "enemy_block": Box(low=0, high=self.MAX_BLOCK, shape=(self.MAX_NUM_ENEMIES,), dtype=np.float32),
            "enemy_effect": Box(low=0, high=self.MAX_EFFECT_STACK, shape=(self.MAX_NUM_ENEMIES, len(effect_collection)), dtype=np.float32),
            "enemy_intent": Box(low=0, high=1, shape=(self.MAX_NUM_ENEMIES, len(intent_collection)), dtype=np.float32),
            "playing_card": Box(low=0, high=1, shape=(len(card_collection),), dtype=np.float32),
            "playing_card_step": Box(low=0, high=1, shape=(self.MAX_CARD_STEP,), dtype=np.float32),
            "card_target_type": Box(low=0, high=1, shape=(len(CardTargetType),), dtype=np.float32),
        })
        self.action_space = Discrete(50)

    def pad(self, data: np.ndarray, target: list[int]) -> np.ndarray:
        while len(data.shape) < len(target):
            data = np.expand_dims(data, axis=-1)
        width = [(0, target[i] - data.shape[i]) for i in range(len(data.shape))]
        return np.pad(data, width, mode='constant', constant_values=0.0)

    def to_effect_obs(self, effects: list[Effect]) -> np.ndarray:
        return effect_collection.tensor(
            [type(effect) for effect in effects],
            dtype=np.float32,
            values=[effect.stack for effect in effects],
        )

    def to_env_obs(self, obs: CombatObservation) -> dict:
        return {
            "character_hp": np.array([obs.character_hp], np.float32),
            "character_max_hp": np.array([obs.character_max_hp], np.float32),
            "character_block": np.array([obs.character_block], np.float32),
            "character_effects": self.to_effect_obs(obs.character_effects),
            "hand_pile_id": self.pad(np.array([card_collection.tensor([card]) for card in obs.hand_pile.cards], np.float32), (self.MAX_NUM_HAND_CARDS, len(card_collection))),
            "hand_pile_cost": self.pad(np.array([card.cost for card in obs.hand_pile.cards], np.float32), (self.MAX_NUM_HAND_CARDS,)),
            "enemy_type": self.pad(np.array([enemy_collection.tensor([enemy]) for enemy in obs.enemies_type], np.float32), (self.MAX_NUM_ENEMIES, len(enemy_collection))),
            "enemy_hp": self.pad(np.array(obs.enemies_hp, np.float32), (self.MAX_NUM_ENEMIES,)),
            "enemy_max_hp": self.pad(np.array(obs.enemies_max_hp, np.float32), (self.MAX_NUM_ENEMIES,)),
            "enemy_block": self.pad(np.array(obs.enemies_block, np.float32), (self.MAX_NUM_ENEMIES,)),
            "enemy_effect": self.pad(np.array([self.to_effect_obs(effects) for effects in obs.enemies_effects], np.float32), (self.MAX_NUM_ENEMIES, len(effect_collection))),
            "enemy_intent": self.pad(np.array([intent_collection.tensor([intent]) for intent in obs.enemies_intent], np.float32), (self.MAX_NUM_ENEMIES, len(intent_collection))),
            "playing_card": card_collection.tensor([obs.playing_card], dtype=np.float32),
            "playing_card_step": np.zeros(self.MAX_CARD_STEP, np.float32) if obs.playing_card is None else np.eye(self.MAX_CARD_STEP, dtype=np.float32)[obs.playing_card.step],
            "card_target_type": np.zeros(len(CardTargetType), np.float32) if obs.playing_card is None else np.eye(len(CardTargetType), dtype=np.float32)[obs.playing_card.target_type().value],
        }

    def reset(self, *, seed = None, options = None) -> dict:
        random.seed(seed)
        obs = self.game.reset()
        return self.to_env_obs(obs), {"env_state": "reset"}

    def step(self, action: int) -> dict:
        obs = self.game.step(action)
        reward = -obs.character_hp_lost
        terminated = obs.is_over
        truncated = obs.is_over
        infos = {}
        
        valid = {
            "character_hp": (1,),
            "character_max_hp": (1,),
            "character_block": (1,),
            "character_effects": (9,),
            "hand_pile_id": (10, 5),
            "hand_pile_cost": (10,),
            "enemy_type": (10, 10),
            "enemy_hp": (10,),
            "enemy_max_hp": (10,),
            "enemy_block": (10,),
            "enemy_effect": (10, 9),
            "enemy_intent": (10, 20),
            "playing_card": (5,),
            "playing_card_step": (4,),
            "card_target_type": (5,),
        }

        print(reward)
        for k, v in self.to_env_obs(obs).items():
            if v.shape != valid[k]:
                print(k, v.shape, obs.is_over, self.game.enemies)
        return (self.to_env_obs(obs), reward, terminated, truncated, infos)
