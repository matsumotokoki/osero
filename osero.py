import pygame
from pygame.locals import *
import sys
import numpy as np

SCREEN_SIZE = (750,500);
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("osero")
void_position  =0
brack_position =1
white_position =2
brack_num=white_num=all_number=0
green=(55,255,55)
white=(255,255,255)
brack=(0,0,0)
purple=(155,155,255)
switch=1
point = ["2","2"]
turn = ["brack turn","white turn"]
# position = np.zeros((8,8),dtype=int)

#trance mat
position = np.asarray([[0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,2,1,0,0,0],
                       [0,0,0,1,2,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0]])
def initial_draw(screen):
    pygame.display.update()
    pygame.draw.rect(screen, (white), Rect(0,0,750,500),0)
    pygame.draw.rect(screen, (green), Rect(10,10,500-15,500-15),0)
    pygame.draw.rect(screen, (brack), Rect(10,10,500-15,500-15),5)
    pygame.draw.rect(screen, (purple), Rect(510,20,230,450),0)
    pygame.draw.rect(screen, (white), Rect(520,30,210,120),0)
    pygame.draw.rect(screen, (brack), Rect(520,30,210,120),5)
    sysfont = pygame.font.SysFont(None, 80)
    sysfont_turn = pygame.font.SysFont(None, 40)
    amount_brack = sysfont.render(point[0],  True, (0,0,0))
    amount_white = sysfont.render(point[1],  True, (0,0,0))
    turn_white = sysfont_turn.render(turn[1],  True, (0,0,0))
    turn_brack = sysfont_turn.render(turn[0], True, (0,0,0))
    hihun= sysfont.render("-",  True, (0,0,0))
    screen.blit(amount_white, (540,40))
    screen.blit(amount_brack, (540+140,40))
    screen.blit(hihun, (540+80,40))
    if switch == 0:
        screen.blit(turn_brack ,(550,100))
    elif switch == 1:
        screen.blit(turn_white ,(550,100))
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
def count_koma():
    brack_num=white_num=all_number=0
    for i in range(8):
        for j in range(8):
            if position[i,j]==brack_position:brack_num+=1
            elif position[i,j]==white_position:white_num+=1
    all_number = [white_num,brack_num]
    return str(white_num),str(brack_num)

def mouse_get_position():
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:  
        x, y = pygame.mouse.get_pos()
        return(x,y)

def reverse(last_position):
    right_frag=left_frag=up_frag=down_frag=right_up_frag=right_down_frag=left_up_frag=left_down_frag=True
    position_x=last_position[0]
    position_y=last_position[1]
    if switch==1:
        while right_frag:
            if position_x==7:
                right_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x+1,position_y]==1:
                position_x+=1
            elif position[position_x+1,position_y]==2:
                for reverse_time in range(last_position[0]+1,position_x+1):
                    position[reverse_time,position_y]=2
                right_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x+1,position_y]==0 or position_x>8:
                right_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while left_frag:
            if position_x==0:
                left_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x-1,position_y]==1:
                position_x-=1
            elif position[position_x-1,position_y]==2:
                for reverse_time in range(position_x-1,last_position[0]):
                    position[reverse_time,position_y]=2
                left_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x-1,position_y]==0 or position_x<=0:
                left_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while up_frag:
            if position_y==0:
                up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x,position_y-1]==1:
                position_y-=1
            elif position[position_x,position_y-1]==2:
                for reverse_time in range(position_y,last_position[1]):
                    position[position_x,reverse_time]=2
                up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x,position_y-1]==0 or position_y<=0:
                up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while down_frag:
            if position_y==7:
                down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x,position_y+1]==1:
                position_y+=1
            elif position[position_x,position_y+1]==2:
                for reverse_time in range(last_position[1]+1,position_y+1):
                    position[position_x,reverse_time]=2
                down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x,position_y+1]==0 or position_y>8:
                down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while right_up_frag:
            if position_x==7 or position_y==0:
                right_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x+1,position_y-1]==1:
                position_x+=1
                position_y-=1
            elif position[position_x+1,position_y-1]==2:
                for reverse_time in range(last_position[0]+1,position_x+1):
                    position[reverse_time,last_position[1]-1]=2
                    last_position[1]-=1
                right_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x+1,position_y-1]==0 or position_x>8 or position_y<0:
                right_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while right_down_frag:
            if position_x==7 or position_y==7:
                right_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x+1,position_y+1]==1:
                position_x+=1
                position_y+=1
            elif position[position_x+1,position_y+1]==2:
                for reverse_time in range(last_position[0]+1,position_x+1):
                    position[reverse_time,last_position[1]+1]=2
                    last_position[1]+=1
                right_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x+1,position_y+1]==0 or position_x>8 or position_y>8:
                right_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while left_up_frag:
            if position_x==0 or position_y==0:
                left_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x-1,position_y-1]==1:
                position_x-=1
                position_y-=1
            elif position[position_x-1,position_y-1]==2:
                for reverse_time in range(position_x,last_position[0]):
                    position[reverse_time,position_y]=2
                    position_y+=1
                left_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x-1,position_y-1]==0 or position_x<0 or position_y<0:
                left_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while left_down_frag:
            if position_x==0 or position_y==7:
                left_down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x-1,position_y+1]==1:
                position_x-=1
                position_y+=1
            elif position[position_x-1,position_y+1]==2:
                for reverse_time in range(position_x,last_position[0]):
                    position[reverse_time,position_y]=2
                    position_y-=1
                left_down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x-1,position_y+1]==0 or position_x<0 or position_y<0:
                left_down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

    if switch==0:
        while right_frag:
            if position_x==7:
                right_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x+1,position_y]==2:
                position_x+=1
            elif position[position_x+1,position_y]==1:
                for reverse_time in range(last_position[0]+1,position_x+1):
                    position[reverse_time,position_y]=1
                right_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x+1,position_y]==0 or position_x>8:
                right_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while left_frag:
            if position_x==0:
                left_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x-1,position_y]==2:
                position_x-=1
            elif position[position_x-1,position_y]==1:
                for reverse_time in range(position_x-1,last_position[0]):
                    position[reverse_time,position_y]=1
                left_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x-1,position_y]==0 or position_x<=0:
                left_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while up_frag:
            if position_y==0:
                up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x,position_y-1]==2:
                position_y-=1
            elif position[position_x,position_y-1]==1:
                for reverse_time in range(position_y,last_position[1]):
                    position[position_x,reverse_time]=1
                up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x,position_y-1]==0 or position_y<=0:
                up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while down_frag:
            if position_y==7:
                down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x,position_y+1]==2:
                position_y+=1
            elif position[position_x,position_y+1]==1:
                for reverse_time in range(last_position[1]+1,position_y+1):
                    position[position_x,reverse_time]=1
                down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x,position_y+1]==0 or position_y>8:
                down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while right_up_frag:
            if position_x==7 or position_y==0:
                right_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x+1,position_y-1]==2:
                position_x+=1
                position_y-=1
            elif position[position_x+1,position_y-1]==1:
                for reverse_time in range(last_position[0]+1,position_x+1):
                    position[reverse_time,last_position[1]-1]=1
                    last_position[1]-=1
                right_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x+1,position_y-1]==0 or position_x>8 or position_y<0:
                right_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while right_down_frag:
            if position_x==7 or position_y==7:
                right_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x+1,position_y+1]==2:
                position_x+=1
                position_y+=1
            elif position[position_x+1,position_y+1]==1:
                for reverse_time in range(last_position[0]+1,position_x+1):
                    position[reverse_time,last_position[1]+1]=1
                    last_position[1]+=1
                right_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x+1,position_y+1]==0 or position_x>8 or position_y>8:
                right_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while left_up_frag:
            if position_x==0 or position_y==0:
                left_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x-1,position_y-1]==2:
                position_x-=1
                position_y-=1
            elif position[position_x-1,position_y-1]==1:
                for reverse_time in range(position_x,last_position[0]):
                    position[reverse_time,position_y]=1
                    position_y+=1
                left_up_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x-1,position_y-1]==0 or position_x<0 or position_y<0:
                left_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break

        while left_down_frag:
            if position_x==0 or position_y==7:
                left_down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            if position[position_x-1,position_y+1]==2:
                position_x-=1
                position_y+=1
            elif position[position_x-1,position_y+1]==1:
                for reverse_time in range(position_x,last_position[0]):
                    position[reverse_time,position_y]=1
                    position_y-=1
                left_down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
            elif position[position_x-1,position_y+1]==0 or position_x<0 or position_y<0:
                left_down_frag=False
                position_x=last_position[0]
                position_y=last_position[1]
                break
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
                print(position[0,4])
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_position=mouse_get_position()
            for i in range(8):
                for j in range(8):
                    if mouse_position[0]>(20+60*i) and mouse_position[0]<(60+60*i) and mouse_position[1]>(25+60*j) and mouse_position[1]<(60+60*j):
                        last_position=[i,j]
                        if switch == 1 and position[i,j]==0:
                            position[i,j]=2
                            reverse(last_position)
                            switch = 0
                        elif switch == 0 and position[i,j]==0:
                            position[i,j]=1
                            reverse(last_position)
                            switch = 1
                        point=count_koma()
