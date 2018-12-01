#####################################################################################
############# A NE PAS LANCER, EN COURS DE DEVELOPPEMENT ############################
#####################################################################################
#coding:utf-8
import random,pygame,os,time,math
from pygame.locals import *

pygame.init()

tex,tey=1200,1000
mape=[]
impmap=[]
pause=False

def bm(dd):
    for m in mape:
        m.px+=dd[0]
        m.py+=dd[1]

def vt(p):
    rr=pygame.Rect(p.px,p.py,p.tx,p.ty)
    for m in mape:
        if m.pmd==False and m.px > 0-m.tx and m.px < tex+m.tx and m.py > 0-m.ty and m.py < tey+m.ty:
            if rr.colliderect():
            

class Perso:
    def __init__(self,x,y):
        self.nom="Jean"
        self.vie=100
        self.px=x
        self.py=y
        self.vit=15
        self.tx=100
        self.ty=100
        self.img=pygame.transform.scale(pygame.image.load("images/ow/perso.png"),[self.tx,self.ty])
    def bouger(self,aa):
        if aa=="up":
            bm([0,self.vit])
        elif aa=="down":
            bm([0,-self.vit])
        elif aa=="left":
            bm([self.vit,0])
        elif aa=="right":
            bm([-self.vit,0])
        elif aa=="jump":
            for x in range(10):
                bm([0,-1])
                time.sleep(0.01)
            time.sleep(0.1)
            for x in range(10):
                bm([0,1])
                time.sleep(0.01)

tx=50
ty=50

mtp=[0          ,1          ,2         ,3           ,4         ,5        ,6             ]
mnm=["herbe"    ,"route"    ,"rien"    ,"maison"    ,"magasin" ,"mur"    ,"parquet1"    ]
mtx=[tx         ,tx         ,tx        ,tx*2        ,tx*4      ,tx       ,tx            ]
mty=[ty         ,ty         ,ty        ,ty*2        ,ty*4      ,ty       ,ty            ]
mpm=[True       ,True       ,False     ,False       ,False     ,False    ,True          ]
mim=["herbe.png","route.png","rien.png","maison.png","shop.png","mur.png","par1.png"    ]

def chtt(dtx,dty,tx,ty):
    for m in mape:
        m.tx*=tx
        m.ty*=ty
    perso.tx=tx
    perso.ty=ty
    return tx,ty
    

class Om():
    def __init__(self,x,y,tp):
        self.px=x
        self.py=y
        self.tx=mtx[tp]
        self.ty=mty[tp]
        self.pmd=mpm[tp]
        self.img=pygame.transform.scale(pygame.image.load("images/ow/"+mim[tp]),[self.tx,self.ty])

def aff():
    if not pause:
        fenetre.fill((0,0,0))
        for m in mape:
            if m.px > 0-m.tx and m.px < tex+m.tx and m.py > 0-m.ty and m.py < tey+m.ty:
                fenetre.blit(m.img,[m.px,m.py])
        fenetre.blit(perso.img,[perso.px,perso.py])
    pygame.display.update()

def vtz(p):
    rr=pygame.Rect(p.px,p.py,p.tx,p.ty)
    for z in inpmape:
        if rr.colliderect(pygame.Rect(z[1],z[2],10,10))
        

def cm():
    mape=[]
    impmape=[]
    mp=open("mape.nath","r").readlines()
    xx=0
    yy=0
    for m in mp:
        for c in m:
            try:
                mape.append(Om(xx,yy,int(c)))
                if int(c)==4:
                    impmape.append([int(c),xx+tx*4,yy+ty*4])
                xx+=tx
            except: pass
        yy+=ty
        xx=0
    return mape,inpmape
##################################################################################################################



fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("The Fun Fighting Open Zone")
pygame.key.set_repeat(40,30)

mape=cm()
perso=Perso(tex/2,tey/2)

encour=True
while encour:
    for event in pygame.event.get():
        if event.type==QUIT:
            encour=False
        elif event.type==KEYDOWN:
            if event.key==K_q:
                encour=False
            elif event.key==K_UP: perso.bouger("up")
            elif event.key==K_DOWN: perso.bouger("down")
            elif event.key==K_LEFT: perso.bouger("left")
            elif event.key==K_RIGHT: perso.bouger("right")
            elif event.key==K_SPACE: perso.bouger("jump")
            elif event.key==K_a:
                tx-=10
                ty-=10
                chtt(tx,ty)
            elif event.key==K_z:
                tx+=10
                ty+=10
                chtt(tx,ty)
    aff()













