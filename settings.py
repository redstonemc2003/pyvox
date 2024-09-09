from numba import njit
import numpy as np
import glm
import math

# Window 
WIN_RES = glm.vec2(960, 640)
WIN_COLOR = glm.vec3(255, 255, 255)

# Camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# Player
PLAYER_SPEED = 0.005
PLAYER_ROTATION_SPEED = 0.003 
PLAYER_POS = glm.vec3(0,0,1)
MOUSE_SENSTIVITY = 0.002