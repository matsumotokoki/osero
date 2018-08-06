import pygame
from pygame.locals import *
import sys
import numpy as np

SCREEN_SIZE = (500,500);
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("osero")
void_position  =0
brack_position =1
white_position =2
green=(55,255,55)
white=(255,255,255)
brack=(0,0,0)
position = np.zeros((8,8),dtype=int)
position[3,3]=position[4,4]=1
position[3,4]=position[4,3]=2
#back_img = pygame.image.load("./back.png").convert()
def initial_draw(screen):
    pygame.display.update()
    pygame.draw.rect(screen, (white), Rect(0,0,500,500),0)
    pygame.draw.rect(screen, (green), Rect(10,10,500-15,500-15),0)
    pygame.draw.rect(screen, (brack), Rect(10,10,500-15,500-15),5)

    pygame.draw.circle(screen, (brack), (135,135), 8)
    pygame.draw.circle(screen, (brack), (135+240,135), 8)
    pygame.draw.circle(screen, (brack), (135,135+240), 8)
    pygame.draw.circle(screen, (brack), (135+240,135+240), 8)
    
    for i in range(8):
        pygame.draw.line(screen, (brack), (15+60*(i+1),15), (15+60*(i+1),485),3)
        pygame.draw.line(screen, (brack), (15,15+60*(i+1)), (485,15+60*(i+1)),3)

def koma_draw(screen):
    for i in range(8):
        for j in range(8):
            if position[i,j]==0:
                pygame.draw.circle(screen, (green), (45+60*(i),45+60*(j)), 25)
            if position[i,j]==1:
                pygame.draw.circle(screen, (brack), (45+60*(i),45+60*(j)), 25)
            if position[i,j]==2:
                pygame.draw.circle(screen, (white), (45+60*(i),45+60*(j)), 25)

def mouse_get_position():
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:  # 左クリック
        x, y = pygame.mouse.get_pos()
        return(x,y)

game_mode = True

while game_mode:
    #screen.blit(back_img,(0,0))
    pygame.display.update()
    initial_draw(screen)
    koma_draw(screen)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:  
            if event.key == K_ESCAPE:
                sys.exit()
            if event.key == K_SPACE:
                koma_draw(screen)
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_position=mouse_get_position()
            for i in range(8):
                for j in range(8):
                    if mouse_position[0]>(20+60*i) and mouse_position[0]<(60+60*i) and mouse_position[1]>(25+60*j) and mouse_position[1]<(60+60*j):
                        position[i,j]=1
