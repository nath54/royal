#coding:utf-8
import pygame,time,os
from pygame.locals import *

pygame.init()
tex,tey=1000,800
smenu=1



font=pygame.font.SysFont("Serif",20)
def aff():
    fenetre.fill((0,0,0))
    if smenu==1:
        bplay=pygame.draw.rect(fenetre,(150,150,50),(tex/4,tey/1.8,tex/5,tey/5),0)
        fenetre.blit(font.render("play",20,(50,50,150)),[tex/3,tey/1.6])
    pygame.display.update()
    return bplay



##################################################

fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("ROYAL")



encour=True
while encour:
    bplay=aff()
    for event in pygame.event.get():
        if event.type==QUIT: encour=False
        elif event.type==KEYDOWN:
            if event.key==K_q: encour=False
        elif event.type==MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            rpos=pygame.Rect(pos[0],pos[1],1,1)
            if rpos.colliderect(bplay):
                os.system("python a.py")










