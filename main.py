import pygame
import math
from pygame.locals import *
from settings import *
from player import *
from map import map

pygame.init()
clock = pygame.time.Clock()
screen = sc
running = True
player = Player()

surf = pygame.Surface((100, 100))
surf.fill(LIGHT_GREEN)
surf2 = pygame.Surface((100, 100))
surf2.fill(BLACK)

while running:
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:
            running = False

    for x, y in map:
        pygame.draw.rect(screen, GRAY, (x, y, x_size2, y_size2)) #--------------------------------------------------------------------------------------------------------------

    controls = pygame.key.get_pressed()
    if controls[pygame.K_a]:
                screen.blit(surf2, (x_pos2, y_pos2))
                x_pos2 += -5
    if controls[pygame.K_s]:
                screen.blit(surf2, (x_pos2, y_pos2))
                y_pos2 += 5       
    if controls[pygame.K_w]:
                screen.blit(surf2, (x_pos2, y_pos2))
                y_pos2 += -5
    if controls[pygame.K_d]:
                screen.blit(surf2, (x_pos2, y_pos2))
                x_pos2 += 5

    if controls[pygame.K_KP_4]:
        player.move(x = -1)
    if controls[pygame.K_KP_6]:
        player.move(x = 1)
    if controls[pygame.K_KP_8]:
        player.move(y = -1)
    if controls[pygame.K_KP_5]:
        player.move(y = 1)
    if controls[pygame.K_KP_7]:
        player.rotate(-0.01)
    if controls[pygame.K_KP_9]:
        player.rotate(0.01)
        
    screen.fill(BLACK)
    screen.blit(surf, (x_pos2, y_pos2))
    player.draw()  
    player.line()         
    pygame.display.flip() 
    clock.tick(FPS)
    
pygame.quit()

# import pygame
# from pygame.locals import *
# from settings import *
# from player import *

# pygame.init()
# clock = pygame.time.Clock()
# screen = sc
# running = True

# player = Player()

# surf = pygame.Surface((100, 100))
# surf.fill(LIGHT_GREEN)
# surf2 = pygame.Surface((100, 100))
# surf2.fill(BLACK)

# while running:
#     for event in pygame.event.get():
         
#         if event.type == pygame.QUIT:
#             running = False
#         controls = pygame.key.get_pressed()
#         if controls[pygame.K_a]:
#                     screen.blit(surf2, (x1, y1))
#                     x1 += -5
#         if controls[pygame.K_s]:
#                     screen.blit(surf2, (x1, y1))
#                     y1 += 5       
#         if controls[pygame.K_w]:
#                     screen.blit(surf2, (x1, y1))
#                     y1 += -5
#         if controls[pygame.K_d]:
#                     screen.blit(surf2, (x1, y1))
#                     x1 += 5

#         if controls[pygame.K_LEFT]:
#             player.move(x = -1)
#         if controls[pygame.K_RIGHT]:
#             player.move(x = 1)
#         if controls[pygame.K_UP]:
#             player.move(y = -1)
#         if controls[pygame.K_DOWN]:
#             player.move(y = 1)
        
#     screen.fill(BLACK)
#     screen.blit(surf, (x1, y1))
#     player.draw()           
#     pygame.display.flip() 
#     clock.tick(60)
    
# pygame.quit()