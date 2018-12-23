#coding:utf-8

def test():
    rv = (3,1)
    import sys,os
    cv = sys.version_info
    if cv < rv:
         print("vous utilisez une version de python trop ancienne, veuillez installer python"+str(rv[0])+"."+str(rv[1]))
         exit()
    try: import subprocess
    except:
        print("La librairie subprocess va etre installée sur votre ordinateur...")
        os.system("pip install subprocess")
        os.system("pip3 install subprocess")
        print("La librairie subprocess devrait etre installée sur votre ordinateur.")
    try: import pygame
    except:
        print("La librairie pygame va etre installée sur votre ordinateur...")
        os.system("pip install pygame")
        os.system("pip3 install pygame")
        print("La librairie pygame devrait etre installée sur votre ordinateur.")
    try: import requests
    except:
        print("La librairie requests va etre installée sur votre ordinateur...")
        os.system("pip install requests")
        print("La librairie requests devrait etre installée sur votre ordinateur.")

test()

import pygame,time,os,random
from pygame.locals import *
from cartes import *
import subprocess

pygame.init()
tex,tey=1000,750
smenu=2
scrtm=0
cselec=None

####text de version#####

version=float(open("version","r").read())
try:
    url="https://raw.githubusercontent.com/nath54/royal/master/version"
    import requests
    req = requests.get(url)
    txxt=""
    for chunk in req.iter_content(1000):
        txxt+=str(chunk)
    #print(txxt)
    dv=float(txxt[2:-3])
    ff=open("dernier_version","w")
    ff.write(str(dv))
    ff.close()
except:
    if not "dernier_version" in os.listdir():
        dv=0.0
    else:
        dv=float(open("dernier_version","r").read())
#print(dv)

##############

font=pygame.font.SysFont("Serif",20)

rarete=["commun","rare","epique","legendaire","divin"]
craret=[(0,0,140),(150,105,25),(150,0,150),(20,150,20),(250,250,0)]

if not "stats.nath" in os.listdir("./"):
    txt=""
    import textbox
    tc=""
    for x in ctpp:
        if x==0 or x==1: tc+="0"
        else: tc+="2"
        tc+="|"
    tc=tc[:-1]
    print(tc)
    txt+=textbox.main()+"##2000#0#"+tc+"#0"
    f=open("stats.nath","w")
    f.write(txt)
    f.close()





class Joueur:
    def __init__(self):
        self.nom="None"
        self.deck=[]
        self.argent=0
        self.trophes=0
        self.cartpos=[]
        self.arene=1
        for ar in atpp:
            if self.trophes >= atro[ar]: self.arene=ar
def load(j):
    jjr=open("stats.nath","r").read().split("#")
    j.nom=jjr[0]
    ara,nar=jjr[1].split("|"),[]
    if len(ara) > 1:
       for a in ara: nar.append(int(a))
    j.deck=nar
    j.argent=int(jjr[2])
    j.trophes=int(jjr[3])
    ara,nar=jjr[4].split("|"),[]
    for a in ara: nar.append(int(a))
    j.cartpos=nar
    j.arene=1
    for ar in atpp:
        if j.trophes >= atro[ar]: j.arene=ar
    return j
    
j=Joueur()
j=load(j)

def save():
    ff=open("stats.nath","w")
    t1=str(j.nom)
    t2=""
    for jj in j.deck:
        t2+=str(jj)+"|"
    t2=t2[:-1]
    t3=str(j.argent)
    t4=str(j.trophes)
    t6=str(j.arene)
    t5=""
    for jj in j.cartpos:
        t5+=str(jj)+"|"
    t5=t5[:-1]
    txt=t1+"#"+t2+"#"+t3+"#"+t4+"#"+t5+"#"+t6+"#"
    ff.write(txt)
    ff.close()

def aff():
    fenetre.fill((50,20,100))
    bplay=pygame.Rect(0,0,0,0)
    bale=pygame.Rect(0,0,0,0)
    bf1=pygame.Rect(0,0,0,0)
    bf2=pygame.Rect(0,0,0,0)
    if smenu!=1:  imgm1="images/m1.png"
    else       :  imgm1="images/m1sel.png"
    if smenu!=2:  imgm2="images/m2.png"
    else       :  imgm2="images/m2sel.png"
    if smenu!=3:  imgm3="images/m4.png"
    else       :  imgm3="images/m4sel.png"
    bm1=fenetre.blit(pygame.transform.scale(pygame.image.load(imgm1),[int(tex/3),int(75/1000*tey)]),[tex/3*0,0])
    bm2=fenetre.blit(pygame.transform.scale(pygame.image.load(imgm2),[int(tex/3),int(75/1000*tey)]),[tex/3*1,0])
    bm3=fenetre.blit(pygame.transform.scale(pygame.image.load(imgm3),[int(tex/3),int(75/1000*tey)]),[tex/3*2,0])
    fenetre.blit(font.render(j.nom+" : "+str(j.argent)+" or  ,  "+str(j.trophes)+" trophés  ,  arene : "+str(j.arene),20,(150,145,15)),[50/1200*tex,85/1000*tey])
    if version < dv: cl=(150,0,0)
    else: cl=(0,150,0)
    fenetre.blit(font.render("votre version : "+str(version)+" , derniere version : "+str(dv),20,cl),[int(tex-500/1200*tex),int(85/1000*tey)])
    rcs=[]
    rcf=[]
    rcd=[]
    if smenu==2:
        bplay=fenetre.blit(pygame.transform.scale(pygame.image.load("images/bplay.png"),[int(200/1200*tex),int(150/1000*tey)]),[tex/2,tey/2,])
        xxx,yyy=50,200
        txx,tyy=300,400
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[j.arene])+"_3.png"),[txx,tyy]),[xxx,yyy])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[j.arene])+"_1.png"),[txx-10,int(tyy/2-10)]),[xxx+5,yyy+5])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[j.arene])+"_1.png"),[txx-10,int(tyy/2-10)]),[xxx+5,yyy+tyy/2+5])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[j.arene])+"_2.png"),[int(70/1200*txx),int(100/1000*tyy)]),[xxx+30,yyy+tyy/2-20])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[j.arene])+"_2.png"),[int(70/1200*txx),int(100/1000*tyy)]),[xxx+txx-60,yyy+tyy/2-20])
        fenetre.blit(font.render(anom[j.arene],20,(150,150,150)),[xxx,yyy+tyy+50])
        if j.arene>=len(atpp)-1:
            fenetre.blit(font.render("Vous etes à l'arène maximale",20,(215,210,230)),[50/1200*tex,800/1000*tey])
        else:
            ars=atpp[j.arene+1]
            fenetre.blit(font.render("Arène suivante : "+str(atro[ars])+" , "+str(atro[ars]-j.trophes)+" trophés restants",20,(215,210,230)),[50/1200*tex,800/1000*tey])
    elif smenu==1:
        if scrtm+44 > len(ctpp): ac=len(ctpp)
        else:
            ac=scrtm+44
            bf2=fenetre.blit(pygame.transform.scale(pygame.image.load("images/flch.png"),[int(20/1200*tex),int(100/1000*tey)]),[tex-1-int(20/1200*tex),tey/2])
        if scrtm>0: bf1=fenetre.blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load("images/flch.png"),[int(20/1200*tex),int(100/1000*tey)]),1,0),[1,tey/2])
        lscrt=range(scrtm,ac)
        for cc in j.deck:
            if j.cartpos[cc]==0: del(j.deck[j.deck.index(cc)])
        xx,yy=50,350
        tx,ty=int(60/1200*tex),int(85/1000*tey)
        xxx=None
        for g in lscrt:
            if g == cselec:
                iii="images/fcs.png"
                xxx=xx
            elif g in j.deck: iii="images/fcd.png"
            elif j.cartpos[g]==0: iii="images/fcn.png"
            else: iii="images/fc.png"
            nbc=str(j.cartpos[g])
            clr=craret[crar[g]]
            rcs.append( fenetre.blit(pygame.transform.scale(pygame.image.load(iii),[tx+30,ty+30]),[xx-15,yy-15]) )
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[g]),[tx,ty]),[xx,yy])
            pygame.draw.rect(fenetre,clr,(xx-12,yy-12,20+len(nbc)*3,20),0)
            fenetre.blit(font.render(nbc,20,(250-clr[0],250-clr[1],250-clr[2])),[xx-8,yy-12])
            xx+=tx+35
            if xx>tex-tx*1.2:
                xx=50
                yy+=ty+35
        if cselec!=None:
                g=cselec+scrtm
                txi,tyi=400,400
                xi,yi=tex-txi,tey-tyi
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
                ttx=" "
                w=0
                yty=yi+80
                for t in txt:
                    if w>=tl and t==" ":
                        w=0
                        fenetre.blit(font.render(str(ttx),20,(50,50,50)),[xi+5,yty])
                        yty+=20
                        ttx=""
                    ttx+=t
                    w+=1
                fenetre.blit(font.render(str(ttx),20,(50,50,50)),[xi+5,yty])
        pygame.draw.rect(fenetre,(100,50,25),(0,(130/1000*tey),tex,200),0)
        pygame.draw.rect(fenetre,(150,150,5),(20,(150/1000*tey),tex-40,160),5)
        xx,yy,tx,ty=50,120,int(60/1200*tex),int(85/1000*tey)
        for ca in j.deck:
            rcd.append( fenetre.blit(pygame.transform.scale(pygame.image.load("images/fc.png"),[tx+30,ty+30]),[xx-15,yy]) )
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[ca]),[tx,ty]),[xx,yy+15])
            xx+=tx+50
        if len(j.deck)==8: cl=(0,200,0)
        else: cl=(200,0,0)
        fenetre.blit(pygame.font.SysFont("Sans",40).render(str(len(j.deck))+"/ 8",20,cl),[tex-150,150])
        bale=pygame.Rect(int(tex-90/1200*tex),int(150/1000*tey),int(65/1200*tex),int(45/1000*tey))
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/bale.png"),[int(65/1200*tex),int(45/1000*tey)]),[int(tex-90/1200*tex),int(150/1000*tey)])
    elif smenu==3:
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
    return bplay,bm1,bm2,bm3,rcs,rcf,rcd,bale,bf1,bf2

def get_card(rar,aren):
    ll=[]
    for tp in ctpp:
        if tp!=0 and tp!=1: ll.append(tp)
    crt=random.choice(ll)
    while crar[crt]!=rar or care[crt]>aren:
        crt=random.choice(ll)
    return crt

def ac():
    while True:
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONUP: return True
            if event.type==QUIT: exit()

def coffre(c,aren):
    crts=[]
    nbcr=[]
    ore=random.randint(cfore[c][0],cfore[c][1])
    if c==0:
        cfcrt=[ [5,0],
                [4,1] ]
    elif c==1:
        cfcrt=[ [6,0],
                [5,1],
                [3,2] ]
    elif c==2:
        cfcrt=[ [9,0],
                [7,1],
                [6,2],
                [2,3] ]
    elif c==3:
        cfcrt=[ [9,0],
                [5,1],
                [3,2],
                [2,3],
                [1,4] ]
    elif c==4:
        cfcrt=[ [6,2],
                [10,3],
                [3,4] ]
    elif c==5:
        cfcrt=[ [6,2],
                [5,3],
                [10,4] ]
    for ccc in cfcrt:
        #print(ccc)
        for x in range(ccc[0]): 
            crt=get_card(ccc[1],aren)
            #if crar[crt]!=ccc[1]: print("mauvais")
            crts.append(crt)
    crts=list(set(crts))
    r0=[1,10]
    r1=[1,8]
    r2=[1,6]
    r3=[1,3]
    r4=[1,2]
    if c==4 or c==5:
        r3=[1,30]
        #print("c>=4")
    if c==5:
        r4=[1,30]
    for cc in crts:
        if crar[cc]==0: nbcr.append(random.randint(r0[0],r0[1]))
        elif crar[cc]==1: nbcr.append(random.randint(r1[0],r1[1]))
        elif crar[cc]==2: nbcr.append(random.randint(r2[0],r2[1]))
        elif crar[cc]==3: nbcr.append(random.randint(r3[0],r3[1]))
        elif crar[cc]==4: nbcr.append(random.randint(r4[0],r4[1]))
        else: nbcr.append(1)
    fenetre.fill((10,0,50))
    fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*tex),int(cftyy[c]/1000*tey)]),[tex/4,tey/4])
    pygame.display.update()
    njk=0
    for x in range(100):
            fenetre.fill((10,0,50))
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*tex),int(cftyy[c]/1000*tey)]),[tex/4,tey/4])
            pygame.draw.rect(fenetre,(100,100,0),(tex/3,tey/3,x*2,int(x*2.5)),5)
            fenetre.blit(pygame.transform.scale(font.render("or : "+str(ore),20,(150,150,20)),[x*2,int(x*2.5)]),[tex/3,tey/3])
            pygame.display.update()
            time.sleep(0.01)
            for event in pygame.event.get():
                if event.type==MOUSEBUTTONUP: njk=1
            if njk==1:
                break
    if njk!=1:
        ac()
        time.sleep(0.5)
    for cc in crts:
        njk=0
        for x in range(100):
            fenetre.fill((10,0,50))
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*tex),int(cftyy[c]/1000*tey)]),[tex/4,tey/4])
            pygame.draw.rect(fenetre,craret[crar[cc]],(tex/3,tey/3,x*2,int(x*2.5)),5)
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[cc]),[x*2,int(x*2.5)]),[tex/3,tey/3])
            fenetre.blit(pygame.transform.scale(font.render(cnom[cc]+"  ("+str(nbcr[crts.index(cc)])+")",20,(200,200,200)),[x*2,int(x*1.001)]),[tex/3,tey/3.5])
            pygame.display.update()
            time.sleep(0.01)
            for event in pygame.event.get():
                if event.type==MOUSEBUTTONUP:
                    njk=1
            if njk==1:
                break
        if njk!=1:
            ac()
            time.sleep(0.5)
    time.sleep(0.6)
    fenetre.fill((10,0,50))
    fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*tex),int(cftyy[c]/1000*tey)]),[tex/4,tey/4])
    xx,yy=int(50/1200*tex),int(50/1000*tey)
    txx,tyy=int(120/1200*tex),int(170/1000*tey)
    pygame.draw.rect(fenetre,(100,100,0),(xx,yy,txx,tyy),5)
    fenetre.blit(pygame.transform.scale(font.render("or : "+str(ore),20,(100,100,0)),[txx,tyy]),[xx,yy])
    xx+=txx+20
    pygame.display.update()
    for cc in crts:
        pygame.draw.rect(fenetre,craret[crar[cc]],(xx,yy,txx,tyy),5)
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[cc]),[txx,tyy]),[xx,yy])
        fenetre.blit(pygame.transform.scale( font.render(cnom[cc]+" ("+str(nbcr[crts.index(cc)])+")",20,(200,200,200)) ,[txx,25] ),[xx,yy+tyy])
        xx+=txx+20
        if xx >= tex-txx-20:
            xx=50
            yy+=tyy+40
        pygame.display.update()
    j.argent+=ore
    for ccc in crts:
        j.cartpos[ccc]+=nbcr[crts.index(ccc)]
    time.sleep(0.5)
    ac()
    time.sleep(0.5)

def deckale(j):
    deck=[]
    while len(deck)<8:
        a=random.choice(ctpp)
        if a!=0 and a!=1 and j.cartpos[a]>0:
            deck.append(a)
            deck=list(set(deck))
    return deck

def alertbox(txt):
    bx,by,btx,bty=int(tex/3),int(tey/3),int(500/1200*tex),int(350/1000*tey)
    pygame.draw.rect(fenetre,(50,10,100),(bx,by,btx,bty),0)
    pygame.draw.rect(fenetre,(10,10,10),(bx,by,btx,bty),5)
    fenetre.blit(font.render(txt,20,(200,200,200)),[bx+15,by+15])
    bb=pygame.draw.rect(fenetre,(125,125,10),(int(bx+btx/4*2),int(by+bty/5*3),int(btx/4),int(bty/5)),0)
    pygame.draw.rect(fenetre,(125,125,120),(int(bx+btx/4*2),int(by+bty/5*3),int(btx/4),int(bty/5)),5)
    fenetre.blit(font.render("ok",20,(200,200,200)),[int(5+bx+btx/4*2),int(5+by+bty/5*3)])
    pygame.display.update()
    boucle=True
    while boucle:
        for event in pygame.event.get():
            if event.type==QUIT:
                encour=False
                boucle=False
                break
            elif event.type==KEYDOWN:
                if event.key==K_q:
                    encour=False
                    boucle=False
                    break
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                rpos=pygame.Rect(pos[0],pos[1],0,0)
                if rpos.colliderect(bb):
                    boucle=False
                    break
            
def maj():
    #TODO
    pass

def vdate():
    date=time.localtime()
    if date.tm_mon==12 and date.tm_mday==25:
        cond=True
        nvf=False
        if not "recompget.nath" in os.listdir():
            cond=True
            nvf=True
        else:
            ff=open("recompget.nath","r").read()
            df=ff.split("#")
            for dd in df:
              if len(dd)>4:
                d=dd.split("|") #0=jour,1=mois,2=année
                if d[0]==str(date.tm_mday) and d[1]==str(date.tm_mon) and d[2]==str(date.tm_year):
                    cond=False
        if cond:
            alertbox("Joyeux Noël !")
            alertbox("Voici un petit cadeau : 10.000 or !")
            j.argent+=10000
            if nvf: txt=""
            else: txt="#"
            txt+=str(date.tm_mday)+"|"+str(date.tm_mon)+"|"+str(date.tm_year)
            ff=open("recompget.nath","a")
            ff.write(txt)
            ff.close()
            
            

##################################################

fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("THE CLASH OF FIGHTERS")
fenetre.blit(pygame.transform.scale(pygame.image.load("images/fmenu.png"),[tex,tey]),[0,0])
pygame.display.update()
time.sleep(1)
dc=time.time()
tdc=0.5

if version < dv and dv != 0.0:
    alertbox("Une mise à jour est disponible")
    
vdate()

encour=True
while encour:
    bplay,bm1,bm2,bm3,rcs,rcf,rcd,bale,bf1,bf2=aff()
    for cc in j.deck:
        if j.cartpos[cc]==0: del(j.deck[j.deck.index(cc)])
    for event in pygame.event.get():
        if event.type==QUIT: encour=False
        elif event.type==KEYDOWN:
            if event.key==K_q: encour=False
        elif event.type==MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            rpos=pygame.Rect(pos[0],pos[1],1,1)
            if rpos.colliderect(bplay):
                if len(j.deck)==8:
                    for cc in j.deck:
                        if j.cartpos[cc] >= 1: j.cartpos[cc]-=1
                    save() 
                    try: os.system("python3 a.py")
                    except: os.system("python a.py")
                    fenetre.blit(pygame.font.SysFont("Serif",50).render("si votre partie est finie, cliquez",0,(0,200,150)),[20,tey/2])
                    pygame.display.update()
                    ac()
                    j=load(j)
                else:
                    alertbox("votre deck n'est pas composé de 8 cartes !")
            elif rpos.colliderect(bm1): smenu=1
            elif rpos.colliderect(bm2): smenu=2
            elif rpos.colliderect(bm3): smenu=3
            elif rpos.colliderect(bf1): scrtm-=44
            elif rpos.colliderect(bf2): scrtm+=44
            elif rpos.colliderect(bale): j.deck=deckale(j)
            for c in rcs:
                if rpos.colliderect(c):
                    if cselec!=rcs.index(c): cselec=rcs.index(c)
                    else: cselec=None
                    if time.time()-dc < tdc:
                        crtg=rcs.index(c)+scrtm
                        if len(j.deck) < 8 and j.cartpos[crtg]>=1 and ctpp[crtg]!=0 and ctpp[crtg]!=1:
                            j.deck.append(crtg)
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
                        coffre(rcf.index(c),j.arene)
                        j.argent-=cfarg[rcf.index(c)]
            save()
    








