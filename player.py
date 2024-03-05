import pygame
import math
from map import *
from settings import *

class Player:
    def __init__(self):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle
        self.fov_angle = fov_angle
        self.map = set(map)
        self.mapx = set(mapx)
        self.mapy = set(mapy)
        self.G = set(G)

    def rotate(self, b):
        self.angle += b 

    def move_forw(self):
        # u = 0
        xm = math.cos((self.angle))
        ym = math.sin((self.angle))
        x = xm * P_SPEED + self.x_pos
        y = ym * P_SPEED + self.y_pos
        if (x // x_size2 * y_size2, y // x_size2 * y_size2) in self.map:
            self.x_pos += 0
            self.y_pos += 0
            # u += 1
        else:
            self.x_pos = x
            self.y_pos = y
        # if u == 1:
            # self.y_pos = y
    
    def move_back(self):
        # u = 0        
        xm = -math.cos((self.angle))
        ym = -math.sin((self.angle))
        # print(x,y,self.angle,"BACK")
        x = xm * P_SPEED + self.x_pos
        y = ym * P_SPEED + self.y_pos
        if (x // x_size2 * y_size2, y // x_size2 * y_size2) in self.map:
            self.x_pos += 0
            self.y_pos += 0
            # u += 1
        else:
            self.x_pos = x
            self.y_pos = y
        # if u == 1:
            # self.y_pos = y

    def move_left(self):
        # u = 0        
        xm = -math.cos((self.angle))
        ym = math.sin((self.angle))
        x = ym * P_SPEED + self.x_pos
        y = xm * P_SPEED + self.y_pos
        if (x // x_size2 * y_size2, y // x_size2 * y_size2) in self.map:
            self.x_pos += 0
            self.y_pos += 0
            # u += 1
        else:
            self.x_pos = x
            self.y_pos = y
        # if u == 1:
            # self.y_pos = y

    def move_right(self):
        # u = 0        
        xm = math.cos((self.angle))
        ym = -math.sin((self.angle))
        x = ym * P_SPEED + self.x_pos
        y = xm * P_SPEED + self.y_pos
        if (x // x_size2 * y_size2, y // x_size2 * y_size2) in self.map:
            self.x_pos += 0
            self.y_pos += 0
            # u += 1
        else:
            self.x_pos = x
            self.y_pos = y
        # if u == 1:
            # self.y_pos = y


    def draw(self):
        pygame.draw.circle(sc, (LIGHT_PURPLE), (self.x_pos, self.y_pos), (r_size), (rline))
        #pygame.draw.circle(screen, (LIGHT_PURPLE, YELLOW), (self.x_pos, self.y_pos, r_size, rline))
    
    # def obj_1(self):
        # for line in range(fov_lines):
            # cur_angle = self.angle-self.fov_angle
            # cos = math.cos(cur_angle)
            # sin = math.sin(cur_angle)
            # for depth in range(int(600)):
                # x = self.x_pos + depth * cos
                # y = self.y_pos + depth * sin
                # pygame.draw.line( sc, (WHITE), (self.x_pos, self.y_pos), 
                                #  (x, y), 1)
                # if (x // 20 * 20, y // 20 * 20) in self.G:    
                    # depth *= math.cos(self.angle-(cur_angle))
                    # proj_height = min(PROJ_COEF_OBJ / (depth + 0.0001), HEIGHT)
                    # c = 255 // (1 + depth**2 * 0.000005)
                    # shade = (c, c, c/3)
                    # pygame.draw.rect(sc, shade, (line * SCALE, (HALF_HEIGHT - proj_height // 2), SCALE, proj_height))
                    # break
            # self.fov_angle -= fov_abr
        # self.fov_angle = fov_angle

    def fov(self):
        for line in range(fov_lines):
            cur_angle = self.angle-self.fov_angle
            cos = math.cos(cur_angle)
            sin = math.sin(cur_angle)
            for depth in range(int(DIOGONAL)):
                x = self.x_pos + depth * cos
                y = self.y_pos + depth * sin
                # pygame.draw.line( sc, (WHITE), (self.x_pos, self.y_pos), 
                                #  (x, y), 1)
                if (x // x_size2 * y_size2, y // x_size2 * y_size2) in self.map: #-------------------------------------------------------------------------------------    
                    depth *= math.cos(self.angle-(cur_angle))
                    proj_height = min(PROJ_COEF / (depth + 0.0001), HEIGHT)
                    c = 255 // (1 + depth**2 * 0.000005)
                    shade = (c, c, c)
                    pygame.draw.rect(sc, shade, (line * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                    break
            self.fov_angle -= fov_abr
        self.fov_angle = fov_angle
    

                


 
























 
    # def fov(self):
        # for i in range(fov_lines):
            # pygame.draw.line(sc, (WHITE), (self.x_pos, self.y_pos), 
                            #  (self.x_pos + (DIOGONAL  * math.cos(math.radians(self.angle-self.fov_angle))) , self.y_pos + DIOGONAL * math.sin(math.radians(self.angle-self.fov_angle))))
            # self.fov_angle -= fov_abc
        # self.fov_angle = fov_angle   
        # 
    # def fov(self):
        # map_s = set(map)
        # height = 0
        # for line in range(fov_lines):
            # cos = math.cos(math.radians(self.angle-self.fov_angle))
            # sin = math.sin(math.radians(self.angle-self.fov_angle))
            # for n2 in range(int(DIOGONAL)):
                # x = self.x_pos + n2 * cos
                # y = self.y_pos + n2 * sin
                # pygame.draw.line( sc, (WHITE), (self.x_pos, self.y_pos), 
                                #  (x, y), 1)
                # if (x // x_size2 * y_size2, y // x_size2 * y_size2) in map_s: #------------------------------------------------------------------------------------- 
                    # d = math.sqrt((x-self.x_pos)**2 + (y-self.y_pos)**2)                    
                    # c = 255 // (1 + n2**2 * 0.000005)
                    # shade = (c, c, c)
                    # if math.radians(self.angle) == math.radians(0):
                        # height = HEIGHT * (1-((x - self.x_pos)/WIDTH))                    
                    # if math.radians(self.angle) == math.radians(90):
                        # height = HEIGHT * (1-((y - self.y_pos)/WIDTH))
                    # if math.radians(self.angle) == math.radians(180):
                    # if math.radians(self.angle) == math.radians(270):
                    # pygame.draw.rect(sc, shade, (line * SCALE, HALF_HEIGHT - height // 2, SCALE, height))
                    # break
            # self.fov_angle -= fov_abc
        # self.fov_angle = fov_angle