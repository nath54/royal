#coding:utf-8
import random,pygame,math,time
from pygame.locals import *

tex,tey=1000,800

tpx,tpy=int(tex/1.5),tey

carts1=[]
carts2=[]
maxelixir=10
miss=[]

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
cpdps=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
j1.deck=cpdps
j2.deck=cpdps

from cartes import *
#rar: 0=commun , 1=rare , 2=epique , 3=legendaire , 4=dieu

def affattack(p1,p2):
    if p1.camp==1: cc=(0,0,250)
    else: cc=(250,0,0)
    #pygame.draw.line(fenetre,cc,(p1.px,p1.py),(p2.px,p2.py),1)
    #pygame.display.update()

def dtouch(c1,c2):
    if c1.camp==1: cl=(0,0,200)
    else           : cl=(200,0,0)
    rr=pygame.draw.circle(fenetre,cl,(int(c1.px+c1.tx/2),int(c1.py+c1.ty/2)),c1.portee,1)
    if rr.colliderect(c2.px,c2.py,c2.tx,c2.ty): return True
    return False

class Mis:
    def __init__(self,pos,cible,tp):
        self.tp=tp
        self.pos=pos
        self.px=int(self.pos.px+self.pos.tx/2)
        self.py=int(self.pos.py+self.pos.ty/2)
        self.tx=mtxx[tp]
        self.ty=mtyy[tp]
        self.cible=cible
        try: 
            aa=float((float(self.py)-float(self.cible.py))/(float(self.px)-float(self.cible.px)))
        except: aa=1
        agl=math.atan(aa)
        self.img=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/"+mimg[self.pos.mtp]),[self.tx,self.ty]),agl)
        self.vit=mvit[tp]
        self.inut=False
        self.rect=None
    def ev(self):
        if math.sqrt((self.cible.px-self.px)*(self.cible.px-self.px)+(self.cible.py-self.py)*(self.cible.py-self.py)) > self.vit:
            a=-abs(self.cible.px-self.px)
            b=-abs(self.cible.py-self.py)
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
        else:
            self.px+=self.cible.px-self.px
            self.py+=self.cible.py-self.py
        if self.rect==None: cond=pygame.Rect(self.px,self.py,self.tx,self.ty).colliderect(pygame.Rect(self.cible.px,self.cible.py,self.cible.tx,self.cible.ty))
        else: cond=self.rect.colliderect(pygame.Rect(self.cible.px,self.cible.py,self.cible.tx,self.cible.ty))
        if cond:
            self.inut=True
            self.cible.vie-=self.pos.att
            if self.tp==3:
                self.cible.dnat=time.time()
                self.cible.cible=None
            elif self.tp==4:
                self.cible.etat.append("gelé")
                self.cible.etat=list(set(self.cible.etat))

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
        self.tipeatt=cpta[tp]
        self.endroit=cend[tp]
        self.att_endroit=caen[tp]
        self.tpcarte=ctpc[tp]
        self.mtp=cims[tp]
        self.cible=None
        self.etat=[]
        if self.tpcarte==3:
            for x in range(1,30):
                fenetre.blit(self.img,[self.px-((30-x)*2),self.py-((30-x)*3)])
                time.sleep(0.015)
                pygame.display.update()
            fenetre.blit(pygame.image.load("images/explose.png"),[self.px,self.py])
            pygame.display.update()
            if self.camp==1: cl=(0,0,200)
            else           : cl=(200,0,0)
            rr=pygame.draw.circle(fenetre,cl,(int(self.px+self.tx/2),int(self.py+self.ty/2)),self.portee,1)
            if self.camp==1: cc=carts2
            else: cc=carts1
            tchs=[]
            for c in cc:
                if rr.colliderect(pygame.Rect(c.px,c.py,c.tx,c.ty)): tchs.append(c)
            if tchs!=[]:
                if self.tpatt==2:
                    for c in tchs: c.vie-=self.att
                else:
                    lpp=tchs[0]
                    for c in tchs:
                        if abs(self.px-c.px) < abs(self.px-lpp.px) and abs(self.py-c.py) < abs(self.py-lpp.py): lpp=c
                    lpp.vie-=self.att
            pygame.display.update()
    def atta(self,cible):
        if self.mtp!=None:
            miss.append(Mis(self,cible,self.mtp))
        else:
            cible.vie-=self.att
            if self.tipeatt==2 and self.cible.vie<=0:
                carts1.append( Carte(self.px-self.tx,self.py-self.ty/2,self.tp,self.camp) )
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
                    if lpp.px-self.px < c.px-self.px and lpp.py-self.py < c.py-self.py and c.endroit in self.att_endroit: lpp=c
                self.atta(lpp)
                affattack(self,lpp)
                if self.tp==13:
                    lpp.cible=None
                    if self.camp==1:
                        del(carts2[carts2.index(lpp)])
                        lpp.camp=1
                        carts1.append(lpp)
                    else:
                        del(carts1[carts1.index(lpp)])
                        lpp.camp=2
                        carts2.append(lpp)
            elif self.tpatt==2:
                for c in tchs:
                    if c.endroit in self.att_endroit:
                        self.atta(c)
                        affattack(self,c)
                        if self.tp==20:
                            if c.tpcarte!=2 and c.tp!=20 and not "cloné" in c.etat:
                                c.etat.append("cloné")
                                if self.camp==1: carts1.append(Carte(c.px+c.tx,c.py,c.tp,1))
                                else           : carts2.append(Carte(c.px+c.tx,c.py,c.tp,2))
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
          if math.sqrt((self.cible.px-self.px)*(self.cible.px-self.px)+(self.cible.py-self.py)*(self.cible.py-self.py)) > self.portee:
            a=-abs(self.cible.px-self.px)
            b=-abs(self.cible.py-self.py)
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
    jcs=j.cartactu[j.cartselec]
    if j.elixir>celi[jcs]:
        if j.camp==2:
            if ctpc[jcs]!=3:
                if aa: xx,yy=650/1200*tex,400/1000*tey
                else: xx,yy=150/1200*tex,400/1000*tey
            else:
                if carts1!=[]:
                    cc=random.choice(carts1)
                    xx,yy=cc.px,cc.py
            for x in range(cnbp[jcs]):
                dp1=random.randint(-1,1)*ctxx[jcs]
                dp2=random.randint(-1,1)*ctxx[jcs]
                carts2.append(Carte(xx-x*dp1,yy-dp1*x,jcs,2))
            j.elixir-=celi[jcs]
            del(j.cartactu[j.cartselec])
        else:
            if cptc[jcs]!=3:
                if aa: xx,yy=650/1200*tex,600/1000*tey
                else: xx,yy=150/1200*tex,600/1000*tey
            else:
                if carts1!=[]:
                    cc=random.choice(carts2)
                    xx,yy=cc.px,cc.py
            carts1.append(Carte(xx,yy,jcs,1))
            j.elixir-=celi[jcs]
            del(jcs)

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
            if "gelé" in c.etat: fenetre.blit(pygame.transform.scale(pygame.image.load("images/glace.png"),[c.tx,c.ty]),[c.px,c.py])
        for m in miss: m.rect=fenetre.blit(m.img,[m.px,m.py])
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
        if not "gelé" in c1.etat:
            c1.bouger()
        if c1.vie<=0: del(carts1[carts1.index(c1)])
    for c2 in carts2:
        if not "gelé" in c2.etat:
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
    for m in miss:
        if m.inut: del(miss[miss.index(m)])
        m.ev()
    while len(j1.cartactu) < 4: j1.cartactu.append(random.choice(j1.deck))
    while len(j2.cartactu) < 4: j2.cartactu.append(random.choice(j2.deck))

#######################################################

fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("THE FUN FIGHTING")

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
            if j1.cartselec!=None:
                jcs=j1.cartactu[j1.cartselec]
                cond1=pos[0] >= 0 and pos[0] <= tpx and pos[1] >= tpy/2
                cond2=pos[0] >= 0 and pos[0] <= tpx
                if ctpc[jcs]!=3: cond=cond1
                else: cond=cond2
                if cond:
                    if  j1.elixir >= celi[jcs]:
                        for x in range(cnbp[jcs]):
                            dp1=random.randint(-1,1)*ctxx[jcs]
                            dp2=random.randint(-1,1)*ctxx[jcs]
                            carts1.append( Carte(pos[0]+dp1*x,pos[1]+dp2*x,jcs,1) )
                        j1.elixir-=celi[jcs]
                        del(j1.cartactu[j1.cartselec])
                        j1.cartselec=None
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
bmenu=fenetre.blit(pygame.transform.scale(pygame.image.load("images/bmenu.png"),[int(100/1200*tex),int(50/1000*tey)]),[tex/2,tey/2])
pygame.display.update()

while encour2:
    for event in pygame.event.get():
        if event.type==QUIT: encour2=False
        elif event.type==KEYDOWN:
            if event.key==K_q: encour2=False
        elif event.type==MOUSEBUTTONUP:
            p=pygame.mouse.get_pos()
            rpos=pygame.Rect(p[0],p[1],1,1)
            if rpos.colliderect(bmenu): encour2=False








