import pygame
import math
#screen settings
FPS = 15
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = 600
HALF_HEIGHT = 400
DIOGONAL = math.sqrt(WIDTH**2 + HEIGHT**2)
sc = pygame.display.set_mode((WIDTH, HEIGHT))

#color palette
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (128, 255, 0)

PURPLE = (255, 0, 255)
PINK = (255, 0, 128)
LIGHT_PURPLE = (128, 0, 255)

#square100
x_pos2 = 100 
y_pos2 = 100
x_size2 = 100
y_size2 = 100

#player setting
P_SPEED = 5
angle = 0
x_pos = HALF_WIDTH
y_pos = HALF_HEIGHT
x_size = 50
y_size = 50
r_size = 25

#player camera (ray casting)
rline = 0
fov_lines = 90
fov_angle = 45
fov_abc = 1
dist = fov_lines / 2 * math.tan(fov_angle)
PROJ_COEF = dist * x_size2 * 6
SCALE = WIDTH / fov_lines
