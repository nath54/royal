#coding:utf-8
import random,pygame,math,time
from pygame.locals import *
from cartes import *
from lib import *

spr=open(fichp,"r").read().split("#")
tex,tey=int(spr[0]),int(spr[1])

tpx,tpy=int(tex/1.5),tey

carts1=[]
carts2=[]
maxelixir=10
miss=[]
sorts=[]
sorps=[]
dtsp=time.time()
cltxt=(215,215,215)
temps=2*60
dtps=time.time()
etps=time.time()
j1ga=False
j2ga=False
jegal=False
modj=False

pygame.init()

fonb=pygame.font.SysFont("Serif",40)

jjr=open("stats.nath","r").read().split("#")

class Joueur:
    def __init__(self,camp):
        self.camp=camp
        self.nom="bot"+str(random.randint(0,100))
        self.deck=[]
        self.cartactu=[]
        self.rcartactu=[]
        self.cartselec=random.randint(0,3)
        self.elixir=0
        self.argent=0
        self.dnel=time.time()
        self.tpel=1.5
        self.trophes=random.randint(10,10000)
        self.cartpos=[]
        self.arene=1
        self.nbtour=3
        self.fpsmax=60
        self.arensl=None


##############
cpdps=ctpp[2:]

j1=Joueur(1)
j1=load(j1)
print(j1.arene)
"""
j1.nom=jjr[0]
ara=jjr[1].split("|")
nar=[]
if len(ara)>1:
    for a in ara: nar.append(int(a))
j1.deck=nar
j1.argent=int(jjr[2])
j1.trophes=int(jjr[3])
j1.arene=int(jjr[5])
ara=jjr[4].split("|")
nar=[]
for a in ara: nar.append(int(a))
j1.cartpos=nar

ara=jjr[6].split("|")
nar=[]
for a in ara: nar.append(int(a))
j1.cartdeb=nar
spr=open(fichp,"r").read().split("#")
tex,tey=int(spr[0]),int(spr[1])
"""
j2=Joueur(2)
if j1.arene==0: j2.tpel=4

if j1.arene==4: cltxt=(0,0,0)

imgfond1=pygame.transform.scale( pygame.image.load("images/mape_"+str(aimg[j1.arene])+"_3.png") ,[int(tex/1.5)+5,tey+50] )
imgfond2=pygame.transform.scale( pygame.image.load("images/mape_"+str(aimg[j1.arene])+"_3.png") ,[int(tex/1.5)+5,tey+50] )
if1x,if1y,if2x,if2y=0,0,int(800/1200*tex),0
imgsol1=pygame.transform.scale( pygame.image.load("images/mape_"+str(aimg[j1.arene])+"_1.png") ,[int(700/1200*tex),int(450/1000*tey)] )
is1x,is1y=int(50/1200*tex),int(50/1000*tey)
imgsol2=pygame.transform.scale( pygame.image.load("images/mape_"+str(aimg[j1.arene])+"_1.png") ,[int(700/1200*tex),int(450/1000*tey)] )
is2x,is2y=int(50/1200*tex),int(550/1000*tey)
imgpon1=pygame.transform.scale( pygame.image.load("images/mape_"+str(aimg[j1.arene])+"_2.png") ,[int(75/1200*tex),int(100/1000*tey)] )
ip1x,ip1y=int(100/1200*tex),int(460/1000*tey)
imgpon2=pygame.transform.scale( pygame.image.load("images/mape_"+str(aimg[j1.arene])+"_2.png") ,[int(75/1200*tex),int(100/1000*tey)] )
ip2x,ip2y=int(600/1200*tex),int(460/1000*tey)

lms=[pygame.Rect(is1x,is1y,700/1200*tex,350/1000*tey),pygame.Rect(is2x,is2y,700/1200*tex,350/1000*tey),pygame.Rect(ip1x,ip1y,75/1200*tex,100/1000*tey),pygame.Rect(ip2x,ip2y,75/1200*tex,100/1000*tey)]

nrmape=lms[0]
nrmape.union(lms[1])
#for zr in lms: nrmape.union(zr)

rmape=pygame.Rect(0,0,int(800/1200*tex),tey)
for rr in lms: rmape.clip(rr)
#print(rmape)


www=0
while len(j2.deck) < 8:
    az=random.choice(cpdps)
    if care[az] <= j1.arene:
        j2.deck.append(az)
        j2.deck=list(set(j2.deck))
    www+=1
    if www>=100:
        j2.deck=j1.deck

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
        self.camp=self.pos.camp
        self.tppos=self.pos.tp
        self.px=int(self.pos.px+self.pos.tx/2)
        self.py=int(self.pos.py+self.pos.ty/2)
        self.tx=mtxx[tp]
        self.ty=mtyy[tp]
        self.cible=cible
        a=(self.px-cible.px)
        b=(self.py-cible.py)
        try: agl=math.degrees(math.tan(a/b))
        except: agl=0
        self.img=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/"+mimg[self.pos.mtp]),[self.tx,self.ty]),agl)
        self.vit=mvit[tp]
        self.inut=False
        self.rect=None
    def ev(self):
        if math.sqrt((self.cible.px-self.px)*(self.cible.px-self.px)+(self.cible.py-self.py)*(self.cible.py-self.py)) > self.vit:
            a=(self.px-self.cible.px)
            b=(self.py-self.cible.py)
            try: agl=math.degrees(math.tan(a/b))
            except: agl=0
            self.img=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/"+mimg[self.pos.mtp]),[self.tx,self.ty]),agl)
            a=-abs(self.cible.px-self.px)
            b=-abs(self.cible.py-self.py)
            c,f=int(math.sqrt(a*a+b*b)),self.vit
            #self.px,self.py=self.px+int(a*f/c),self.py+int(b*f/c)
            if f<c: 
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
        if cond and not self.inut:
            self.inut=True
            self.cible.vie-=self.pos.att
            if self.tp==3:
                self.cible.dnat=time.time()
                self.cible.dbg=time.time()
                self.cible.cible=None
            elif self.tp==4:
                self.cible.etat.append("gelé")
                self.cible.etat=list(set(self.cible.etat))
            elif self.tp==7 and self.tppos==42 and self.cible.tpcarte!=2:
                if self.camp==1: dist=-55
                else: dist=55
                self.cible.py+=dist

def tcs(p):
    for m in lms:
        if m.colliderect(p.recte): return True
    return False

def faf():
        fenetre.fill((0,0,0))
        fenetre.blit(imgfond1,[if1x,if1y])
        fenetre.blit(imgfond2,[if2x,if2y])
        fenetre.blit(imgsol1,[is1x,is1y])
        fenetre.blit(imgsol2,[is1x,is2y])
        fenetre.blit(imgpon1,[ip1x,ip1y])
        fenetre.blit(imgpon1,[ip2x,ip2y])
        pygame.draw.rect(fenetre,(0,0,0),(int(800/1200*tex),0,int(400/1200*tex),tey),0)
        for c in carts1+carts2:
            if c.camp==1: pygame.draw.circle(fenetre,(0,0,150),(int(c.px+c.tx/2),int(c.py+c.ty/1.5)),int(c.tx/2),1)
            else        : pygame.draw.circle(fenetre,(150,0,0),(int(c.px+c.tx/2),int(c.py+c.ty/1.5)),int(c.tx/2),1)
            c.recte=fenetre.blit(c.img,[c.px,c.py])
            if c.vie<c.vie_tot and c.vie_tot>0:
                pygame.draw.rect(fenetre,(250,0,0),(c.px,c.py-10,int(c.vie/c.vie_tot*c.tx),5),0)
                pygame.draw.rect(fenetre,(50,0,0),(c.px,c.py-10,c.tx,5),1)
                if c.tp==0 or c.tp==1 : fenetre.blit(fon.render(str(c.vie)+" / "+str(c.vie_tot),20,(250,250,250)),[c.px,c.py-20])
            if "gelé" in c.etat: fenetre.blit(pygame.transform.scale(pygame.image.load("images/glace.png"),[c.tx,c.ty]),[c.px,c.py])
            if "empoisoné" in c.etat: fenetre.blit(pygame.transform.scale(pygame.image.load("images/emp.png"),[c.tx,c.ty]),[c.px,c.py])
        for m in miss: m.rect=fenetre.blit(m.img,[m.px,m.py])
        pygame.display.update()
    

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
        if ctap[tp]==1:
            self.portee=self.tx+10
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
        self.apcarte=cact[tp]
        self.crcrtdead=cccd[tp]
        self.dbg=time.time()
        self.tbg=0.03
        self.mtp=cims[tp]
        self.cible=None
        self.etat=[]
        self.recte=pygame.Rect(self.px,self.py,self.tx,self.ty)
        self.aaa,self.bbb=random.randint(0,1),random.randint(0,1)
        self.dasp=time.time()
        self.tpasp=0.1
    def atta(self,cible):
        if self.mtp!=None:
            miss.append(Mis(self,cible,self.mtp))
        else:
            cible.vie-=self.att
            #if "énervé" in self.etat: cible.vie-=self.att
            if cible.tpcarte==2 and self.tipeatt==7: cible.vie-=self.att
            if self.tipeatt==2 and self.cible.vie<=0:
                carts1.append( Carte(self.px-self.tx,self.py-self.ty/2,self.tp,self.camp) )
            if self.tipeatt==4 and cible.tp!=26 and not "pondu" in self.etat and len(carts1)+len(carts2)<=100:
                self.etat.append("pondu")
                if self.camp==1:
                    carts1.append( Carte(self.px-self.tx,self.py,self.tp,self.camp) )
                else:
                    carts2.append( Carte(self.px-self.tx,self.py,self.tp,self.camp) )
            if self.tipeatt==5:
                self.vie+=self.att
                if "énervé" in self.etat: self.vie+=self.att
                if "empoisoné" in self.etat: del(self.etat[self.etat.index("empoisoné")])
                if self.vie>=self.vie_tot:
                    cible.vie-=self.vie_tot-self.vie
                    self.vie=self.vie_tot
            if self.tipeatt==12:
                if cible.tpcarte==1:
                    dtfas=False
                    for et in cible.etat:
                        if type(et)==list:
                            if et[0]=="assomé": dtfas=True
                    if not dtfas:
                        cible.etat.append(["assomé",50])
    def attack(self):
        if "énervé" in self.etat: tap=self.vitatt/2
        else: tap=self.vitatt
        if time.time()-self.dnat > tap:
            self.dnat=time.time()
            if self.camp==1: cc=carts2
            else: cc=carts1
            if self.tp==37:
                if self.camp==1:
                    if j1.elixir<10: j1.elixir+=1
                else:
                    if j2.elixir<10: j2.elixir+=1
            if self.apcarte != None:
                if len(carts1+carts2)<=100:
                    if self.camp==1: carts1.append( Carte(self.px+self.tx/2,self.py-self.ty-10,self.apcarte,self.camp) )
                    else: carts2.append( Carte(self.px+self.tx/2,self.py+self.ty+10,self.apcarte,self.camp) )
            tchs=[]
            for c in cc:
                if dtouch(self,c) and c.tpcarte!=3 and c.endroit in self.att_endroit: tchs.append(c)
            if tchs==[]: return False
            if  self.tpatt == 1:
                lpp=tchs[0]
                for c in tchs:
                    if math.sqrt((self.px-c.px)*(self.px-c.px)+(self.py-c.py)*(self.py-c.py)) < math.sqrt((self.px-lpp.px)*(self.px-lpp.px)+(self.py-lpp.py)*(self.py-lpp.py)) and c.endroit in self.att_endroit: lpp=c
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
            if self.tpatt==2:
                for c in tchs:
                    if c.endroit in self.att_endroit:
                        self.atta(c)
                        affattack(self,c)
                        if self.tp==20:
                            if c.tpcarte!=2 and c.tp!=20 and not "cloné" in c.etat:
                                c.etat.append("cloné")
                                if self.camp==1: carts1.append(Carte(c.px+c.tx,c.py,c.tp,1))
                                else           : carts2.append(Carte(c.px+c.tx,c.py,c.tp,2))
            #tipeatt
            
            if self.tipeatt==6:
                if self.camp==1: cc=carts1
                else: cc=carts2
                tchs=[]
                for c in cc:
                    if c.tpcarte == 1 and dtouch(self,c): tchs.append(c)
                for c in tchs:
                    if c.vie < c.vie_tot:
                        c.vie+=self.att
                        if "empoisoné" in c.etat: del(c.etat[c.etat.index("empoisoné")])
                        if c.vie > c.vie_tot: c.vie=c.vie_tot
            if self.tipeatt==7:
                if self.camp==1: cc=carts1
                else: cc=carts2
                tchs=[]
                for c in cc:
                    if dtouch(self,c):
                        if c.tpcarte == 2: tchs.append(c)
                for c in tchs:
                    if c.vie < c.vie_tot:
                        c.vie+=self.att
                        if c.vie > c.vie_tot: c.vie=c.vie_tot
            if self.tipeatt==8 or self.tp==38:
                if c.tpcarte == 1 and not "empoisoné" in c.etat: c.etat.append("empoisoné")
            if self.tipeatt==9:  self.vie=0
            if self.tipeatt==10: self.vie=0
    def dcibl(self):
        lpp=None
        if self.tp==29:
            if self.camp==1: cc=carts1
            else: cc=carts2
            dc=[]
            for c in cc:
                if c.tpcarte==2 and c.vie<c.vie_tot: dc.append(c)
            for c in dc:
                if lpp==None or ( c!=lpp and math.sqrt((self.px-c.px)*(self.px-c.px)+(self.py-c.py)*(self.py-c.py)) < math.sqrt((self.px-lpp.px)*(self.px-lpp.px)+(self.py-lpp.py)*(self.py-lpp.py)) and c.endroit in self.att_endroit ):
                    lpp=c
        if self.tp != 29 or lpp==None:
            cc=carts1+carts2
            for c in cc:
                if lpp==None or ( c!=lpp and math.sqrt((self.px-c.px)*(self.px-c.px)+(self.py-c.py)*(self.py-c.py)) < math.sqrt((self.px-lpp.px)*(self.px-lpp.px)+(self.py-lpp.py)*(self.py-lpp.py)) and c.endroit in self.att_endroit ):
                    if self.camp!=c.camp : lpp=c
        if lpp != None : self.cible=lpp
    def bouger(self):
        if True or self.cible==None: self.dcibl()
        if time.time()-self.dbg>=self.tbg:
          self.dbg=time.time()
          if self.vit!=0 and math.sqrt((self.cible.px-self.px)*(self.cible.px-self.px)+(self.cible.py-self.py)*(self.cible.py-self.py)) > self.portee:
            if "énervé" in self.etat: vitt=self.vit*2
            else: vitt=self.vit
            a=-abs(self.cible.px-self.px)
            b=-abs(self.cible.py-self.py)
            c,f=int(math.sqrt(a*a+b*b)),vitt
            #self.px,self.py=self.px+int(a*f/c),self.py+int(b*f/c)
            if f<c and f > 1.05:
                e=int(b*f/c)
                d=int(a*f/c)
                if self.px > self.cible.px: self.px+=d
                else                      : self.px-=d
                if self.py > self.cible.py: self.py+=e
                else                      : self.py-=e
            else: self.px,self.px=self.px+a,self.py+b
            """
            az=0
            vitt=2
            while (not tcs(self)) and self.endroit==1:
                if self.px >= tex-100: self.px-=vitt
                if self.px <= 100    : self.px+=vitt
                if self.py >= tey-100: self.py-=vitt
                if self.py <= 100    : self.py+=vitt
                self.recte=pygame.Rect(self.px,self.py,self.tx,self.ty)
                az+=vitt
                if az >= 20: break
            """
        df=5
        for c in carts1+carts2:
          if c!=self:
            #if c.px >= self.px-df and c.px <= self.px+df and c.py >= self.py-df and c.py <= self.py+df and c!=self:
            if self.recte==None or True: self.recte=pygame.Rect(self.px,self.py,self.tx,self.ty)
            if c.recte==None or True: c.recte=pygame.Rect(c.px,c.py,c.tx,c.ty)
            vitt=int(1)
            az=0
            while self.endroit == c.endroit and self.recte.colliderect(c.recte):
                if self.tpcarte!=1: break
                else:
                    #if self.aaa: self.px+=1
                    #else       : self.px-=1
                    #if self.bbb: self.py+=1
                    #else       : self.py-=1
                    az=0
                    while c.recte.collidepoint(self.px,self.py) and c.recte.collidepoint(self.px,self.py+self.ty): #côté gauche
                        self.px+=self.vit
                        if self.bbb: self.py-=1
                        else: self.py+=1
                        az+=1
                        if az>=1000:break
                    az=0
                    while c.recte.collidepoint(self.px+self.tx,self.py) and c.recte.collidepoint(self.px+self.tx,self.py+self.ty): #côté droit
                        self.px-=self.vit
                        if self.bbb: self.py-=1
                        else: self.py+=1
                        az+=1
                        if az>=1000:break
                    az=0
                    while c.recte.collidepoint(self.px,self.py) and c.recte.collidepoint(self.px+self.tx,self.py): #côté haut
                        self.py+=self.vit
                        if self.aaa: self.px-=1
                        else: self.px+=1
                        az+=1
                        if az>=1000:break
                    az=0
                    while c.recte.collidepoint(self.px,self.py+self.ty) and c.recte.collidepoint(self.px+self.tx,self.py+self.ty): #côté bas
                        self.py-=self.vit
                        if self.aaa: self.px-=1
                        else: self.px+=1
                        az+=1
                        if az>=1000:break
                    az=0
                    while (self.px==c.px and self.py==c.py) or self.recte.colliderect(c.recte):
                        if self.aaa: self.px+=self.tx+1
                        else: self.px-=self.tx+1
                        if self.bbb: self.py+=self.ty+1
                        else: self.py-=self.ty+1
                        self.recte=pygame.Rect(self.px,self.py,self.tx,self.ty)
                        az+=1
                        if az>=1000:break
                    self.recte=pygame.Rect(self.px,self.py,self.tx,self.ty)
                    az+=1
                    if self.px>800/1200*tex:self.px=800/1200*tex-self.tx-1
                    if self.px<0  :self.px=1
                    if self.py>tex:self.py=tey-self.ty-1
                    if self.py<0  :self.py=1
                    if az >= 1000: break
        if self.px>800/1200*tex:self.px=800/1200*tex-self.tx-1
        if self.px<0  :self.px=1
        if self.py>tex:self.py=tey-self.ty-1
        if self.py<0  :self.py=1
        if self.tipeatt==11:
            if self.camp==1: cc=carts1
            else: cc=carts2
            tchs=[]
            for c in cc:
                if dtouch(self,c) and c!=self: tchs.append(c)
            for c in tchs:
                if not "énervé" in c.etat: c.etat.append("énervé")
        if self.tp==44:
            tchs=[]
            for c in carts1+carts2:    
                if c.camp==self.camp and dtouch(self,c) and c.tpcarte==1:
                    tchs.append(c)
            for c in tchs:
                if not "cloné" in c.etat:
                    c.etat.append("cloné")
                    cart=Carte(c.px,c.py,c.tp,self.camp)
                    cart.etat.append("cloné")
                    if self.camp==2: carts2.append( cart )
                    else: carts1.append( cart )
        if self.tipeatt==11:
            if self.camp==1: cc=carts1
            else: cc=carts2
            tchs=[]
            for c in cc:
                if dtouch(self,c) and c!=self: tchs.append(c)
            for c in tchs:
                if not "énervé" in c.etat: c.etat.append("énervé")
        if self.tp==53:
            tchs=[]
            for c in carts1+carts2:    
                if c.camp==self.camp and dtouch(self,c) and c.tpcarte==1:
                    tchs.append(c)
            for c in tchs:
                if c.vie<c.vie_tot:
                    c.vie+=self.att
        if self.tipeatt==7:
            if time.time()-self.dasp > self.tpasp:
                self.dasp=time.time()
                if self.camp==1: cc=carts1
                else: cc=carts2
                tchs=[]
                for c in cc:
                    if dtouch(self,c):
                        if c.tpcarte == 2: tchs.append(c)
                for c in tchs:
                    if c.vie < c.vie_tot:
                        c.vie+=self.att
                        if c.vie > c.vie_tot: c.vie=c.vie_tot
        self.attack()
        

pause=False

def botpc(j):
    if j.cartselec!=0 and j.cartselec!=1 and j.cartselec!=2 and j.cartselec!=3:
        j.cartselec=random.randint(0,3)
    jcs=j.cartactu[j.cartselec]
    if j.elixir>celi[jcs]:
        if j.camp==2:
            if ctpc[jcs]!=3 and ctpc[jcs]!=4:
                xx,yy=random.randint(0,tex-int(200/1200*tex)),random.randint(0,int(tey/2))
            else:
                if ctpp[jcs]!=52 and ctpc[jcs]!=4: ccc=carts1
                else: ccc=carts2
                if ccc!=[]:
                    cc=random.choice(ccc)
                    xx,yy=cc.px,cc.py
            for x in range(cnbp[jcs]):
                if ctpc[jcs]==4: sorps.append(Carte(xx,yy,jcs,j.camp))
                elif ctpc[jcs]!=3: carts2.append(Carte(xx,yy,jcs,j.camp))
                else: sorts.append( [Carte(xx-30,yy-30,jcs,j.camp),30] )
            j.elixir-=celi[jcs]
            j.cartselec=random.randint(0,3)
            del(j.cartactu[j.cartselec])
        else:
            if ctpc[jcs]!=3 and ctpc[jcs]!=4:
                xx,yy=random.randint(0,tex-int(200/1200*tex)),random.randint(int(tey/2),tey)
            else:
                if ctpp[jcs]!=52 and ctpc[jcs]!=4: ccc=carts2
                else: ccc=carts1
                if ccc!=[]:
                    cc=random.choice(ccc)
                    xx,yy=cc.px,cc.py
            for x in range(cnbp[jcs]):
                if ctpc[jcs]==4: sorps.append(Carte(xx,yy,jcs,j.camp))
                elif ctpc[jcs]!=3: carts1.append(Carte(xx,yy,jcs,j.camp))
                else: sorts.append( [Carte(xx-30,yy-30,jcs,j.camp),30] )
            j.elixir-=celi[jcs]
            j.cartselec=random.randint(0,3)
            del(j.cartactu[j.cartselec])

def bot(j):
    botpc(j)
        
fps=0

fond=pygame.transform.scale(pygame.image.load("images/fond.png"),[tpx,tpy])
font=pygame.font.SysFont("Serif",20)
fon=pygame.font.SysFont("Serif",10)
def aff():
    if not pause:
        fenetre.fill((0,0,0))
        #jeu
        fenetre.blit(imgfond1,[if1x,if1y])
        fenetre.blit(imgfond2,[if2x,if2y])
        fenetre.blit(imgsol1,[is1x,is1y])
        fenetre.blit(imgsol2,[is1x,is2y])
        fenetre.blit(imgpon1,[ip1x,ip1y])
        fenetre.blit(imgpon1,[ip2x,ip2y])
        
        pygame.draw.rect(fenetre,(0,0,0),(int(800/1200*tex),0,int(400/1200*tex),tey),0)
        
        for c in sorps:
            if c.camp==1: cl=(0,0,250)
            else: cl=(250,0,0)
            pygame.draw.circle(fenetre,cl,(int(c.px+c.tx/2),int(c.py+c.ty/2)),int(c.tx/2),1)
            fenetre.blit(c.img,[c.px,c.py])
            if c.vie<c.vie_tot and c.vie_tot>0 and c.vie >= 0:
                pygame.draw.rect(fenetre,(0,150,150),(c.px,c.py-10,int(c.vie/c.vie_tot*c.tx),5),0)
                pygame.draw.rect(fenetre,(0,50,50),(c.px,c.py-10,c.tx,5),1)
        
        for c in carts1+carts2:
            if c.camp==1: pygame.draw.circle(fenetre,(0,0,150),(int(c.px+c.tx/2),int(c.py+c.ty/1.5)),int(c.tx/2),1)
            else        : pygame.draw.circle(fenetre,(150,0,0),(int(c.px+c.tx/2),int(c.py+c.ty/1.5)),int(c.tx/2),1)
            c.recte=fenetre.blit(c.img,[c.px,c.py])
            if c.vie<c.vie_tot and c.vie_tot>0 and c.vie >= 0:
                pygame.draw.rect(fenetre,(250,0,0),(c.px,c.py-10,int(c.vie/c.vie_tot*c.tx),5),0)
                pygame.draw.rect(fenetre,(50,0,0),(c.px,c.py-10,c.tx,5),1)
                if c.tp==0 or c.tp==1 : fenetre.blit(fon.render(str(c.vie)+" / "+str(c.vie_tot),20,cltxt),[c.px,c.py-20])
            if "gelé" in c.etat: fenetre.blit(pygame.transform.scale(pygame.image.load("images/glace.png"),[c.tx,c.ty]),[c.px,c.py])
            if "empoisoné" in c.etat: fenetre.blit(pygame.transform.scale(pygame.image.load("images/emp.png"),[c.tx,c.ty]),[c.px,c.py])
            if "énervé" in c.etat: fenetre.blit(pygame.transform.scale(pygame.image.load("images/rage.png"),[c.tx,c.ty]),[c.px,c.py])
            dtfas=False
            for et in c.etat:
                if type(et)==list:
                    if et[0]=="assomé": dtfas=True
            if dtfas: fenetre.blit(pygame.transform.scale(pygame.image.load("images/zzz.png"),[c.tx,c.ty]),[c.px,c.py])
        for m in miss: m.rect=fenetre.blit(m.img,[m.px,m.py])
        for ss in sorts:
            s=ss[0]
            if s.camp==1: cl=(0,0,250)
            else: cl=(250,0,0)
            pygame.draw.circle(fenetre,cl,(int(s.px+s.tx/2),int(s.py+s.ty/2)),int(s.tx/2),1)
            fenetre.blit(s.img,[s.px,s.py])
        
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
        #statsgame
        fenetre.blit(font.render(j1.nom+" : "+str(3-j2.nbtr),20,(0,0,250)),[rx(20),ry(20)])
        fenetre.blit(font.render(j2.nom+" : "+str(3-j1.nbtr),20,(250,0,0)),[rx(220),ry(20)])
        if temps > 5: fenetre.blit(font.render(str(temps)+" sec restantes",20,(250,0,250)),[rx(420),ry(20)])
        else: fenetre.blit(fonb.render(str(temps)+" sec restantes",20,(250,0,250)),[rx(300),ry(500)])
        fenetre.blit(font.render("fps : "+str(fps),20,(200,200,200)),[rx(1100),ry(965)])
    pygame.display.update()


def cm():
    carts1.append( Carte(int(105/1200*tex),int(700/1000*tey),0,1) )
    carts1.append( Carte(int(575/1200*tex),int(700/1000*tey),0,1) )
    carts1.append( Carte(int(350/1200*tex),int(800/1000*tey),1,1) )
    carts2.append( Carte(int(105/1200*tex),int(170/1000*tey),0,2) )
    carts2.append( Carte(int(575/1200*tex),int(170/1000*tey),0,2) )
    carts2.append( Carte(int(350/1200*tex),int(70/1000*tey),1,2) )

def bb():
    global if1x,if2x,dtps,temps,dtsp,etps
    if1x+=1
    if2x+=1
    if if1x >= 800/1200*tex: if1x=-800/1200*tex
    if if2x >= 800/1200*tex: if2x=-800/1200*tex
    if time.time()-dtps >= 1:
        temps-=1
        dtps=time.time()
    bs=2
    for ss in sorts:
        s=ss[0]
        ss[1]-=bs
        s.px+=bs
        s.py+=bs
        if ss[1]<=0:
            if s.camp==1:
                if s.tp==52: cc1,cc2=carts1,carts1
                else: cc1,cc2=carts2,carts1
            else:
                if s.tp==52: cc1,cc2=carts2,carts2
                else: cc1,cc2=carts1,carts2
            for c in cc1:
                if dtouch(s,c):
                    c.vie-=s.att
                    if s.tipeatt==8 and c.tpcarte==1: c.etat.append("empoisoné")
                    elif s.tipeatt==9 and c.tpcarte==1: c.etat.append("gelé")
                    elif s.tp==52: c.etat.append("énervé")
            if s.crcrtdead != None:
                for x in range(s.crcrtdead[0]): cc2.append( Carte(s.px,s.py,s.crcrtdead[1],s.camp) )
            del(sorts[sorts.index(ss)])
    for sp in sorps:
        if sp.vie <= 0:
            del(sorps[sorps.index(sp)])
        if time.time()-dtsp >= 1:
            dtsp=time.time()
            sp.vie-=1
        sp.bouger()
    for c1 in carts1:
        dtfas=False
        for et in c1.etat:
            if type(et)==list:
                if et[0]=="assomé":
                    dtfas=True
                    if time.time()-etps >= 1:
                        et[1]-=1
                        if et[1]<=0:
                            try: del(c1.etat[c1.etat.index(et)])
                            except: pass
        if not "gelé" in c1.etat and not dtfas:
            c1.bouger()
        if "empoisoné" in c1.etat: c1.vie-=1
        if c1.vie<=0:
            if c1.crcrtdead != None:
                for x in range(c1.crcrtdead[0]): carts1.append( Carte(c1.px,c1.py,c1.crcrtdead[1],c1.camp) )
            if c1.tp==41 or c1.tp==51:
                porte=125
                fenetre.blit(pygame.transform.scale(pygame.image.load("images/explose.png"),[int(2*porte/1200*tex),int(2*porte/1000*tey)]),[int(c1.px-porte/2),int(c1.py-porte/2)])
                pygame.display.update()
                for c in carts2:
                    if math.sqrt((c1.px-c.px)*(c1.px-c.px)+(c1.py-c.py)*(c1.py-c.py)) < porte: c.vie-=c1.att
            del(carts1[carts1.index(c1)])
        if c1.px>800/1200*tex:c1.px=800/1200*tex-c1.tx-1
        if c1.px<0  :c1.px=1
        if c1.py>tex:c1.py=tey-c1.ty-1
        if c1.py<0  :c1.py=1
        if c1.tpcarte==2 and (c1.tp!=0 and c1.tp!=1):
            c1.vie-=1
    for c2 in carts2:
        dtfas=False
        for et in c2.etat:
            if type(et)==list:
                if et[0]=="assomé":
                    dtfas=True
                    if time.time()-etps >= 1:
                        et[1]-=1
                        if et[1]<=0:
                            try: del(c2.etat[c2.etat.index(et)])
                            except: pass
        if not "gelé" in c2.etat and not dtfas:
            c2.bouger()
        if "empoisoné" in c2.etat: c2.vie-=1
        if c2.vie<=0:
            if c2.crcrtdead != None:
                for x in range(c2.crcrtdead[0]): carts2.append( Carte(c2.px,c2.py,c2.crcrtdead[1],c2.camp) )
            if c2.tp==41 or c2.tp==51:
                porte=125
                fenetre.blit(pygame.transform.scale(pygame.image.load("images/explose.png"),[int(2*porte/1200*tex),int(2*porte/1000*tey)]),[int(c2.px-porte/2),int(c2.py-porte/2)])
                pygame.display.update()
                for c in carts1:
                    if math.sqrt((c2.px-c.px)*(c2.px-c.px)+(c2.py-c.py)*(c2.py-c.py)) < porte: c.vie-=c2.att
            del(carts2[carts2.index(c2)])
        if c2.px>800/1200*tex:c2.px=800/1200*tex-c2.tx-1
        if c2.px<0  :c2.px=1
        if c2.py>tex:c2.py=tey-c2.ty-1
        if c2.py<0  :c2.py=1
        if c2.tpcarte==2 and (c2.tp!=0 and c2.tp!=1):
            c2.vie-=1
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
    while len(j1.cartactu) < 4:
        azz=random.choice(j1.deck)
        if not azz in j1.cartactu: j1.cartactu.append(azz)
    while len(j2.cartactu) < 4:
        azz=random.choice(j2.deck)
        if not azz in j2.cartactu: j2.cartactu.append(azz)
    if time.time()-etps >= 1:
        etps=time.time()

def deb():
    t=time.time()
    tt=time.time()
    ff=pygame.font.SysFont("Segoe",40)
    ct=(150,45,20)
    while tt-t <= 3:
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/vs.png"),[tex,tey]),[0,0])
        fenetre.blit(ff.render(str(3-int(tt-t)),40,ct),[tex/2,50])
        fenetre.blit(ff.render(j1.nom,40,(5,5,5)),[tex/4*1,tey/3*1])
        fenetre.blit(ff.render("bot",40,(5,5,5)),[tex/4*3,tey/3*2])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/por0.png"),[int(150/1200*tex),int(150/1000*tey)]),[tex/4*1-160,tey/3*1])
        pygame.draw.rect(fenetre,(250,250,250),(tex/4*1-160,tey/3*1,int(150/1200*tex),int(150/1000*tey)),5)
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/por0.png"),[int(150/1200*tex),int(150/1000*tey)]),[tex/4*3-160,tey/3*2])
        pygame.draw.rect(fenetre,(250,250,250),(tex/4*3-160,tey/3*2,int(150/1200*tex),int(150/1000*tey)),5)
        pygame.display.update()
        tt=time.time()

#def countr(crts):
#    nb=0
#    for c in crts:
#        if c.tp==0 or c.tp==1: nb+=1
#    return nb

def countr():
    nbt1=0
    nbt2=0
    for c in carts1+carts2:
        if c.tp==0 or c.tp==1:
            if c.camp==1: nbt1+=1
            else: nbt2+=1
    return nbt1,nbt2
        

def vcp(x,y,tx,ty):
    re=pygame.Rect(x,y,tx,ty)
    for c in carts1+carts2:
        if c.tpcarte==2 and re.colliderect(pygame.Rect(c.px,c.py,c.tx,c.ty)): return True
    return False

#######################################################

fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("THE CLASH OF FIGHTERS")
fpsClock = pygame.time.Clock()

deb()
cm()


encour=True
while encour:
    tit=time.time()
    if carts2==[] or carts1==[]:
        encour=False
        encour2=True
    j1.nbtr,j2.nbtr=countr()
    aff()
    bb()
    bot(j2)
    if modj: bot(j1)
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
                if ctpc[jcs]!=3 and ctpc[jcs]!=4: cond=cond1
                else: cond=cond2
                if cond:
                    if j1.elixir >= celi[jcs]:
                        if not vcp(pos[0],pos[1],ctxx[jcs],ctyy[jcs]) or ctpc[jcs]==1 or ctpc[jcs]==3 or ctpc[jcs]==4:
                            if ctpc[jcs]==3:
                                sa=40
                                sorts.append( [Carte(pos[0]-sa,pos[1]-sa,jcs,1),sa] )
                                j1.elixir-=celi[jcs]
                                del(j1.cartactu[j1.cartselec])
                                j1.cartselec=None
                            elif ctpc[jcs]==4:
                                sorps.append( Carte(pos[0],pos[1],jcs,1) )
                                j1.elixir-=celi[jcs]
                                del(j1.cartactu[j1.cartselec])
                                j1.cartselec=None
                            else:
                                for x in range(cnbp[jcs]): carts1.append( Carte(pos[0],pos[1],jcs,1) )
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
            elif event.key==K_SPACE: modj=not modj
            elif event.key==K_p: print(countr(),j1.nbtr,j2.nbtr)
    atp=0.8
    if j1.nbtr == 0 or carts1==[]:
        encour=False
        j2ga=True
        time.sleep(atp)
    if j2.nbtr == 0 or carts2==[]:
        encour=False
        j1ga=True
        time.sleep(atp)
    if temps <= 0:
        if j1.nbtour>j2.nbtour: j1ga=True
        elif j1.nbtour<j2.nbtour: j2ga=True
        else: jegal=True
        encour=False
        time.sleep(atp)
    fpsClock.tick(j1.fpsmax)
    tiit=time.time()
    fps=int(1.0/(tiit-tit))

"""
def save(j):
    ff=open("stats.nath","w")
    t1=str(j.nom)
    t2=""
    for jj in j.deck:
        t2+=str(jj)+"|"
    t2=t2[:-1]
    t3=str(j.argent)
    t4=str(j.trophes)
    t5=""
    for jj in j.cartpos:
        t5+=str(jj)+"|"
    t5=t5[:-1]
    t6=str(j.arene)
    t7=""
    for jj in j.cartdeb: t7+=str(jj)+"|"
    t7=t7[:-1]
    txt=t1+"#"+t2+"#"+t3+"#"+t4+"#"+t5+"#"+t6+"#"+t7+"#"
    ff.write(txt)
    ff.close()
"""

fenetre.fill((0,0,0))
img="images/perdu.png"
encour2=False
arg,tro=0,0
vict=0
if jegal or countr()[0]==countr()[1]:
    img="images/egal.png"
    encour2=True
    arg=random.randint(10,30)
    epx=random.randint(0,10)
    tro=0
    j1.argent+=arg
    j1.exp+=epx
if carts2==[] or j1ga or j1.nbtour>j2.nbtour or countr()[0]>countr()[1]:
    img="images/gagné.png"
    encour2=True
    arg=random.randint(20,60)
    tro=random.randint(20,40)
    epx=random.randint(20,60)
    j1.argent+=arg
    j1.trophes+=tro
    j1.exp+=epx
    fenetre.blit(font.render("vous avez gagné "+str(tro)+" trophés",20,(10,10,10)),[tex/1.5,tey/1.2])
    vict=1
if carts1==[] or j2ga or j1.nbtour<j2.nbtour or countr()[0]<countr()[1]:
    img="images/perdu.png"
    encour2=True
    arg=random.randint(0,10)
    tro=random.randint(20,30)
    epx=random.randint(0,10)
    j1.argent+=arg
    j1.trophes-=tro
    j1.exp+=epx
    if j1.trophes < 0: j1.trophes=0
    fenetre.blit(font.render("vous avez perdu "+str(abs(tro))+" trophés",20,(10,10,10)),[tex/1.5,tey/1.2])
    vict=2

for cc in j1.deck:
    if j1.cartpos[cc] >= 1: j1.cartpos[cc]-=1

save(j1)
rhisto(j1.deck,j2.deck,vict,countr()[0],countr()[1],j1.nom,j2.nom,1)

fenetre.blit(pygame.transform.scale(pygame.image.load(img),[tex,tey]),[0,0])
bmenu=fenetre.blit(pygame.transform.scale(pygame.image.load("images/bmenu.png"),[int(100/1200*tex),int(50/1000*tey)]),[tex/2,tey/2])
fenetre.blit(font.render("vous avez gagné "+str(arg)+" or",20,(150,150,10)),[tex-650,tey-200])
fenetre.blit(font.render("vous avez gagné "+str(tro)+" trophés",20,(150,150,10)),[tex-650,tey-150])
fenetre.blit(font.render("vous avez gagné "+str(epx)+" experience",20,(150,150,10)),[tex-650,tey-100])

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

save(j1)
save(j1)




