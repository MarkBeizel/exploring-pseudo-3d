import pygame
import math
#screen settings
FPS = 30
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = 600
HALF_HEIGHT = 400
DIOGONAL = math.sqrt(WIDTH**2 + HEIGHT**2) + 1
#DIOGONAL = 1442.22051
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

#obj30
x_size3 = 20
y_size3 = 20


#player setting
P_SPEED = 5
angle = math.radians(90)
x_pos = x_size2 * 2.5
y_pos = y_size2 * 1.5
x_size = 50
y_size = 50
r_size = 25
rline = 0
 
#player camera (ray casting)
k = math.radians(2)
q = 10
fov_lines = int(WIDTH / q) # = 120
fov_angle = math.radians(60) / 2
fov_abr = (fov_angle*2) / fov_lines
dist = fov_lines / (2 * math.tan(fov_angle))
PROJ_COEF = dist * x_size2 * q
PROJ_COEF_OBJ = dist * x_size3 * q
SCALE = WIDTH / fov_lines
