# core
import gymnasium
import pybullet
from PyFlyt.core import Aviary
import pybullet as pb
# utility
import wheel
# math
import numpy as np
# gymnasium
import gymnasium as gym
import PyFlyt.gym_envs
from PyFlyt.gym_envs.quadx_envs.quadx_hover_env import QuadXHoverEnv
# types
from gymnasium import Env
from typing import *



if __name__ == "__main__":
    start_pos = np.array([[0.0, 0.0, 1.0]])
    start_orn = np.array([[0.0, 0.0, 0.0]])

    env = Aviary(start_pos=start_pos, start_orn=start_orn, render=True, drone_type="quadx")
    env.set_mode(7)

    projectile_mass: float = 1.0
    projectile_radius: float = 0.1
    start_position: List[int] = [0,0,5]

    shape_id = pb.createCollisionShape(
        shapeType = pybullet.GEOM_SPHERE,
        radius = projectile_radius
    )

    # Watermelon

    projectile_id = pb.createMultiBody(
        baseMass = projectile_mass,
        baseCollisionShapeIndex = shape_id,
        basePosition = start_position
    )

    # this is a green watermelon
    pb.changeVisualShape(
        objectUniqueId = projectile_id,
        linkIndex = -1,
        rgbaColor = [0,1,0,1]
    )



    termination: bool = False
    truncation: bool = False

    for i in range(1000):
        env.step()