import pygame
import math
from settings import *

class Player:
    def __init__(self):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle
        self.fov_angle = fov_angle

    def rotate(self, b):
        self.angle += b 

    def move_forw(self):
        x = math.cos(math.radians(self.angle))
        y = math.sin(math.radians(self.angle))
        # print(x,y,self.angle,"FORW")
        self.x_pos += x * P_SPEED
        self.y_pos += y * P_SPEED
    
    def move_back(self):
        x = -math.cos(math.radians(self.angle))
        y = -math.sin(math.radians(self.angle))
        # print(x,y,self.angle,"BACK")
        self.x_pos += x * P_SPEED
        self.y_pos += y * P_SPEED

    def move_left(self):
        x = -math.cos(math.radians(self.angle))
        y = math.sin(math.radians(self.angle))
        self.x_pos += y * P_SPEED
        self.y_pos += x * P_SPEED

    def move_right(self):
        x = math.cos(math.radians(self.angle))
        y = -math.sin(math.radians(self.angle))
        self.x_pos += y * P_SPEED
        self.y_pos += x * P_SPEED

    def draw(self):
        pygame.draw.circle(sc, (LIGHT_PURPLE), (self.x_pos, self.y_pos), (r_size), (rline))
        #pygame.draw.circle(screen, (LIGHT_PURPLE, YELLOW), (self.x_pos, self.y_pos, r_size, rline))

    def fov(self):
        for i in range(fov_lines):
            pygame.draw.line(sc, (WHITE), (self.x_pos, self.y_pos), 
                             (self.x_pos + (DIOGONAL  * math.cos(math.radians(self.angle-self.fov_angle))) , self.y_pos + DIOGONAL * math.sin(math.radians(self.angle-self.fov_angle))))
            self.fov_angle -= fov_abl
        self.fov_angle = fov_angle

    