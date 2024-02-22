import pygame
import math
from settings import *

class Player:
    def __init__(self):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle

    def move(self, x = 0, y = 0):
        self.x_pos += x * P_SPEED
        self.y_pos += y * P_SPEED
    
    def rotate(self, a):
        self.angle += a 

    def draw(self):
        pygame.draw.circle(sc, (LIGHT_PURPLE), (self.x_pos, self.y_pos), (r_size), (rline))
        #pygame.draw.circle(screen, (LIGHT_PURPLE, YELLOW), (self.x_pos, self.y_pos, r_size, rline))

    def line(self):
        pygame.draw.line(sc, (WHITE), (self.x_pos, self.y_pos), (self.x_pos + WIDTH * math.cos(self.angle), self.y_pos + WIDTH * math.sin(self.angle)))

    