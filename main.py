import gymnasium
from PyFlyt.core import Aviary
# utility
import wheel
# math
import numpy as np
# gymnasium
import gymnasium as gym
import PyFlyt.gym_envs
# types
from gymnasium import Env



if __name__ == "__main__":
    env: Env = gymnasium.make("PyFlyt/QuadX-Hover-v4", render_mode="human")
    obs = env.reset()

    termination: bool = False
    truncation: bool = False

    while not termination or truncation:
        observation, reward, termination, truncation, info = env.step(env.action_space.sample())