#coding:utf-8
import random,pygame,math,time
from pygame.locals import *

tex,tey=1000,800

tpx,tpy=int(tex/1.5),tey

carts1=[]
carts2=[]
maxelixir=10
pygame.init()

class Joueur:
    def __init__(self,camp):
        self.camp=camp
        self.nom=None
        self.deck=[]
        self.cartactu=[]
        self.rcartactu=[]
        self.cartselec=None
        self.elixir=0
        self.argent=0
        self.dnel=time.time()
        self.tpel=1.5

j1=Joueur(1)
j2=Joueur(2)
cpdps=[2,3,4,5,6,7,8,9,10,11,12]
j1.deck=cpdps
j2.deck=cpdps

from cartes import *
#rar: 0=commun , 1=rare , 2=epique , 3=legendaire , 4=dieu

def affattack(p1,p2):
    if p1.camp==1: cc=(0,0,250)
    else: cc=(250,0,0)
    pygame.draw.line(fenetre,cc,(p1.px,p1.py),(p2.px,p2.py),1)
    pygame.display.update()

def dtouch(c1,c2):
    if pygame.Rect(c1.px-c1.portee,c1.py-c1.portee,c1.tx+c1.portee,c1.ty+c1.portee).colliderect(c2.px,c2.py,c2.tx,c2.ty): return True
    return False

class Carte:
    def __init__(self,x,y,tp,camp):
        self.tp=tp
        self.camp=camp
        self.nom=cnom[tp]
        self.px=x
        self.py=y
        self.tx=ctxx[tp]
        self.ty=ctyy[tp]
        self.att=catt[tp]
        self.vitatt=cvat[tp]
        self.vie_tot=cvie[tp]
        self.vie=cvie[tp]
        self.portee=cpor[tp]
        self.vit=cvit[tp]
        self.img=pygame.transform.scale( pygame.image.load("images/"+cimg[tp]),[self.tx,self.ty])
        self.rarete=crar[tp]
        self.elixir=celi[tp]
        self.dnat=time.time()
        self.tpatt=ctpa[tp]
        self.cible=None
    def attack(self):
      if time.time()-self.dnat > self.vitatt:
        self.dnat=time.time()
        if self.camp==1: cc=carts2
        else: cc=carts1
        tchs=[]
        for c in cc:
            if dtouch(self,c): tchs.append(c)
        if tchs==[]: return False
        if  self.tpatt == 1:
            lpp=tchs[0]
            for c in tchs:
                if lpp.px-self.px < c.px-self.px and lpp.py-self.py < c.py-self.py: lpp=c
            lpp.vie-=self.att
            affattack(self,lpp)
        elif self.tpatt==2:
            for c in tchs:
                c.vie-=self.att
                affattack(self,c)
    def dcibl(self):
        if self.camp==1: cc=carts2
        else: cc=carts1
        if cc!=[]:
            lpp=cc[0]
            for c in cc:
                if abs(self.px-c.px) <= abs(self.px-lpp.px) and abs(self.py-c.py) <= abs(self.py-lpp.py): lpp=c
            self.cible=lpp
    def bouger(self):
        if self.cible==None or self.cible.vie<=0: self.dcibl()
        else:
          if abs(self.px-self.cible.px) > self.portee or abs(self.py-self.cible.py) > self.portee:
            if self.cible.px<=self.px: a=self.cible.px-self.px
            else                     : a=self.px-self.cible.px
            if self.cible.py<=self.py: b=self.cible.py-self.py
            else                     : b=self.py-self.cible.py
            c,f=int(math.sqrt(a*a+b*b)),self.vit
            if f<c: #self.px,self.py=self.px+int(a*f/c),self.py+int(b*f/c)
                e=int(b*f/c)
                d=int(a*f/c)
                if self.px > self.cible.px: self.px+=d
                else                      : self.px-=d
                if self.py > self.cible.py: self.py+=e
                else                      : self.py-=e
            else: self.px,self.px=self.px+a,self.py+b
            if  self.px>=tpx-self.tx: self.px=tpx-self.tx
            elif self.px <= 0: self.px=0
            if  self.py>=tpy-self.ty: self.py=tpy-self.ty
            elif self.py <= 0: self.py=0
        self.attack()
        

pause=False

def botpc(j,aa):
    j.cartselec=random.randint(0,3)
    if j.elixir>celi[j.cartactu[j.cartselec]]:
        if j.camp==2:
            if aa: xx,yy=650/1200*tex,400/1000*tey
            else: xx,yy=150/1200*tex,400/1000*tey
            for x in range(cnbp[j.cartactu[j.cartselec]]):
                dp1=random.randint(-1,1)*ctxx[j.cartactu[j.cartselec]]
                dp2=random.randint(-1,1)*ctxx[j.cartactu[j.cartselec]]
                carts2.append(Carte(xx-x*dp1,yy-dp1*x,j.cartactu[j.cartselec],2))
            j.elixir-=celi[j.cartactu[j.cartselec]]
            del(j.cartactu[j.cartselec])
        else:
            if aa: xx,yy=650/1200*tex,600/1000*tey
            else: xx,yy=150/1200*tex,600/1000*tey
            carts1.append(Carte(xx,yy,j.cartactu[j.cartselec],1))
            j.elixir-=celi[j.cartactu[j.cartselec]]
            del(j.cartactu[j.cartselec])

def bot(j):
    botpc(j,random.randint(0,1))
        
            

fond=pygame.transform.scale(pygame.image.load("images/fond.png"),[tpx,tpy])
font=pygame.font.SysFont("Serif",20)
def aff():
    if not pause:
        fenetre.fill((0,0,0))
        #jeu
        fenetre.blit(fond,[0,0])
        for c in carts1+carts2:
            if c.camp==1: pygame.draw.circle(fenetre,(0,0,150),(int(c.px+c.tx/2),int(c.py+c.ty/1.5)),int(c.tx/2),1)
            else        : pygame.draw.circle(fenetre,(150,0,0),(int(c.px+c.tx/2),int(c.py+c.ty/1.5)),int(c.tx/2),1)
            fenetre.blit(c.img,[c.px,c.py])
            if c.vie<c.vie_tot:
                pygame.draw.rect(fenetre,(250,0,0),(c.px,c.py-10,int(c.vie/c.vie_tot*c.tx),5),0)
                pygame.draw.rect(fenetre,(50,0,0),(c.px,c.py-10,c.tx,5),1)
            
        #interface
        ky=50
        dd=0
        for c in j1.cartactu:
            m=fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[c]),[int(50/1200*tex),int(70/1000*tey)]),[int(850/1200*tex),int(ky/1000*tey)])
            j1.rcartactu.append(m)
            if celi[c]<=j1.elixir : fenetre.blit(font.render(str(celi[c]),20,(150,20,150)),[1000/1200*tex,ky/1000*tey])
            else                  : fenetre.blit(font.render(str(celi[c]),20,(250,5,20)),[1000/1200*tex,ky/1000*tey])
            if j1.cartselec==dd: pygame.draw.rect(fenetre,(50,50,150),(850/1200*tex,ky/1000*tey,50/1200*tex,70/1000*tey),5)
            else: pygame.draw.rect(fenetre,(150,150,150),(850/1200*tex,ky/1000*tey,50/1200*tex,70/1000*tey),5)
            ky+=140
            dd+=1
        pygame.draw.rect(fenetre,(120,10,120),(1100/1200*tex,50/1000*tey,50/1200*tex,j1.elixir/maxelixir*750/1000*tey),0)
        pygame.draw.rect(fenetre,(250,250,250),(1100/1200*tex,50/1000*tey,50/1200*tex,750/1000*tey),5)
        fenetre.blit(font.render(str(j1.elixir)+"/"+str(maxelixir),20,(150,20,150)),[1100/1200*tex,800/1000*tey])
    pygame.display.update()


def cm():
    carts1.append( Carte(105/1200*tex,750/1000*tey,0,1) )
    carts1.append( Carte(575/1200*tex,750/1000*tey,0,1) )
    carts1.append( Carte(350/1200*tex,850/1000*tey,1,1) )
    carts2.append( Carte(105/1200*tex,250/1000*tey,0,2) )
    carts2.append( Carte(575/1200*tex,250/1000*tey,0,2) )
    carts2.append( Carte(350/1200*tex,100/1000*tey,1,2) )

def bb():
    for c1 in carts1:
        c1.bouger()
        if c1.vie<=0: del(carts1[carts1.index(c1)])
    for c2 in carts2:
        c2.bouger()
        if c2.vie<=0: del(carts2[carts2.index(c2)])
    if time.time()-j1.dnel > j1.tpel:
        j1.dnel=time.time()
        j1.elixir+=1
        if j1.elixir>=maxelixir: j1.elixir=maxelixir
    if time.time()-j2.dnel > j2.tpel:
        j2.dnel=time.time()
        j2.elixir+=1
        if j2.elixir>=maxelixir: j2.elixir=maxelixir
    while len(j1.cartactu) < 4: j1.cartactu.append(random.choice(j1.deck))
    while len(j2.cartactu) < 4: j2.cartactu.append(random.choice(j2.deck))

#######################################################

fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("COMBAT ROYAL")

cm()

encour=True
while encour:
    if carts2==[] or carts1==[]:
        encour=False
        encour2=True
    aff()
    bb()
    bot(j2)
    for event in pygame.event.get():
        if event.type==QUIT:
            encour=False
        elif event.type==MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            rpos=pygame.Rect(pos[0],pos[1],1,1)
            if pos[0] >= 0 and pos[0] <= tpx and pos[1] >= tpy/2:
                if j1.cartselec != None and j1.elixir >= celi[j1.cartactu[j1.cartselec]]:
                    for x in range(cnbp[j1.cartactu[j1.cartselec]]):
                        dp1=random.randint(-1,1)*ctxx[j1.cartactu[j1.cartselec]]
                        dp2=random.randint(-1,1)*ctxx[j1.cartactu[j1.cartselec]]
                        carts1.append( Carte(pos[0]+dp1*x,pos[1]+dp2*x,j1.cartactu[j1.cartselec],1) )
                    j1.elixir-=celi[j1.cartactu[j1.cartselec]]
                    del(j1.cartactu[j1.cartselec])
                    j1.cartselec=None
            else:
                for cs in j1.rcartactu:
                    if cs.colliderect(rpos):
                        j1.cartselec=j1.rcartactu.index(cs)
                        break
        elif event.type==KEYDOWN:
            if event.key==K_q:
                encour=False


fenetre.fill((0,0,0))
img="images/perdu.png"
encour2=False
if carts2==[]:
    img="images/gagné.png"
    encour2=True
elif carts1==[]:
    img="images/perdu.png"
    encour2=True
fenetre.blit(pygame.transform.scale(pygame.image.load(img),[tex,tey]),[0,0])
pygame.display.update()

while encour2:
    for event in pygame.event.get():
        if event.type==QUIT: encour2=False
        elif event.type==KEYDOWN:
            if event.key==K_q: encour2=False








