#coding:utf-8
import pygame,time,os,random
from pygame.locals import *
from cartes import *

pygame.init()
tex,tey=1200,900
smenu=2
cselec=None


font=pygame.font.SysFont("Serif",20)

rarete=["commun","rare","epique","legendaire","divin"]
craret=[(0,0,140),(150,105,25),(150,0,150),(20,150,20),(250,250,0)]

jjr=open("stats.nath","r").readlines()
class Joueur:
    def __init__(self):
        self.nom=jjr[0]
        ara,nar=jjr[1].split("|"),[]
        for a in ara: nar.append(int(a))
        self.deck=nar
        self.argent=int(jjr[2])
        self.trophes=int(jjr[3])
        ara,nar=jjr[4].split("|"),[]
        for a in ara: nar.append(int(a))
        self.cartpos=nar
j=Joueur()


def save():
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
    txt=t1+t2+"\n"+t3+"\n"+t4+"\n"+t5+"\n"+"\n"
    ff.write(txt)
    ff.close()

def aff():
    fenetre.fill((50,20,100))
    bplay=pygame.Rect(0,0,0,0)
    bm1=fenetre.blit(pygame.transform.scale(pygame.image.load("images/m1.png"),[int(tex/4),75]),[tex/4*0,0])
    bm2=fenetre.blit(pygame.transform.scale(pygame.image.load("images/m2.png"),[int(tex/4),75]),[tex/4*1,0])
    bm3=fenetre.blit(pygame.transform.scale(pygame.image.load("images/m3.png"),[int(tex/4),75]),[tex/4*2,0])
    bm4=fenetre.blit(pygame.transform.scale(pygame.image.load("images/m4.png"),[int(tex/4),75]),[tex/4*3,0])
    fenetre.blit(font.render("vous avez "+str(j.argent)+" or",20,(150,145,15)),[50,tey-20])
    rcs=[]
    rcf=[]
    rcd=[]
    if smenu==2:
        #bplay=pygame.draw.rect(fenetre,(150,150,50),(tex/4,tey/1.8,tex/5,tey/5),0)
        #fenetre.blit(font.render("play",20,(50,50,150)),[tex/3,tey/1.6])
        bplay=fenetre.blit(pygame.transform.scale(pygame.image.load("images/bplay.png"),[int(200/1200*tex),int(150/1000*tey)]),[tex/2,tey/2,])
    elif smenu==1:
        xx,yy=50,350
        tx,ty=int(75/1200*tex),int(100/1000*tey)
        xxx=None
        for g in ctpp:
            if g == cselec:
                iii="images/fcs.png"
                xxx=xx
            elif g in j.deck: iii="images/fcd.png"
            elif j.cartpos[g]==0: iii="images/fcn.png"
            else: iii="images/fc.png"
            rcs.append( fenetre.blit(pygame.transform.scale(pygame.image.load(iii),[tx+30,ty+30]),[xx-15,yy-15]) )
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[g]),[tx,ty]),[xx,yy])
            xx+=tx+35
            if xx>tex-tx*1.2:
                xx=50
                yy+=ty+35
        if cselec!=None:
                g=cselec
                txi,tyi=400,400
                if xxx != None:
                    if xxx <= tex/2:  xi,yi=tex-txi,tey-tyi
                    else: xi,yi=0,tey-tyi
                pygame.draw.rect(fenetre,(200,200,200),(xi,yi,txi,tyi),0)
                fenetre.blit(font.render(str(cnom[g])                         ,20,(50,50,50))      ,[xi+5 ,yi])
                fenetre.blit(font.render("vie = "        +str(cvie[g])        ,20,(0,0,0))         ,[xi+5 ,yi+20])
                fenetre.blit(font.render("att = "        +str(catt[g])        ,20,(0,0,0))         ,[xi+5 ,yi+40])
                fenetre.blit(font.render("vitesse att = "+str(cvat[g])        ,20,(0,0,0))         ,[xi+5 ,yi+60])
                fenetre.blit(font.render("vitesse = "    +str(cvit[g])        ,20,(0,0,0))         ,[xi+150,yi+20])
                fenetre.blit(font.render("elixir = "     +str(celi[g])        ,20,(150,0,150))     ,[xi+150,yi+40])
                fenetre.blit(font.render("rareté = "     +str(rarete[crar[g]]),20,craret[crar[g]]) ,[xi+150,yi+60])
                txt=cdes[g]
                tl=30
                aa=int(len(txt)/tl)
                ttx=[]
                for w in range(aa):
                    if w+1==aa:
                        ttx.append( txt[int(w*tl):] )
                    else: ttx.append( txt[int(w*tl):int(w*tl+tl)] )
                for tt in ttx: fenetre.blit(font.render(str(tt),20,(50,50,50))      ,[xi+5 ,yi+80+(20*ttx.index(tt))])
        pygame.draw.rect(fenetre,(100,50,25),(0,(100/1000*tey),tex,200),0)
        pygame.draw.rect(fenetre,(150,150,5),(20,(120/1000*tey),tex-40,160),5)
        xx,yy,tx,ty=50,120,70,100
        for ca in j.deck:
            rcd.append( fenetre.blit(pygame.transform.scale(pygame.image.load("images/fc.png"),[tx+30,ty+30]),[xx-15,yy-15]) )
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[ca]),[tx,ty]),[xx,yy])
            xx+=tx+50
    elif smenu==4:
        xx,yy=50,100
        tx,ty=150,150
        for cf in cftpp:
            rcf.append( fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[cf]),[tx,ty]),[xx,yy]) )
            fenetre.blit(font.render(cfnom[cf],20,(250,250,250)),[xx,yy+ty+5])
            if j.argent >= cfarg[cf]: clf=(150,145,15)
            else: clf=(180,0,0)
            fenetre.blit(font.render(str(cfarg[cf])+" or",20,clf),[xx,yy+ty+25])
            xx+=tx+20
            if xx >= tex-tx+1:
                xx=50
                yy+=ty+50
    pygame.display.update()
    return bplay,bm1,bm2,bm3,bm4,rcs,rcf,rcd

def get_card(ic):
    ll=[]
    for tp in ctpp:
        if tp!=0 and tp!=1: ll.append(tp)
    crt=random.choice(ll)
    while crar[crt]!=ic: crt=random.choice(ll)
    return crt

def ac():
    while True:
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONUP: return True
            if event.type==QUIT: exit()

def coffre(c):
    crts=[]
    ore=random.randint(cfore[c][0],cfore[c][1])
    for ccc in cfcrt[c]:
        for x in range(ccc[1]): crts.append(get_card(ccc[0]))
    crts=list(set(crts))
    fenetre.fill((10,0,50))
    fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*tex),int(cftyy[c]/1000*tey)]),[tex/4,tey/4])
    pygame.display.update()
    for x in range(100):
            fenetre.fill((10,0,50))
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*tex),int(cftyy[c]/1000*tey)]),[tex/4,tey/4])
            pygame.draw.rect(fenetre,(100,100,0),(tex/3,tey/3,x*2,int(x*2.5)),5)
            fenetre.blit(pygame.transform.scale(font.render("or : "+str(ore),20,(150,150,20)),[x*2,int(x*2.5)]),[tex/3,tey/3])
            pygame.display.update()
            time.sleep(0.01)
    ac()
    time.sleep(0.5)
    for cc in crts:
        for x in range(100):
            fenetre.fill((10,0,50))
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*tex),int(cftyy[c]/1000*tey)]),[tex/4,tey/4])
            pygame.draw.rect(fenetre,craret[crar[cc]],(tex/3,tey/3,x*2,int(x*2.5)),5)
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[cc]),[x*2,int(x*2.5)]),[tex/3,tey/3])
            fenetre.blit(pygame.transform.scale(font.render(cnom[cc],20,(200,200,200)),[x*2,int(x*1.001)]),[tex/3,tey/3.5])
            pygame.display.update()
            time.sleep(0.01)
        ac()
        time.sleep(0.5)
    fenetre.fill((10,0,50))
    fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*tex),int(cftyy[c]/1000*tey)]),[tex/4,tey/4])
    xx,yy=50,50
    txx,tyy=120,170
    pygame.draw.rect(fenetre,(100,100,0),(xx,yy,txx,tyy),5)
    fenetre.blit(pygame.transform.scale(font.render("or : "+str(ore),20,(100,100,0)),[txx,tyy]),[xx,yy])
    xx+=txx+20
    pygame.display.update()
    for cc in crts:
        pygame.draw.rect(fenetre,craret[crar[cc]],(xx,yy,txx,tyy),5)
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[cc]),[txx,tyy]),[xx,yy])
        fenetre.blit(font.render(cnom[cc],20,(200,200,200)),[xx,yy+tyy])
        xx+=txx+20
        if xx >= tex-txx-20:
            xx=50
            yy+=tyy+20
        pygame.display.update()
    j.argent+=ore
    for c in crts: j.cartpos[c]=1
    time.sleep(0.5)
    ac()
    time.sleep(0.5)
    
##################################################

fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("ROYAL")
fenetre.blit(pygame.transform.scale(pygame.image.load("images/fmenu.png"),[tex,tey]),[0,0])
pygame.display.update()
time.sleep(1)
dc=time.time()
tdc=0.5

encour=True
while encour:
    bplay,bm1,bm2,bm3,bm4,rcs,rcf,rcd=aff()
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
                    if time.time()-dc < tdc:
                        if len(j.deck) < 8 and j.cartpos[rcs.index(c)]==1 and ctpp[rcs.index(c)]!=0 and ctpp[rcs.index(c)]!=1:
                            j.deck.append(rcs.index(c))
                            j.deck=list(set(j.deck))
                    dc=time.time()
            for c in rcd:
                if rpos.colliderect(c):
                    if time.time()-dc < tdc:
                        if rcd.index(c)<=len(j.deck): del(j.deck[rcd.index(c)])
                    dc=time.time()
            for c in rcf:
                if rpos.colliderect(c):
                    if j.argent >= cfarg[rcf.index(c)]:
                        coffre(rcf.index(c))
                        j.argent-=cfarg[rcf.index(c)]
            save()
    








