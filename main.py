#coding:utf-8
import pygame,time,os
from pygame.locals import *
from cartes import *

pygame.init()
tex,tey=1000,800
smenu=2
cselec=None


font=pygame.font.SysFont("Serif",20)

rarete=["commun","rare","epique","legendaire","divin"]
craret=[(0,0,140),(150,105,25),(150,0,150),(20,150,20),(250,250,0)]

def aff():
    fenetre.fill((50,20,100))
    bplay=pygame.Rect(0,0,0,0)
    bm1=fenetre.blit(pygame.transform.scale(pygame.image.load("images/m1.png"),[int(tex/4),75]),[tex/4*0,0])
    bm2=fenetre.blit(pygame.transform.scale(pygame.image.load("images/m2.png"),[int(tex/4),75]),[tex/4*1,0])
    bm3=fenetre.blit(pygame.transform.scale(pygame.image.load("images/m3.png"),[int(tex/4),75]),[tex/4*2,0])
    bm4=fenetre.blit(pygame.transform.scale(pygame.image.load("images/m4.png"),[int(tex/4),75]),[tex/4*3,0])
    rcs=[]
    if smenu==2:
        #bplay=pygame.draw.rect(fenetre,(150,150,50),(tex/4,tey/1.8,tex/5,tey/5),0)
        #fenetre.blit(font.render("play",20,(50,50,150)),[tex/3,tey/1.6])
        bplay=fenetre.blit(pygame.transform.scale(pygame.image.load("images/bplay.png"),[int(200/1200*tex),int(150/1000*tey)]),[tex/2,tey/2,])
    elif smenu==1:
        xx,yy=50,100
        tx,ty=int(100/1200*tex),int(125/1000*tey)
        for g in ctpp:
            if g==cselec:
                iii="images/fcs.png"
                txi,tyi=400,400
                xi,yi=tex-txi,tey-tyi
                pygame.draw.rect(fenetre,(200,200,200),(xi,yi,txi,tyi),0)
                fenetre.blit(font.render(str(cnom[g])                         ,20,(50,50,50))      ,[xi+5 ,yi])
                fenetre.blit(font.render("vie = "        +str(cvie[g])        ,20,(0,0,0))         ,[xi+5 ,yi+20])
                fenetre.blit(font.render("att = "        +str(catt[g])        ,20,(0,0,0))         ,[xi+5 ,yi+40])
                fenetre.blit(font.render("vitesse att = "+str(cvat[g])        ,20,(0,0,0))         ,[xi+5 ,yi+60])
                fenetre.blit(font.render("vitesse = "    +str(cvit[g])        ,20,(0,0,0))         ,[xi+150,yi+20])
                fenetre.blit(font.render("elixir = "     +str(celi[g])        ,20,(150,0,150))     ,[xi+150,yi+40])
                fenetre.blit(font.render("rareté = "     +str(rarete[crar[g]]),20,craret[crar[g]]) ,[xi+150,yi+60])
            else: iii="images/fc.png"
            rcs.append( fenetre.blit(pygame.transform.scale(pygame.image.load(iii),[tx+30,ty+30]),[xx-15,yy-15]) )
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[g]),[tx,ty]),[xx,yy])
            xx+=tx+35
            if xx>tex-tx*1.2:
                xx=50
                yy+=ty+35
    pygame.display.update()
    return bplay,bm1,bm2,bm3,bm4,rcs



##################################################

fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("ROYAL")
fenetre.blit(pygame.transform.scale(pygame.image.load("images/fmenu.png"),[tex,tey]),[0,0])
pygame.display.update()
time.sleep(1)

encour=True
while encour:
    bplay,bm1,bm2,bm3,bm4,rcs=aff()
    for event in pygame.event.get():
        if event.type==QUIT: encour=False
        elif event.type==KEYDOWN:
            if event.key==K_q: encour=False
        elif event.type==MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            rpos=pygame.Rect(pos[0],pos[1],1,1)
            if rpos.colliderect(bplay): os.system("python a.py")
            elif rpos.colliderect(bm1): smenu=1
            elif rpos.colliderect(bm2): smenu=2
            elif rpos.colliderect(bm3): smenu=3
            elif rpos.colliderect(bm4): smenu=4
            for c in rcs:
                if rpos.colliderect(c):
                    if cselec!=rcs.index(c): cselec=rcs.index(c)
                    else: cselec=None
            
    








