import pygame
#screen settings
FPS = 60
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = 600
HALF_HEIGHT = 400
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

#player setting
P_SPEED = 5
angle = 0
x_pos = 10
y_pos = 10
x_size = 50
y_size = 50
r_size = 25
rline = 0

#square100
x_pos2 = 100 
y_pos2 = 100
x_size2 = 100
y_size2 = 100