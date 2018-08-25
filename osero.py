import const
import agent
import sys
import pygame
from time import sleep
from pygame.locals import *
import sys
import numpy as np

SCR_RECT = Rect(0,0,const.SCR_X,const.SCR_y)
green=(55,255,55)
r_green=(125,155,125)
white=(255,255,255)
brack=(0,0,0)
red=(255,0,0)
gray=(100,100,100)
purple=(155,155,255)
d_purple=(255,0,255)

class Osero:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCR_RECT.size)
        self.SWITCH=0
        while True:
            pygame.display.update()
            self.draw_back()
            self.amount = self.count_storn()
            self.draw_txt(self.screen,self.amount)
            self.next_draw()
            self.storn_draw(self.screen)
            pygame.display.set_caption("osero")
            self.event()

    def draw_back(self):
        pygame.draw.rect(self.screen, (white), Rect(0,0,750,500),0)
        pygame.draw.rect(self.screen, (green), Rect(10,10,500-15,500-15),0)
        pygame.draw.rect(self.screen, (brack), Rect(10,10,500-15,500-15),5)
        pygame.draw.rect(self.screen, (purple), Rect(510,20,230,450),0)
        pygame.draw.rect(self.screen, (white), Rect(520,30,210,120),0)
        pygame.draw.rect(self.screen, (brack), Rect(520,30,210,120),5)
        pygame.draw.rect(self.screen, (white), Rect(520,160,210,120),0)
        pygame.draw.rect(self.screen, (brack), Rect(520,160,210,120),5)
        pygame.draw.rect(self.screen, (white), Rect(520,290,210,120),0)
        pygame.draw.rect(self.screen, (brack), Rect(520,290,210,120),5)
        for i in range(8):
            pygame.draw.line(self.screen, (brack), (15+const.CS*(i+1),15), (15+const.CS*(i+1),485),3)
            pygame.draw.line(self.screen, (brack), (15,15+const.CS*(i+1)), (485,15+const.CS*(i+1)),3)
    
    def draw_txt(self,screen,amount):
        sysfont_big = pygame.font.SysFont(None, 80)
        sysfont_small = pygame.font.SysFont(None, 50)

        self.white_win = sysfont_small.render("white win!!",True, (0,55,155)) 
        self.brack_win = sysfont_small.render("brack win!!",True, (0,55,155)) 
        self.draw = sysfont_small.render("draw game!!",True, (0,55,155)) 
        self.white_num = sysfont_big.render(str(amount[0]),True, (brack)) 
        self.brack_num = sysfont_big.render(str(amount[1]),True, (brack)) 
        self.hihun = sysfont_big.render("-",True, (brack)) 
        self.pass_txt  = sysfont_big.render("pass", True, (red))
        self.replay_txt= sysfont_big.render("replay", True,(d_purple))
        self.turn_white = sysfont_small.render("white turn",  True, (brack))
        self.turn_brack = sysfont_small.render("brack turn", True, (brack))

        self.screen.blit(self.pass_txt, (560,190))
        self.screen.blit(self.replay_txt, (540,320))
        self.screen.blit(self.brack_num, (650,40))
        self.screen.blit(self.white_num, (550,40))
        self.screen.blit(self.hihun, (620,40))
        if self.SWITCH == 0:
            self.screen.blit(self.turn_brack, (540,100))
        elif self.SWITCH == 1:
            self.screen.blit(self.turn_white, (540,100))
        if (amount[0]>amount[1] and amount[2]==64) or (amount[1]==0):
            self.screen.blit(self.brack_win, (530,430))
        elif (amount[0]<amount[1] and amount[2]==64) or (amount[0]==0):
            self.screen.blit(self.white_win, (530,430))
        elif (amount[0]==amount[1] and amount[2]==64):
            self.screen.blit(self.draw, (530,430))

    def storn_draw(self,screen):
        for i in range(8):
            for j in range(8):
                if const.storn_position[j,i]==0:
                    pygame.draw.circle(self.screen, (green), (45+60*(i),45+60*(j)), 23)
                elif const.storn_position[j,i]==1:
                    pygame.draw.circle(self.screen, (brack), (45+60*(i),45+60*(j)), 23)
                elif const.storn_position[j,i]==2:
                    pygame.draw.circle(self.screen, (white), (45+60*(i),45+60*(j)), 23)
                elif const.storn_position[j,i]==3:
                    pygame.draw.circle(self.screen, (gray), (45+60*(i),45+60*(j)), 5)

    def mouse_get_position(self):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:  
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            return(self.mouse_x,self.mouse_y)

    def count_storn(self):
        self.amount = [0 ,0 ,0]#brack,white,all
        for i in range(8):
            for j in range(8):
                if const.storn_position[j,i] == 1:
                    self.amount[0] +=1
                elif const.storn_position[j,i] == 2:
                    self.amount[1] +=1
        self.amount[2] = self.amount[0]+self.amount[1]
        return self.amount

    def next_draw(self):
        DX=[1,1,0,-1,-1,-1,0,1]
        DY=[0,1,1,1,0,-1,-1,-1]
        frag=1
        if self.SWITCH==0:
            for i in range(8):
                for j in range(8):
                        for (dx,dy) in zip (DX,DY):
                            k = 1
                            count_reverse = 1
                            while True:
                                if (j+dx*k<0)or(j+dx*k>7)or(i+dy*k<0)or(i+dy*k>7):
                                    count_reverse=1
                                    break
                                if const.storn_position[i+dy*k][j+dx*k] == 0 or const.storn_position[i+dy*k][j+dx*k] == 3:
                                    count_reverse=1
                                    break
                                if const.storn_position[i+dy*k][j+dx*k] == 2:
                                    count_reverse+=1
                                if const.storn_position[i+dy*k][j+dx*k] == 1:
                                    break
                                k+=1
                            if count_reverse==1:
                                frag+=1
                        if frag<9 and const.storn_position[i,j]==0:
                            const.storn_position[i,j]=3
                        if frag==9 and const.storn_position[i,j]==3:
                            const.storn_position[i,j]=0
                        frag=1

        if self.SWITCH==1:
            for i in range(8):
                for j in range(8):
                        for (dx,dy) in zip (DX,DY):
                            k = 1
                            count_reverse = 1
                            while True:
                                if (j+dx*k<0)or(j+dx*k>7)or(i+dy*k<0)or(i+dy*k>7):
                                    count_reverse=1
                                    break
                                if const.storn_position[i+dy*k][j+dx*k] == 0 or const.storn_position[i+dy*k][j+dx*k] == 3:
                                    count_reverse=1
                                    break
                                if const.storn_position[i+dy*k][j+dx*k] == 1:
                                    count_reverse+=1
                                if const.storn_position[i+dy*k][j+dx*k] == 2:
                                    break
                                k+=1
                            if count_reverse==1:
                                frag+=1
                        if frag<9 and const.storn_position[i,j]==0:
                            const.storn_position[i,j]=3
                        if frag==9 and const.storn_position[i,j]==3:
                            const.storn_position[i,j]=0
                        frag=1

    def reverse(self,last_position):
        DX=[1,1,0,-1,-1,-1,0,1]
        DY=[0,1,1,1,0,-1,-1,-1]
        frag=1
        if self.SWITCH==0:
            for (dx,dy) in zip (DX,DY):
                i = 1
                count_reverse = 1
                while True:
                    if (last_position[1]+dx*i<0)or(last_position[1]+dx*i>7)or(last_position[0]+dy*i<0)or(last_position[0]+dy*i>7):
                        count_reverse=1
                        break
                    if const.storn_position[last_position[0]+dy*i][last_position[1]+dx*i] == 0:
                        count_reverse=1
                        break
                    if const.storn_position[last_position[0]+dy*i][last_position[1]+dx*i] == 2:
                        count_reverse+=1
                    if const.storn_position[last_position[0]+dy*i][last_position[1]+dx*i] == 1:
                        break
                    i+=1
                for i in range(count_reverse):
                    const.storn_position[last_position[0]+dy*i][last_position[1]+dx*i]=1
                if count_reverse==1:
                    frag+=1

        if self.SWITCH==1:
            for (dx,dy) in zip (DX,DY):
                i = 1
                count_reverse = 1
                while True:
                    if (last_position[1]+dx*i<0)or(last_position[1]+dx*i>7)or(last_position[0]+dy*i<0)or(last_position[0]+dy*i>7):
                        count_reverse=1
                        break
                    if const.storn_position[last_position[0]+dy*i][last_position[1]+dx*i] == 0:
                        count_reverse=1
                        break
                    if const.storn_position[last_position[0]+dy*i][last_position[1]+dx*i] == 1:
                        count_reverse+=1
                    if const.storn_position[last_position[0]+dy*i][last_position[1]+dx*i] == 2:
                        break
                    i+=1
                for i in range(count_reverse):
                    const.storn_position[last_position[0]+dy*i][last_position[1]+dx*i]=2
                if count_reverse==1:
                    frag+=1
        return frag

    def event(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    print(const.storn_position)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_position=self.mouse_get_position()
                for i in range(8):
                    for j in range(8):
                        if mouse_position[0]>(20+const.CS*i) and mouse_position[0]<(60+const.CS*i) and mouse_position[1]>(25+const.CS*j) and mouse_position[1]<(60+const.CS*j):
                            self.last_position=[j,i]
                            if self.SWITCH==1 and const.storn_position[j,i]==3:
                                const.storn_position[j,i]=2
                                count_reverse=self.reverse(self.last_position)
                                if count_reverse!=9:
                                    self.SWITCH=0
                                else: const.storn_position[j,i]=0
                            if self.SWITCH==0 and const.storn_position[j,i]==3:
                                const.storn_position[j,i]=1
                                count_reverse=self.reverse(self.last_position)
                                if count_reverse!=9:
                                    self.SWITCH=1
                                else: const.storn_position[j,i]=0

                if mouse_position[0]>525 and mouse_position[0]<725 and mouse_position[1]>295 and mouse_position[1]<405:
                    const.storn_position = np.asarray([[0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,1,2,0,0,0],
                                                       [0,0,0,2,1,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0]])
                if mouse_position[0]>525 and mouse_position[0]<725 and mouse_position[1]>165 and mouse_position[1]<275:
                    if self.SWITCH==1:
                        self.SWITCH=0
                    else:
                        self.SWITCH=1


class VS_AI(Osero):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCR_RECT.size)
        self.SWITCH=0
        while True:
            pygame.display.update()
            self.draw_back()
            self.amount = self.count_storn()
            self.draw_txt(self.screen,self.amount)
            self.next_draw()
            self.storn_draw(self.screen)
            pygame.display.set_caption("osero")
            self.single_event()

    def AI_action(self):
        stock=-51
        for i in range(8):
            for j in range(8):
                if const.storn_position[i,j] == 3 and stock<=const.value_storn[i,j]:
                    stock=const.value_storn[i,j]
                    AI_select=[i,j]
        if stock==-51:
            self.SWITCH=0
        if self.SWITCH==1:
            const.storn_position[[AI_select[0]],[AI_select[1]]]=2
            self.reverse(AI_select)
#            pygame.draw.circle(screen, (r_green), (45+60*(AI_select[0]),45+60*(AI_select[1])), 40)
            self.SWITCH=0

    def single_event(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    print(const.storn_position)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_position=self.mouse_get_position()
                for i in range(8):
                    for j in range(8):
                        if mouse_position[0]>(20+const.CS*i) and mouse_position[0]<(60+const.CS*i) and mouse_position[1]>(25+const.CS*j) and mouse_position[1]<(60+const.CS*j):
                            self.last_position=[j,i]
                            if self.SWITCH==0 and const.storn_position[j,i]==3:
                                const.storn_position[j,i]=1
                                count_reverse=self.reverse(self.last_position)
                                if count_reverse!=9:
                                    self.SWITCH=1
                                    self.next_draw()
                                    self.AI_action()
                                else: const.storn_position[j,i]=0

                if mouse_position[0]>525 and mouse_position[0]<725 and mouse_position[1]>295 and mouse_position[1]<405:
                    const.storn_position = np.asarray([[0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,2,1,0,0,0],
                                                       [0,0,0,1,2,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0]])
                if mouse_position[0]>525 and mouse_position[0]<725 and mouse_position[1]>165 and mouse_position[1]<275:
                    if self.SWITCH==1:
                        self.SWITCH=0
                    else:
                        self.SWITCH=1
                        self.next_draw()
                        self.AI_action()

class GA(Osero):
#TODO learning
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCR_RECT.size)
        self.SWITCH=0
        while True:
            pygame.display.update()
            self.draw_back()
            self.amount = self.count_storn()
            self.draw_txt(self.screen,self.amount)
            self.next_draw()
            self.storn_draw(self.screen)
            pygame.display.set_caption("osero")
            self.AI_action()
            self.GA_event()

    def AI_action(self):
        stock=-51
        if self.SWITCH==1:
            for i in range(8):
                for j in range(8):
                    if const.storn_position[i,j] == 3 and stock<=const.value_storn[i,j]:
                        stock=const.value_storn[i,j]
                        AI_select=[i,j]
            if stock==-51:
                self.SWITCH=0
            if self.SWITCH==1:
                const.storn_position[[AI_select[0]],[AI_select[1]]]=2
                self.reverse(AI_select)
                self.SWITCH=0
        elif self.SWITCH==0:
            for i in range(8):
                for j in range(8):
                    if const.storn_position[i,j] == 3 and stock<=const.value_storn[i,j]:
                        stock=const.value_storn[i,j]
                        AI_select=[i,j]
            if stock==-51:
                self.SWITCH=1
            if self.SWITCH==0:
                const.storn_position[[AI_select[0]],[AI_select[1]]]=2
                self.reverse(AI_select)
                self.SWITCH=1
        if self.amount[2] == 64 or self.amount[0]==0 or self.amount[1]==0:
            const.storn_position = np.asarray([[0,0,0,0,0,0,0,0],
                                               [0,0,0,0,0,0,0,0],
                                               [0,0,0,0,0,0,0,0],
                                               [0,0,0,2,1,0,0,0],
                                               [0,0,0,1,2,0,0,0],
                                               [0,0,0,0,0,0,0,0],
                                               [0,0,0,0,0,0,0,0],
                                               [0,0,0,0,0,0,0,0]])
            if self.amount[0]==0 or self.amount[0]<self.amount[1]:
                print("brack_win")
            elif self.amount[1]==0 or self.amount[0]>self.amount[1]:
                print("white_win")
            elif self.amount[0]==self.amount[1]:
                print("draw")

    def GA_event(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    print(const.storn_position)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_position=self.mouse_get_position()
                if mouse_position[0]>525 and mouse_position[0]<725 and mouse_position[1]>295 and mouse_position[1]<405:
                    const.storn_position = np.asarray([[0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,2,1,0,0,0],
                                                       [0,0,0,1,2,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0],
                                                       [0,0,0,0,0,0,0,0]])
                if mouse_position[0]>525 and mouse_position[0]<725 and mouse_position[1]>165 and mouse_position[1]<275:
                    if self.SWITCH==1:
                        self.SWITCH=0
                    else:
                        self.SWITCH=1
                        self.next_draw()
                        self.AI_action()
                
args=sys.argv
args.append('main')
if args[1] in 'AI':
    if __name__ == '__main__':
        VS_AI()
elif args[1] in 'GA':
    if __name__ == '__main__':
        GA()
elif args[1] in 'main':
    if __name__ == '__main__':
        Osero()
