import pygame
import math
from map import map
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
        map_s = set(map)
        for line in range(fov_lines):
            cos = math.cos(math.radians(self.angle-self.fov_angle))
            sin = math.sin(math.radians(self.angle-self.fov_angle))
            for n2 in range(int(DIOGONAL/1)):
                x = self.x_pos + n2 * cos
                y = self.y_pos + n2 * sin
                # pygame.draw.line( sc, (WHITE), (self.x_pos, self.y_pos), 
                #                  (x, y), 1)
                if (x // x_size2 * y_size2, y // x_size2 * y_size2) in map_s: #-------------------------------------------------------------------------------------
                    # n2 *= math.cos((self.angle-(self.angle-self.fov_angle)))
                    proj_height = PROJ_COEF / n2
                    # c = 255 // (1 + n2**2 * 0.000005)
                    # shade = (c, c, c)
                    pygame.draw.rect(sc, WHITE, (line * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                    break
            self.fov_angle -= fov_abc
        self.fov_angle = fov_angle

    # def fov(self):
    #     for i in range(fov_lines):
    #         pygame.draw.line(sc, (WHITE), (self.x_pos, self.y_pos), 
    #                          (self.x_pos + (DIOGONAL  * math.cos(math.radians(self.angle-self.fov_angle))) , self.y_pos + DIOGONAL * math.sin(math.radians(self.angle-self.fov_angle))))
    #         self.fov_angle -= fov_abc
    #     self.fov_angle = fov_angle   