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
            "character_hp": Box(low=0, high=self.MAX_CHARACTER_HP, shape=(1,), dtype=np.int32),
            "character_max_hp": Box(low=0, high=self.MAX_CHARACTER_HP, shape=(1,), dtype=np.int32),
            "character_block": Box(low=0, high=self.MAX_BLOCK, shape=(1,), dtype=np.int32),
            "character_effects": Box(low=0, high=self.MAX_EFFECT_STACK, shape=(len(effect_collection),), dtype=np.int32),
            "hand_pile_id": Box(low=0, high=1, shape=(self.MAX_NUM_HAND_CARDS, len(card_collection)), dtype=np.int32),
            "hand_pile_energy": Box(low=0, high=self.MAX_ENERGY, shape=(self.MAX_NUM_HAND_CARDS,), dtype=np.int32),
            "enemy_type": Box(low=0, high=1, shape=(self.MAX_NUM_ENEMIES, len(enemy_collection)), dtype=np.int32),
            "enemy_hp": Box(low=0, high=self.MAX_ENEMY_HP, shape=(self.MAX_NUM_ENEMIES, 1), dtype=np.int32),
            "enemy_max_hp": Box(low=0, high=self.MAX_ENEMY_HP, shape=(self.MAX_NUM_ENEMIES, 1), dtype=np.int32),
            "enemy_block": Box(low=0, high=self.MAX_BLOCK, shape=(self.MAX_NUM_ENEMIES, 1), dtype=np.int32),
            "enemy_effect": Box(low=0, high=self.MAX_EFFECT_STACK, shape=(self.MAX_NUM_ENEMIES, len(effect_collection)), dtype=np.int32),
            "enemy_intent": Box(low=0, high=1, shape=(self.MAX_NUM_ENEMIES, len(intent_collection)), dtype=np.int32),
            "playing_card": Box(low=0, high=1, shape=(len(card_collection),), dtype=np.int32),
            "playing_card_step": Box(low=0, high=1, shape=(self.MAX_CARD_STEP,), dtype=np.int32),
            "card_target_type": Box(low=0, high=1, shape=(len(CardTargetType),), dtype=np.int32),
            # TODO: relic, potion
        })
        self.action_space = Discrete(50)

    def to_effect_obs(self, effects: list[Effect]) -> np.ndarray:
        return effect_collection.tensor(
            [type(effect) for effect in effects],
            dtype=np.int32,
            values=[effect.stack for effect in effects],
        )

    def to_env_obs(self, obs: CombatObservation) -> dict:
        return {
            "character_hp": np.array([obs.character_hp], np.int32),
            "character_max_hp": np.array([obs.character_max_hp], np.int32),
            "character_block": np.array([obs.character_block], np.int32),
            "character_effects": self.to_effect_obs(obs.character_effects),
            # "hand_pile_id": ,
            # "hand_pile_energy": ,
            "enemy_type": np.array([enemy_collection.tensor([enemy]) for enemy in obs.enemies_type], np.int32),
            "enemy_hp": np.array(obs.enemies_hp, np.int32),
            "enemy_max_hp": np.array(obs.enemies_max_hp, np.int32),
            "enemy_block": np.array(obs.enemies_block, np.int32),
            "enemy_effect": np.array([self.to_effect_obs(effects) for effects in obs.enemies_effects], np.int32),
            "enemy_intent": np.array([intent_collection.tensor([intent]) for intent in obs.enemies_intent], np.int32),
            "playing_card": card_collection.tensor([obs.playing_card]),
            "playing_card_step": np.zeros(self.MAX_CARD_STEP, np.int32) if obs.playing_card is None else np.eye(self.MAX_CARD_STEP)[obs.playing_card.step],
            "card_target_type": np.zeros(len(CardTargetType), np.int32) if obs.playing_card is None else np.eye(len(CardTargetType))[obs.playing_card.target_type()]
        }
        ...

    def reset(self, *, seed = None, options = None) -> None:
        random.seed(seed)
        obs = self.game.reset()
        return self.to_env_obs(obs)

    def step(self, action: int) -> None:
        obs = self.game.step(action)
        return self.to_env_obs(obs)
