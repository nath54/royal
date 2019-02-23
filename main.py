#coding:utf-8
from lib3 import *

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

amaj=False

pygame.init()

t1t=time.time()

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
    if version < dv: amaj=True
except:
    if not "dernier_version" in os.listdir():
        dv=0.0
    else:
        dv=float(open("dernier_version","r").read())
#print(dv)

##############

font=pygame.font.SysFont("Serif",20)

dpseudo=False
if "maj.py" in os.listdir("../"): os.remove("../maj.py")
if "maj.py~" in os.listdir("../"): os.remove("../maj.py~")
if not fichs in os.listdir():
    txt=""
    import textbox
    tc=""
    ct=""
    for x in ctpp+[0,0,0]:
        if care[x] == 0 and ctpp[x] != 0 and ctpp[x] != 1:
            tc+="10"
            ct+="1"
        else :
            tc+="0"
            ct+="0"
        tc+="|"
        ct+="|"
    tc=tc[:-1]
    ct=ct[:-1]
    txt+="pseudo"+cac+cac+"2000"+cac+"0"+cac+tc+cac+"0"+cac+ct+cac+"0"+cac+"0"+cac+"0"
    f=open(fichs,"w")
    f.write(txt)
    f.close()
    smenu=8
    dpseudo=True
if not fichp in os.listdir():
    txt="1000"+cac+"750"+cac+"1"+cac+"1"+cac+"1"+cac+"60"
    g=open(fichp,"w")
    g.write(txt)
    g.close()
if not fichh in os.listdir():
    h=open(fichh,"w")
    h.close()

from lib import *
from lib2 import *
from pygame.locals import *
from cartes import *
import subprocess

j=Joueure()
j=load(j)


def temps():
    if fichtps in os.listdir():
        tps=open(fichtps,"r").read()
        if len(tps)>0:
            if tps[-1]=="\n": tps=tps[:-1]
            tps=int(float(tps))
        else: tps=0
    else: tps=0
    tps+=int(time.time()-t1t)
    return tps

def savetps():
    t2t=time.time()
    if not fichtps in os.listdir():
        txt=str(int(t2t-t1t))
    else:
        fa=open(fichtps,"r").read()
        if len(fa)>0:
            if fa[-1]=="\n": fb=fa[:-1]
            else: fb=fa
            fc=int(fb)
        txt=str(fc+int(t2t-t1t))
    ff=open(fichtps,"w")
    ff.write(txt)
    ff.close()
    
def rx(x): return int(x/1200*j.tex)
def ry(y): return int(y/1000*j.tey)

def texte(xx,yy,txt,cl,tt):
    return fenetre.blit(pygame.font.SysFont("Serif",tt).render(txt,20,cl),[xx,yy])

def button(text,x,y,tx,ty,cl1,cl2):
    tb=2
    bb=pygame.draw.rect(fenetre,cl1,(x,y,tx,ty),0)
    pygame.draw.rect(fenetre,cl2,(x,y,tx,ty),tb)
    fenetre.blit(pygame.transform.scale(font.render(text,20,cl2),[int(tx/1.5),int(ty/1.5)]),[int(x+tx/5),int(y+ty/5)])
    return bb

def deblocrt(crt):
    clt=(250,250,250)
    pygame.draw.rect(fenetre,(25,10,100),(int(100/1200*j.tex),int(100/1000*j.tex),j.tex-int(200/1200*j.tex),j.tey-int(200/1000*j.tey)),0)
    pygame.draw.rect(fenetre,(0,0,0),(int(100/1200*j.tex),int(100/1000*j.tex),j.tex-int(200/1200*j.tex),j.tey-int(200/1000*j.tey)),5)
    fenetre.blit( font.render("Vous avez débloqué une nouvelle carte : "+cnom[crt]+" !!!",20,(200,250,250)) , [int(300/1200*j.tex),int(150/1000*j.tey)] )
    fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[crt]),[int(200/1200*j.tex),int(300/1000*j.tey)]),[int(200/1200*j.tex),int(300/1000*j.tey)])
    pygame.draw.rect(fenetre,craret[crar[crt]],(int(200/1200*j.tex),int(300/1000*j.tey),int(200/1200*j.tex),int(300/1000*j.tey)),5)
    fenetre.blit( font.render("Statistiques de la carte : ",20,clt) , [int(600/1200*j.tex),int(300/1000*j.tey)] )
    fenetre.blit( font.render("vie : "+str(cvie[crt]),20,clt) , [int(500/1200*j.tex),int(350/1000*j.tey)] )
    fenetre.blit( font.render("dégats attaque : "+str(catt[crt]),20,clt) , [int(500/1200*j.tex),int(400/1000*j.tey)] )
    fenetre.blit( font.render("vitesse attaque : "+str(cvat[crt]),20,clt) , [int(500/1200*j.tex),int(450/1000*j.tey)] )
    fenetre.blit( font.render("portee : "+str(cpor[crt]),20,clt) , [int(500/1200*j.tex),int(500/1000*j.tey)] )
    fenetre.blit( font.render("vitesse : "+str(cvit[crt]),20,clt) , [int(500/1200*j.tex),int(550/1000*j.tey)] )
    fenetre.blit( font.render("rareté : "+str(rarete[crar[crt]]),20,clt) , [int(500/1200*j.tex),int(600/1000*j.tey)] )
    fenetre.blit( font.render("description : ",20,clt) , [int(110/1200*j.tex),int(700/1000*j.tey)] )
    xi,yi=int(250/1200*j.tex),int(700/1000*j.tey)
    txt=cdes[crt]
    tl=70
    aa=int(len(txt)/tl)
    ttx=" "
    w=0
    yty=yi
    for t in txt:
        if w>=tl and t==" ":
            w=0
            fenetre.blit(font.render(str(ttx),20,clt),[xi+5,yty])
            yty+=20
            ttx=""
        ttx+=t
        w+=1
    fenetre.blit(font.render(str(ttx),20,clt),[xi+5,yty])
    bexit=pygame.draw.rect(fenetre,(150,0,0),(int(900/1200*j.tex),j.tey-int(150/1000*j.tey),int(80/1200*j.tex),int(50/1000*j.tey)),0)
    pygame.draw.rect(fenetre,(0,0,0),(int(900/1200*j.tex),j.tey-int(150/1000*j.tey),int(80/1200*j.tex),int(50/1000*j.tey)),5)
    fenetre.blit(font.render("fermer",20,(0,0,0)),[int(906/1200*j.tex),j.tey-int(140/1000*j.tey)])
    pygame.display.update()
    ouv=True
    while ouv:
        for event in pygame.event.get():
            if event.type==QUIT: ouv,encour=False,False
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                rpos=pygame.Rect(pos[0],pos[1],1,1)
                if rpos.colliderect(bexit):
                    ouv=False
nbcm=36

def aff():
    global arsel
    fenetre.fill((50,20,100))
    bchlp=pygame.Rect(0,0,0,0)
    bren=pygame.Rect(0,0,0,0)
    bts=[]
    for x in range(25): bts.append( None )
    barensl=[]
    for x in range(len(atpp)): barensl.append(None)
    #0=bouton play
    #1=bouton deck aléatoire
    #2=bouton flèche cartes gauche
    #3=bouton flèche cartes droite
    #4=bouton parametres
    #5=bouton pagecrédits
    #6=bouton menu 1
    #7=bouton menu 2
    #8=bouton menu 3
    #9=bouton menu arene
    #10=bouton parametre reglage musique
    #11=bouton fleche gauche menu arene
    #12=bouton fleche droite menu arene
    #13=bouton fleche gauche menu aide
    #14=bouton fleche droite menu aide
    #15=bouton creer racourcis
    #16=bouton parametre changer os
    #17=bouton tutoriel
    #18=bouton menu profil
    #19=bouton menu historique
    #20=bouton augmenter fpsmax
    #21=bouton diminuer fpsmax
    #22=bouton mettre à jour
    if smenu!=1:  imgm1="images/m1.png"
    else       :  imgm1="images/m1sel.png"
    if smenu!=2:  imgm2="images/m2.png"
    else       :  imgm2="images/m2sel.png"
    if smenu!=3:  imgm3="images/m4.png"
    else       :  imgm3="images/m4sel.png"
    bts[6]=fenetre.blit(pygame.transform.scale(pygame.image.load(imgm1),[int(j.tex/4),int(75/1000*j.tey)]),[j.tex/4*1,0])
    bts[7]=fenetre.blit(pygame.transform.scale(pygame.image.load(imgm2),[int(j.tex/4),int(75/1000*j.tey)]),[j.tex/4*2,0])
    bts[8]=fenetre.blit(pygame.transform.scale(pygame.image.load(imgm3),[int(j.tex/4),int(75/1000*j.tey)]),[j.tex/4*3,0])
    bts[18]=pygame.draw.rect(fenetre,(50,50,170),(rx(0),ry(0),int(j.tex/4),ry(75)),0)
    clbm=(0,0,100)
    if smenu==9: clbm=(0,250,250)
    pygame.draw.rect(fenetre,clbm,(rx(0),ry(0),int(j.tex/4),ry(75)),5)
    pygame.draw.rect(fenetre,(200,200,250),(rx(10),ry(10),int(j.exp/j.xpmax*j.tex/6.0),ry(50)),0)
    pygame.draw.rect(fenetre,(250,250,250),(rx(10),ry(10),j.tex/6,ry(50)),2)
    texte(rx(20)+j.tex/6,ry(15),str(j.niveau),(0,75,75),40)
    fenetre.blit(font.render(j.nom+" : "+str(j.argent)+" or  ,  "+str(j.trophes)+" trophés  ,  arene : "+str(j.arene),20,(150,145,15)),[50/1200*j.tex,85/1000*j.tey])
    if version < dv: cl=(150,0,0)
    else: cl=(0,150,0)
    fenetre.blit(font.render("votre version : "+str(version)+" , derniere version : "+str(dv),20,cl),[int(j.tex-500/1200*j.tex),int(85/1000*j.tey)])
    rcs=[]
    rcf=[]
    rcd=[]
    lbpr=[]
    if smenu==2: #menu principal
        bts[0]=fenetre.blit(pygame.transform.scale(pygame.image.load("images/bplay.png"),[int(200/1200*j.tex),int(150/1000*j.tey)]),[j.tex/2,j.tey/2,])
        xxx,yyy=int(50/1200*j.tex),int(200/1000*j.tey)
        txx,tyy=int(300/1200*j.tex),int(400/1000*j.tey)
        bts[9]=fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[j.arene])+"_3.png"),[txx,tyy]),[xxx,yyy])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[j.arene])+"_1.png"),[txx-10,int(tyy/2-10)]),[xxx+5,yyy+5])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[j.arene])+"_1.png"),[txx-10,int(tyy/2-10)]),[xxx+5,yyy+tyy/2+5])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[j.arene])+"_2.png"),[int(70/1200*txx),int(100/1000*tyy)]),[xxx+30,yyy+tyy/2-20])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[j.arene])+"_2.png"),[int(70/1200*txx),int(100/1000*tyy)]),[xxx+txx-60,yyy+tyy/2-20])
        fenetre.blit(font.render(anom[j.arene],20,(150,150,150)),[xxx,yyy+tyy+50])
        if j.arene>=len(atpp)-1:
            fenetre.blit(font.render("Vous etes à l'arène maximale",20,(215,210,230)),[50/1200*j.tex,750/1000*j.tey])
        else:
            ars=atpp[j.arene+1]
            fenetre.blit(font.render("Arène suivante : "+str(atro[ars])+" , "+str(atro[ars]-j.trophes)+" trophés restants",20,(215,210,230)),[50/1200*j.tex,750/1000*j.tey])
        bts[4]=fenetre.blit(pygame.transform.scale(pygame.image.load("images/para.png"),[int(100/1200*j.tex),int(100/1000*j.tey)]),[j.tex-int(150/1200*j.tex),int(150/1000*j.tey)])
        bts[5]=fenetre.blit(pygame.transform.scale(pygame.image.load("images/cred.png"),[int(150/1200*j.tex),int(100/1000*j.tey)]),[j.tex-int(150/1200*j.tex),j.tey-int(150/1000*j.tey)])
        bts[17]=pygame.draw.rect(fenetre,(200,25,70),(j.tex-int(200/1200*j.tex),int(500/1000*j.tey),int(150/1200*j.tex),int(100/1000*j.tey)),0)
        pygame.draw.rect(fenetre,(0,0,0),(j.tex-int(200/1200*j.tex),int(500/1000*j.tey),int(150/1200*j.tex),int(100/1000*j.tey)),5)
        fenetre.blit(font.render("aide",30,(0,0,0)),[j.tex-int(190/1200*j.tex),int(510/1000*j.tey)])
    elif smenu==1: #menu cartes
        if scrtm+nbcm > len(ctpp): ac=len(ctpp)
        else:
            ac=scrtm+nbcm
            bts[3]=fenetre.blit(pygame.transform.scale(pygame.image.load("images/flch.png"),[rx(20),ry(100)]),[j.tex-1-rx(20),j.tey/2])
        if scrtm>0: bts[2]=fenetre.blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load("images/flch.png"),[rx(20),ry(100)]),1,0),[1,j.tey/2])
        lscrt=range(scrtm,ac)
        for cc in j.deck:
            if j.cartpos[cc]==0: del(j.deck[j.deck.index(cc)])
        xx,yy=rx(80),ry(370)
        tx,ty=rx(80),ry(100)
        xxx=None
        for g in lscrt:
            if g == cselec and j.cartpos[g]>0:
                iii="images/fcs.png"
                xxx=xx
            elif g == cselec and j.cartpos[g]==0:
                iii="images/fcns.png"
                xxx=xx
            elif g in j.deck: iii="images/fcd.png"
            elif j.cartpos[g]==0: iii="images/fcn.png"
            else: iii="images/fc.png"
            nbc=str(j.cartpos[g])
            clr=craret[crar[g]]
            rcs.append( fenetre.blit(pygame.transform.scale(pygame.image.load(iii),[tx+rx(30),ty+ry(30)]),[xx-rx(15),yy-ry(15)]) )
            if j.cartdeb[g]==1 or j.cartpos[g] > 0:
                fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[g]),[tx,ty]),[xx,yy])
            else:
                fenetre.blit(pygame.transform.scale(pygame.image.load("images/inc.png"),[tx,ty]),[xx,yy])
            pygame.draw.rect(fenetre,clr,(xx-rx(12),yy-ry(12),rx(20+len(nbc)*3),ry(20)),0)
            fenetre.blit(font.render(nbc,20,(250-clr[0],250-clr[1],250-clr[2])),[xx-rx(8),yy-ry(12)])
            xx+=tx+rx(40)
            if xx>j.tex-tx*1.2:
                xx=rx(80)
                yy+=ty+ry(40)
        if cselec!=None:
                g=cselec+scrtm
                txi,tyi=rx(400),ry(400)
                xi,yi=j.tex-txi,j.tey-tyi
                if xxx != None:
                    if xxx <= j.tex/2:  xi,yi=j.tex-txi,j.tey-tyi
                    else: xi,yi=0,j.tey-tyi
                pygame.draw.rect(fenetre,(200,200,200),(xi,yi,txi,tyi),0)
                if j.cartdeb[g]==1:
                    fenetre.blit(font.render(str(cnom[g])                         ,20,(50,50,50))      ,[xi+rx(5 ),yi])
                    fenetre.blit(font.render("vie = "        +str(cvie[g])        ,20,(0,0,0))         ,[xi+rx(5 ),yi+ry(20)])
                    fenetre.blit(font.render("att = "        +str(catt[g])        ,20,(0,0,0))         ,[xi+rx(5 ),yi+ry(40)])
                    fenetre.blit(font.render("vitesse att = "+str(cvat[g])        ,20,(0,0,0))         ,[xi+rx(5 ),yi+ry(60)])
                    fenetre.blit(font.render("vitesse = "    +str(cvit[g])        ,20,(0,0,0))         ,[xi+rx(150),yi+ry(20)])
                    fenetre.blit(font.render("elixir = "     +str(celi[g])        ,20,(150,0,150))     ,[xi+rx(150),yi+ry(40)])
                    fenetre.blit(font.render("rareté = "     +str(rarete[crar[g]]),20,craret[crar[g]]) ,[xi+rx(150),yi+ry(60)])
                    txt=cdes[g]
                    tl=30
                    aa=int(len(txt)/tl)
                    ttx=" "
                    w=0
                    yty=yi+ry(80)
                    for t in txt:
                        if w>=tl and t==" ":
                            w=0
                            fenetre.blit(font.render(str(ttx),20,(50,50,50)),[xi+rx(5),yty])
                            yty+=20
                            ttx=""
                        ttx+=t
                        w+=1
                    fenetre.blit(font.render(str(ttx),20,(50,50,50)),[xi+rx(5),yty])
                else:
                    fenetre.blit(font.render("Carte Inconnue",20,(0,0,0)),[xi+rx(5),yi])
        pygame.draw.rect(fenetre,(100,50,25),(0,ry(130),j.tex,ry(200)),0)
        pygame.draw.rect(fenetre,(150,150,5),(rx(20),ry(150),j.tex-rx(40),ry(160)),5)
        xx,yy,tx,ty=rx(50),ry(160),rx(80),ry(100)
        for ca in j.deck:
            rcd.append( fenetre.blit(pygame.transform.scale(pygame.image.load("images/fc.png"),[tx+rx(30),ty+ry(30)]),[xx-rx(15),yy]) )
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[ca]),[tx,ty]),[xx,yy+ry(15)])
            xx+=tx+rx(50)
        if len(j.deck)==8: cl=(0,200,0)
        else: cl=(200,0,0)
        fenetre.blit(pygame.font.SysFont("Sans",40).render(str(len(j.deck))+"/ 8",20,cl),[j.tex-rx(150),ry(220)])
        bts[1]=pygame.Rect(j.tex-rx(90),ry(150),rx(65),ry(45))
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/bale.png"),[rx(65),ry(45)]),[j.tex-rx(90),ry(150)])
    elif smenu==3: #menu coffres
        xx,yy=rx(80),ry(150)
        tx,ty=rx(200),ry(200)
        for cf in cftpp:
            rcf.append( fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[cf]),[tx,ty]),[xx,yy]) )
            fenetre.blit(font.render(cfnom[cf],20,(250,250,250)),[xx,yy+ty+ry(5)])
            if j.argent >= cfarg[cf]: clf=(150,145,15)
            else: clf=(180,0,0)
            fenetre.blit(font.render(str(cfarg[cf])+" or",20,clf),[xx,yy+ty+ry(25)])
            xx+=tx+rx(80)
            if xx >= j.tex-tx+1:
                xx=rx(80)
                yy+=ty+ry(80)
    elif smenu==4:  #menu pararametres
        fenetre.blit(font.render("résolution de l'écran : ",0,(250,250,250)),[rx(300),ry(180)])
        lbpr.append( fenetre.blit(pygame.transform.scale(pygame.image.load("images/fl.png"),[int(40/1200*j.tex),int(30/1000*j.tey)]),[int(355/1200*j.tex),int(250/1000*j.tey)])                             )
        lbpr.append( fenetre.blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load("images/fl.png"),[int(40/1200*j.tex),int(30/1000*j.tey)]),1,0),[int(80/1200*j.tex),int(250/1000*j.tey)])   )
        lbpr.append( fenetre.blit(pygame.transform.scale(pygame.image.load("images/fl.png"),[int(40/1200*j.tex),int(30/1000*j.tey)]),[int(755/1200*j.tex),int(250/1000*j.tey)])                             )
        lbpr.append( fenetre.blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load("images/fl.png"),[int(40/1200*j.tex),int(30/1000*j.tey)]),1,0),[int(480/1200*j.tex),int(250/1000*j.tey)])  )
        lbpr.append( pygame.draw.rect(fenetre,(0,0,0),(int(140/1200*j.tex),int(240/1000*j.tey),int(200/1200*j.tex),int(50/1000*j.tey)),5)                                                                   )
        lbpr.append( pygame.draw.rect(fenetre,(0,0,0),(int(540/1200*j.tex),int(240/1000*j.tey),int(200/1200*j.tex),int(50/1000*j.tey)),5)                                                                   )
        lbpr.append( fenetre.blit(pygame.transform.scale(pygame.image.load("images/apl.png"),[int(150/1200*j.tex),int(100/1000*j.tey)]),[j.tex/2,j.tey-int(170/1000*j.tey)])                                  )
        fenetre.blit(font.render(str(j.teex),0,(250,250,250)),[int(150/1200*j.tex),int(250/1000*j.tey)])
        fenetre.blit(font.render(str(j.teey),0,(250,250,250)),[int(550/1200*j.tex),int(250/1000*j.tey)])
        bts[15]=fenetre.blit( pygame.transform.scale(pygame.image.load("images/brac.png"),[int(200/1200*j.tex),int(100/1000*j.tey)]) , [int(100/1200*j.tex),int(600/1000*j.tey)] )
        if j.sos==1: fenetre.blit(font.render("systeme d'exploitation : windows",20,(200,200,200)),[int(500/1200*j.tex),int(400/1000*j.tey)])
        else: fenetre.blit(font.render("systeme d'exploitation : linux",20,(200,200,200)),[int(500/1200*j.tex),int(400/1000*j.tey)])
        bts[16]=pygame.draw.rect(fenetre,(0,100,150),(int(850/1200*j.tex),int(370/1000*j.tey),int(150/1200*j.tex),int(70/1000*j.tey)),0)
        pygame.draw.rect(fenetre,(0,0,0),(int(850/1200*j.tex),int(370/1000*j.tey),int(150/1200*j.tex),int(70/1000*j.tey)),5)
        fenetre.blit(font.render("changer",20,(140,160,160)),[int(880/1200*j.tex),int(400/1000*j.tey)])
        if j.modlp==1: fenetre.blit(font.render("commande pour lancer : python3",20,(200,200,200)),[int(500/1200*j.tex),int(550/1000*j.tey)])
        else: fenetre.blit(font.render("commande pour lancer : python",20,(200,200,200)),[int(500/1200*j.tex),int(550/1000*j.tey)])
        bchlp=pygame.draw.rect(fenetre,(0,100,150),(int(850/1200*j.tex),int(530/1000*j.tey),int(150/1200*j.tex),int(70/1000*j.tey)),0)
        pygame.draw.rect(fenetre,(0,0,0),(int(850/1200*j.tex),int(530/1000*j.tey),int(150/1200*j.tex),int(70/1000*j.tey)),5)
        fenetre.blit(font.render("changer",20,(140,160,160)),[int(880/1200*j.tex),int(550/1000*j.tey)])
        if j.mpar==1: col=(0,250,0)
        else: col=(250,0,0)
        bts[10]=pygame.draw.rect(fenetre,col,(int(800/1200*j.tex),int(700/1000*j.tey),int(150/1200*j.tex),int(75/1000*j.tey)),0)
        pygame.draw.rect(fenetre,(0,0,0),(int(800/1200*j.tex),int(700/1000*j.tey),int(150/1200*j.tex),int(75/1000*j.tey)),5)
        fenetre.blit(font.render("musique",20,(0,0,0)),[int(810/1200*j.tex),int(710/1000*j.tey)])
        bren=pygame.draw.rect(fenetre,(100,100,100),(int(100/1200*j.tex),int(400/1000*j.tey),int(250/1200*j.tex),int(75/1000*j.tey)),0)
        pygame.draw.rect(fenetre,(0,0,0),(int(100/1200*j.tex),int(400/1000*j.tey),int(250/1200*j.tex),int(75/1000*j.tey)),5)
        fenetre.blit(font.render("rénitialiser le compte",20,(0,0,0)),[int(110/1200*j.tex),int(410/1000*j.tey)])
        button("limite fps : "+str(j.fpsmax),rx(110),ry(900),rx(200),ry(75),(200,200,200),(20,15,5))
        bts[20]=button("augmenter",rx(310),ry(900),rx(100),ry(75),(20,100,200),(0,0,0))
        bts[21]=button("diminuer",rx(10),ry(900),rx(100),ry(75),(200,100,20),(0,0,0))
        if False: bts[22]=button("mettre à jour",rx(100),ry(800),rx(150),ry(75),(0,200,0),(0,0,0))
    elif smenu==5:  #menu credit
        clt=(215,215,215)
        fenetre.blit(font.render("Développeur : ",20,clt),[int(100/1200*j.tex),int(200/1000*j.tey)])
        fenetre.blit(font.render("-Nathan Cerisara",20,clt),[int(120/1200*j.tex),int(230/1000*j.tey)])
        fenetre.blit(font.render("Dessinateur : ",20,clt),[int(100/1200*j.tex),int(270/1000*j.tey)])
        fenetre.blit(font.render("-Nathan Cerisara",20,clt),[int(120/1200*j.tex),int(300/1000*j.tey)])
        fenetre.blit(font.render("Musiques : ",20,clt),[int(100/1200*j.tex),int(350/1000*j.tey)])
        fenetre.blit(font.render("-menu : ",20,clt),[int(120/1200*j.tex),int(380/1000*j.tey)])
        fenetre.blit(font.render("-'https://opengameart.org/content/soft-mysterious-harp-loop', license:CC-BY 3.0",20,clt),[int(140/1200*j.tex),int(410/1000*j.tey)])
        fenetre.blit(font.render("-'https://opengameart.org/content/titlemenu-screen-bgm', license:CC-BY-SA 3.0",20,clt),[int(140/1200*j.tex),int(440/1000*j.tey)])
    elif smenu==6:  #menu arenes
        xxx,yyy=int(150/1200*j.tex),int(150/1000*j.tey)
        txx,tyy=int(300/1200*j.tex),int(400/1000*j.tey)
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[arsel])+"_3.png"),[txx,tyy]),[xxx,yyy])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[arsel])+"_1.png"),[txx-10,int(tyy/2-10)]),[xxx+5,yyy+5])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[arsel])+"_1.png"),[txx-10,int(tyy/2-10)]),[xxx+5,yyy+tyy/2+5])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[arsel])+"_2.png"),[int(70/1200*txx),int(100/1000*tyy)]),[xxx+30,yyy+tyy/2-20])
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/mape_"+str(aimg[arsel])+"_2.png"),[int(70/1200*txx),int(100/1000*tyy)]),[xxx+txx-60,yyy+tyy/2-20])
        fenetre.blit(font.render(anom[arsel],20,(150,150,150)),[int(150/1200*j.tex),int(720/1000*j.tey)])
        fenetre.blit(font.render("trophés : "+str(atro[arsel]),20,(150,150,150)),[int(150/1200*j.tex),int(760/1000*j.tey)])
        if arsel < len(atpp)-1 : bts[12]=fenetre.blit(pygame.transform.scale(pygame.image.load("images/flch.png"),[int(50/1200*j.tex),int(100/1000*j.tey)]),[j.tex-int(60/1200*j.tex),int(450/1000*j.tey)])
        if arsel > 0           : bts[11]=fenetre.blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load("images/flch.png"),[int(50/1200*j.tex),int(100/1000*j.tey)]),1,0),[int(60/1200*j.tex),int(450/1000*j.tey)])
        xxx,yyy=int(480/1200*j.tex),int(150/1000*j.tey)
        txx,tyy=int(70/1200*j.tex),int(110/1000*j.tey)
        acrts=[]
        for c in ctpp:
            if c!=0 and c!=1 and care[c]==arsel: acrts.append(c)
        for c in acrts:
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[c]),[txx,tyy]),[xxx,yyy])
            pygame.draw.rect(fenetre,craret[crar[c]],(xxx,yyy,txx,tyy),2)
            fenetre.blit(pygame.transform.scale(font.render(cnom[c],20,cl),[txx,int(20/1000*j.tey)]),[xxx,yyy+tyy+5])
            xxx+=txx+10
            if xxx >= j.tex-txx-40:
                xxx=int(480/1200*j.tex)
                yyy+=tyy+30
    elif smenu==8:  #menu aide/tutoriel
        fona=pygame.font.SysFont("Georgia",20)
        clt=(0,0,0)
        pygame.draw.rect(fenetre,(150,20,150),(int(100/1200*j.tex),int(200/1000*j.tey),int(1000/1200*j.tex),int(700/1000*j.tey)),0)
        pygame.draw.rect(fenetre,(0,0,0),(int(100/1200*j.tex),int(200/1000*j.tey),int(1000/1200*j.tex),int(700/1000*j.tey)),5)
        if pageaide < pageaidetot : bts[14]=fenetre.blit(pygame.transform.scale(pygame.image.load("images/flch.png"),[int(50/1200*j.tex),int(100/1000*j.tey)]),[j.tex-int(60/1200*j.tex),int(450/1000*j.tey)])
        if pageaide > 1           : bts[13]=fenetre.blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load("images/flch.png"),[int(50/1200*j.tex),int(100/1000*j.tey)]),1,0),[int(20/1200*j.tex),int(450/1000*j.tey)])
        if pageaide==1:
            fenetre.blit(fona.render("AIDE CLASH OF FIGHTERS - PAGE N°1"                                                                ,30,clt),[int(350/1200*j.tex),int(200/1000*j.tey)])
            fenetre.blit(fona.render("Le but du jeu est de détruire les tours ennemies tout en gardant les siennes"                     ,30,clt),[int(120/1200*j.tex),int(260/1000*j.tey)])
            fenetre.blit(fona.render("Il faut créer un deck de 8 cartes dans le menu [Cartes]."                                         ,30,clt),[int(120/1200*j.tex),int(300/1000*j.tey)])
            fenetre.blit(fona.render("Pour mettre une carte dans le deck, il faut double-cliquez sur la carte"                          ,30,clt),[int(120/1200*j.tex),int(340/1000*j.tey)])
            fenetre.blit(fona.render("Pour enlever une carte du deck, c'est la même chose : double-cliquer dessus"                      ,30,clt),[int(120/1200*j.tex),int(380/1000*j.tey)])
            fenetre.blit(fona.render("Pour lancer une partie, il faut cliquer sur le bouton [Play] dans le menu [Combat]"               ,30,clt),[int(120/1200*j.tex),int(420/1000*j.tey)])
            fenetre.blit(fona.render("Quand une partie est lancée, toutes les cartes du deck sont consommées une fois"                  ,30,clt),[int(120/1200*j.tex),int(460/1000*j.tey)])
            fenetre.blit(fona.render("Lors d'une partie, pour jouer une carte, il faut cliquer dessus dans le menu à droite"            ,30,clt),[int(120/1200*j.tex),int(500/1000*j.tey)])
            fenetre.blit(fona.render("Puis il faut cliquer à l'endroit ou vous voulez poser votre carte"                                ,30,clt),[int(120/1200*j.tex),int(540/1000*j.tey)])
            fenetre.blit(fona.render("Une carte consomme de l'elixir, vous gagnez de l'elixir régulierement"                            ,30,clt),[int(120/1200*j.tex),int(580/1000*j.tey)])
            fenetre.blit(fona.render("L'indicateur d'élixir est une barre violette à droite"                                            ,30,clt),[int(120/1200*j.tex),int(620/1000*j.tey)])
            fenetre.blit(fona.render("Il y a du temps pour finir une partie, si les 3 tours ennemies ne sont pas détruite"              ,30,clt),[int(120/1200*j.tex),int(660/1000*j.tey)])
            fenetre.blit(fona.render("Au bout de 300 secondes, celui qui aura détruit le plus de tour gagne"                            ,30,clt),[int(120/1200*j.tex),int(700/1000*j.tey)])
            fenetre.blit(fona.render("A la fin d'une partie, le vainqueur recois des trophés et de l'or"                                ,30,clt),[int(120/1200*j.tex),int(740/1000*j.tey)])
            fenetre.blit(fona.render("Le perdant, lui, perd des trophés et gagne beaucoup moins d'or"                                   ,30,clt),[int(120/1200*j.tex),int(780/1000*j.tey)])
        if pageaide==2:
            fenetre.blit(fona.render("AIDE CLASH OF FIGHTERS - PAGE N°2"                                                                ,30,clt),[int(350/1200*j.tex),int(200/1000*j.tey)])
            fenetre.blit(fona.render("Pour ouvrir un coffre, il faut aller dans le menu [Coffre], puis cliquer sur le coffre désiré"    ,30,clt),[int(120/1200*j.tex),int(260/1000*j.tey)])
            fenetre.blit(fona.render("Dans le jeu, il y a une monnaie virtuelle : l'or"                                                 ,30,clt),[int(120/1200*j.tex),int(300/1000*j.tey)])
            fenetre.blit(fona.render("Un coffre coûte de l'or, il y a différents types de coffres"                                      ,30,clt),[int(120/1200*j.tex),int(340/1000*j.tey)])
            fenetre.blit(fona.render("Un coffre donne des cartes et un peu d'or"                                                        ,30,clt),[int(120/1200*j.tex),int(380/1000*j.tey)])
            fenetre.blit(fona.render("Chaque coffre a un nombre de carte différents par rareté de carte"                                ,30,clt),[int(120/1200*j.tex),int(420/1000*j.tey)])
            fenetre.blit(fona.render("Il y a 5 niveaux de rareté : "                                                                    ,30,clt),[int(120/1200*j.tex),int(460/1000*j.tey)])
            fenetre.blit(fona.render("Commun , rare , épique , légendaire , divin"                                                      ,30,clt),[int(120/1200*j.tex),int(500/1000*j.tey)])
            fenetre.blit(fona.render("Plus une carte à un niveau de rareté élevé, plus il est difficile d'en trouver"                   ,30,clt),[int(120/1200*j.tex),int(540/1000*j.tey)])
        if pageaide==3:
            fenetre.blit(fona.render("AIDE CLASH OF FIGHTERS - PAGE N°3"                                                                ,30,clt),[int(350/1200*j.tex),int(200/1000*j.tey)])        
            fenetre.blit(fona.render("Pour accéder au paramètres, il faut cliquer sur le bouton[parametres] dans le menu"               ,30,clt),[int(120/1200*j.tex),int(260/1000*j.tey)])
            fenetre.blit(fona.render("Dans les paramètres, il y a possibilité de changer la résolution de la fenetre"                   ,30,clt),[int(120/1200*j.tex),int(300/1000*j.tey)])
            fenetre.blit(fona.render("Il faut éviter de changer la résolution de la fenetre si cela n'est pas nécéssaire"               ,30,clt),[int(120/1200*j.tex),int(340/1000*j.tey)])
            fenetre.blit(fona.render("Le jeu est réglé pour fonctionner à la résolution par défaut"                                     ,30,clt),[int(120/1200*j.tex),int(380/1000*j.tey)])
            fenetre.blit(fona.render("Dans les paramètres, il y a possibilité de créer un raccourci"                                    ,30,clt),[int(120/1200*j.tex),int(420/1000*j.tey)])
            fenetre.blit(fona.render("Attention! Le raccourcis ne sera pas créé directement sur le Bureau, il faudra le déplacer"       ,30,clt),[int(120/1200*j.tex),int(460/1000*j.tey)])
            fenetre.blit(fona.render("Il y a aussi possibilité de changer la commande de lancement du jeu"                              ,30,clt),[int(120/1200*j.tex),int(500/1000*j.tey)])
            fenetre.blit(fona.render("Si la commande par défaut ne marche pas, il faut la changer"                                      ,30,clt),[int(120/1200*j.tex),int(540/1000*j.tey)])
            fenetre.blit(fona.render("De même pour le système d'exploitation"                                                           ,30,clt),[int(120/1200*j.tex),int(580/1000*j.tey)])
    elif smenu==9: #profil
        texte(int(j.tex/2),ry(150),"Profil",(0,100,100),45)
        texte(rx(100),ry(210),"pseudo : "+j.nom,(0,0,0),20)
        texte(rx(300),ry(210),"niv : "+str(j.niveau),(0,0,0),20)
        grxx,gryy,grtx,grty=rx(100),ry(300),rx(1000),ry(150)
        pygame.draw.rect(fenetre,(200,200,250),(grxx,gryy,int(j.exp/j.xpmax*grtx),grty),0)
        pygame.draw.rect(fenetre,(250,250,250),(grxx,gryy,grtx,grty),5)
        texte(grxx-60+int(j.exp/j.xpmax*grtx),gryy+20,str(j.exp)+"/"+str(j.xpmax),(0,0,250),20)
        bts[19]=button("historique",rx(50),ry(850),rx(100),ry(50),(150,150,5),(10,10,10))
    elif smenu==10: #historique
        #0=j1 deck 1=j1 deck 2=joueur victorieux 3=j1 crowns 4=j2 crowns 5=j1 nom 6=j2 nom 7=nbj1
        nbh=5
        lsh=lhisto()[::-1]
        hx,hy=rx(50),ry(150)
        htx,hty=rx(1000),ry(140)
        for hh in lsh[:nbh]:
            if hh[7]==1: cln1,cln2=(0,0,150),(150,0,0)
            else: cln2,cln1=(0,0,150),(150,0,0)
            pygame.draw.rect(fenetre,(200,200,200),(hx,hy,htx,hty),0)
            pygame.draw.rect(fenetre,(0,0,0),(hx,hy,htx,hty),2)
            ##1
            pygame.draw.rect(fenetre,cln1,(hx+rx(0),hy+ry(5),rx(450),hty-rx(5)),3)
            texte(hx+rx(10),hy+ry(10),hh[5],cln1,20)
            xxx,yyy=hx+rx(10),hy+ry(50)
            hxt,hyt=rx(40),ry(60)
            for c in hh[0]:
                fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[c]),[hxt,hyt]),[xxx,yyy])
                crt=pygame.draw.rect(fenetre,craret[crar[c]],(xxx,yyy,hxt,hyt),2)
                xxx+=hxt+rx(15)
            xxx,yyy=hx+rx(350),hy+ry(10)
            hxt,hyt=rx(20),ry(20)
            for x in range(hh[3]):
                fenetre.blit(pygame.transform.scale(pygame.image.load("images/crown.png"),[hxt,hyt]),[xxx,yyy])
                xxx+=hxt+rx(5)
            for x in range(3-hh[3]):
                fenetre.blit(pygame.transform.scale(pygame.image.load("images/uncrown.png"),[hxt,hyt]),[xxx,yyy])
                xxx+=hxt+rx(5)
            ##2
            pygame.draw.rect(fenetre,cln2,(hx+rx(550),hy+ry(5),rx(450),hty-rx(5)),3)
            texte(hx+rx(880 ),hy+ry(10),hh[6],cln2,20)
            xxx,yyy=hx+rx(560),hy+ry(50)
            hxt,hyt=rx(40),ry(60)
            for c in hh[1]:
                fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[c]),[hxt,hyt]),[xxx,yyy])
                crt=pygame.draw.rect(fenetre,craret[crar[c]],(xxx,yyy,hxt,hyt),2)
                xxx+=hxt+rx(15)
            xxx,yyy=hx+rx(570),hy+ry(10)
            hxt,hyt=rx(20),ry(20)
            for x in range(hh[4]):
                fenetre.blit(pygame.transform.scale(pygame.image.load("images/crown.png"),[hxt,hyt]),[xxx,yyy])
                xxx+=hxt+rx(5)
            for x in range(3-hh[4]):
                fenetre.blit(pygame.transform.scale(pygame.image.load("images/uncrown.png"),[hxt,hyt]),[xxx,yyy])
                xxx+=hxt+rx(5)
            ##
            if (hh[7]==1 and hh[2]==1) or (hh[7]==2 and hh[2]==2):  txtt,cltt="victoire",(0,200,0)
            elif (hh[7]==1 and hh[2]==2) or (hh[7]==2 and hh[2]==1): txtt,cltt="défaite",(200,0,0)
            else: txtt,cltt="égalité",(160,140,0)
            fenetre.blit(font.render(txtt,20,cltt),[hx+rx(460),hy+ry(10)])
            hy+=hty+rx(25)
    pygame.display.update()
    return rcs,rcf,rcd,lbpr,bchlp,bren,bts,barensl

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
    elif c==6:
        cfcrt=[ [1,0] ]
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
    if c==6:
        r0=[1,1]
    for cc in crts:
        if crar[cc]==0: nbcr.append(random.randint(r0[0],r0[1]))
        elif crar[cc]==1: nbcr.append(random.randint(r1[0],r1[1]))
        elif crar[cc]==2: nbcr.append(random.randint(r2[0],r2[1]))
        elif crar[cc]==3: nbcr.append(random.randint(r3[0],r3[1]))
        elif crar[cc]==4: nbcr.append(random.randint(r4[0],r4[1]))
        else: nbcr.append(1)
    fenetre.fill((10,0,50))
    fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*j.tex),int(cftyy[c]/1000*j.tey)]),[j.tex/4,j.tey/4])
    pygame.display.update()
    njk=0
    for x in range(100):
            fenetre.fill((10,0,50))
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*j.tex),int(cftyy[c]/1000*j.tey)]),[j.tex/4,j.tey/4])
            pygame.draw.rect(fenetre,(100,100,0),(j.tex/3,j.tey/3,x*2,int(x*2.5)),5)
            fenetre.blit(pygame.transform.scale(font.render("or : "+str(ore),20,(150,150,20)),[x*2,int(x*2.5)]),[j.tex/3,j.tey/3])
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
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*j.tex),int(cftyy[c]/1000*j.tey)]),[j.tex/4,j.tey/4])
            pygame.draw.rect(fenetre,craret[crar[cc]],(j.tex/3,j.tey/3,x*2,int(x*2.5)),5)
            fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[cc]),[x*2,int(x*2.5)]),[j.tex/3,j.tey/3])
            fenetre.blit(pygame.transform.scale(font.render(cnom[cc]+"  ("+str(nbcr[crts.index(cc)])+")",20,(200,200,200)),[x*2,int(x*1.001)]),[j.tex/3,j.tey/3.5])
            pygame.display.update()
            time.sleep(0.01)
            for event in pygame.event.get():
                if event.type==MOUSEBUTTONUP:
                    njk=1
            if njk==1:
                break
        if j.cartdeb[cc]==0:
                deblocrt(cc)
                j.cartdeb[cc]=1
        if njk!=1:
            ac()
            time.sleep(0.5)
    time.sleep(0.6)
    fenetre.fill((10,0,50))
    fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cfimg[c]),[int(cftxx[c]/1200*j.tex),int(cftyy[c]/1000*j.tey)]),[j.tex/4,j.tey/4])
    xx,yy=int(50/1200*j.tex),int(50/1000*j.tey)
    txx,tyy=int(120/1200*j.tex),int(170/1000*j.tey)
    pygame.draw.rect(fenetre,(100,100,0),(xx,yy,txx,tyy),5)
    fenetre.blit(pygame.transform.scale(font.render("or : "+str(ore),20,(100,100,0)),[txx,tyy]),[xx,yy])
    xx+=txx+20
    pygame.display.update()
    for cc in crts:
        pygame.draw.rect(fenetre,craret[crar[cc]],(xx,yy,txx,tyy),5)
        fenetre.blit(pygame.transform.scale(pygame.image.load("images/"+cimg[cc]),[txx,tyy]),[xx,yy])
        fenetre.blit(pygame.transform.scale( font.render(cnom[cc]+" ("+str(nbcr[crts.index(cc)])+")",20,(200,200,200)) ,[txx,25] ),[xx,yy+tyy])
        xx+=txx+20
        if xx >= j.tex-txx-20:
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
    ltxt=[]
    nbl=40
    if len(txt) < nbl: ltxt.append(txt)
    else:
        for dd in range(int(len(txt)/nbl)):
            if dd<=len(txt)/50: ltxt.append(txt[dd*nbl:(dd+1)*nbl])
        try: ltxt.append(txt[(dd+1)*nbl:len(txt)])
        except: pass
    bx,by,btx,bty=int(j.tex/3),int(j.tey/3),int(500/1200*j.tex),int(350/1000*j.tey)
    pygame.draw.rect(fenetre,(50,10,100),(bx,by,btx,bty),0)
    pygame.draw.rect(fenetre,(10,10,10),(bx,by,btx,bty),5)
    ky=0
    for xt in ltxt:
        fenetre.blit(font.render(xt,20,(200,200,200)),[bx+15,by+15+ky])
        ky+=25
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
"""
#MAJ
def maj():
    ##aff
    pygame.draw.rect(fenetre,(150,150,25),(rx(100),ry(100),rx(1000),ry(800)),0)
    pygame.draw.rect(fenetre,(15,15,25),(rx(100),ry(100),rx(1000),ry(800)),5)
    fenetre.blit( pygame.font.SysFont("Serif",40).render("Mise à jour en cour",20,(0,0,0)) , [rx(500),ry(150)])
    fenetre.blit( pygame.font.SysFont("Serif",20).render("Cela peut prendre quelques minutes en fonction de votre connection",20,(0,0,0)) , [rx(200),ry(300)])
    fenetre.blit( pygame.font.SysFont("Serif",20).render("Si il y a un problème, veuillez réinstaller la nouvelle version manuellement ",20,(0,0,0)) , [rx(200),ry(400)])
    fenetre.blit( pygame.font.SysFont("Serif",20).render("depuis https://github.com/nath54/royal",20,(0,0,0)) , [rx(200),ry(500)])
    pygame.display.update()
    ##
    import os,shutil
    if "royal.zip" in os.listdir("../"): os.remove("../royal.zip")
    if "royal-master.zip" in os.listdir("../"): os.remove("../royal-master.zip")
    if "maj.py" in os.listdir("../"): os.remove("../maj.py")
    if "royale" in os.listdir("../"): shutil.rmtree("../royale")
    if "royale_maj" in os.listdir("../"): shutil.rmtree("../royale_maj")
    ##
    url="https://github.com/nath54/royal/archive/master.zip"
    from urllib.request import urlopen
    with open('../royal.zip', 'wb') as fich:
        fich.write(urlopen(url).read())
    import zipfile
    with zipfile.ZipFile("../royal.zip", "r") as z:
        z.extractall("../royale")
    ##
    shutil.copyfile(dire+fichs,"../royale/royal-master/"+fichs)
    shutil.copyfile(dire+fichp,"../royale/royal-master/"+fichp)
    shutil.copyfile(dire+fichh,"../royale/royal-master/"+fichh)
    shutil.copyfile(dire+ficht,"../royale/royal-master/"+ficht)
    shutil.copyfile(dire+fichd,"../royale/royal-master/"+fichd)
    os.rename("../royale/royal-master","../royale_maj")
    alertbox("Le programme va se quitter pour installer la mise à jour, quand la mise à jour sera installée, veuillez relancer le programme")
    ##
    dd=os.getcwd()
    ddd=""
    for d in list(dd):
        if d!="\\":
            ddd+=d
        else: ddd+="\\\\"
    if j.modlp==1: lp="3"
    else: lp=""
    txt=
    #coding:utf-8
    import shutil,os,time
    print("Mise a jour en cour d'installation")
    time.sleep(1)
    dd='""""""'
    os.system("cd "+dd+"/../")
    ddd=dd
    shutil.rmtree(ddd)
    os.rename("royale_maj",ddd)
    os.remove("royal.zip")
    os.rmdir("royale")
    import subprocess
    os.system("cd "+ddd)
    proc= subprocess.Popen('python"""""" main.py', shell=True)
    exit()
    f=open("../maj.py","w")
    f.write(txt)
    f.close()
    proc= subprocess.Popen("python "+"../maj.py", shell=True)
    print("Exit")
    exit()
    """


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
    ###
    condd=True
    nvff=False
    if not "dc.nath" in os.listdir():
            condd=True
            nvff=True
    else:
        ddd=open("dc.nath","r").read().split("#")
        for d in ddd:
            dd=d.split("|")
            if dd[0]==str(date.tm_mday) and dd[1]==str(date.tm_mon) and dd[2]==str(date.tm_year): condd=False
    if condd:
        alertbox("Cadeau : 500 or !")
        j.argent+=500
        if nvff: txt=""
        else: txt="#"
        txt+=str(date.tm_mday)+"|"+str(date.tm_mon)+"|"+str(date.tm_year)
        ff=open("dc.nath","a")
        ff.write(txt)
        ff.close()
    save(j)
            
def cracourcis():
    try:
        if j.sos==1: rac=open("clash_of_fighters.cmd","w")
        else: rac=open("clash_of_fighters.bash","w")
        dire=os.getcwd()
        ###
        if j.modlp==1: coml="python3 main.py"
        else: coml="python main.py"
        txt="cd "+dire+"\n"+coml
        rac.write(txt)
        rac.close()
        alertbox("Le racourcis a été créé dans le dossier du jeu ("+dire+")")
    except:
        alertbox("désolé, le racourcis n'a pas pus etre créé")
        #TODO
        #rac=open("/home/Desktop/clash_of_fighters.bin","w")
    

##################################################

fenetre=pygame.display.set_mode([j.tex,j.tey])
pygame.display.set_caption("THE CLASH OF FIGHTERS")
fenetre.blit(pygame.transform.scale(pygame.image.load("images/fmenu.png"),[j.tex,j.tey]),[0,0])
pygame.display.update()
time.sleep(1)
dc=time.time()
tdc=0.5

if version < dv and dv != 0.0:
    alertbox("Une mise à jour est disponible")

if dpseudo:
    j.nom=textbox.main(j.nom,j.tex,j.tey)

mus=["Music/Dream.mp3","Music/Harp.mp3"]
musmenu=pygame.mixer.music.load(random.choice(mus))
if j.mpar==1: pygame.mixer.music.play()


vdate()

needtoaff=True

encour=True
while encour:
    while j.exp >= j.xpmax:
        j.exp=j.exp-j.xpmax
        j.niveau+=1
        j.xpmax=j.xpmax+int(float(j.xpmax)*0.3)
    if needtoaff:
        rcs,rcf,rcd,lbpr,bchlp,bren,bts,barensl=aff()
        needtoaff=False
    if smenu==4:
        pygame.draw.rect(fenetre,(50,20,100),(int(18/1200*j.tex),int(118/1000*j.tey),int(500/1200*j.tex),int(40/1000*j.tey)),0)
        tt=int(temps())
        if tt < 60: fenetre.blit(font.render("temps joué au jeu : "+str(tt)+" sec",0,(250,250,250)),[int(20/1200*j.tex),int(120/1000*j.tey)])
        elif tt > 60 and tt < 3600: fenetre.blit(font.render("temps joué au jeu : "+str(int(tt/60))+" min",0,(250,250,250)),[int(20/1200*j.tex),int(120/1000*j.tey)])
        else: fenetre.blit(font.render("temps joué au jeu : "+str(int(tt/3600))+" heures",0,(250,250,250)),[int(20/1200*j.tex),int(120/1000*j.tey)])
        pygame.display.update()
    for cc in j.deck:
        if j.cartpos[cc]==0: del(j.deck[j.deck.index(cc)])
    for event in pygame.event.get():
        if event.type==QUIT: encour=False
        elif event.type==KEYDOWN:
            if event.key==K_q: encour=False
            elif event.key==K_e: smenu=8
            needtoaff=True
        elif event.type==MOUSEBUTTONUP:
            needtoaff=True
            pos=pygame.mouse.get_pos()
            rpos=pygame.Rect(pos[0],pos[1],1,1)
            if False: pass
            elif rpos.colliderect(bchlp):
                if j.modlp==1: j.modlp=2
                else: j.modlp=1
            elif rpos.colliderect(bren):
                etren+=1
                if etren==1:
                    alertbox("Êtes vous vraiment sur ?")
                    alertbox("Si vous voulez vraiment rénitialiser votre compte, veuillez rappuyer sur le bouton rénitialiser")
                elif etren==2:
                    alertbox("Votre compte a été rénitialisé")
                    alertbox("Veuillez relancer le jeu.")
                    if fichs in os.listdir() : os.remove(fichs)
                    if "dc.nath" in os.listdir() : os.remove("dc.nath")
                    if "recompget.nath" in os.listdir() : os.remove("recompget.nath")
                    exit()
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
            #params
            if len(lbpr)>=7:
                dt=50
                if rpos.colliderect(lbpr[0]): j.teex+=dt
                elif rpos.colliderect(lbpr[1]): j.teex-=dt
                elif rpos.colliderect(lbpr[2]): j.teey+=dt
                elif rpos.colliderect(lbpr[3]): j.teey-=dt
                elif rpos.colliderect(lbpr[4]): 
                    import textbox
                    xet=textbox.main(str(j.tex),j.tex,j.tey)
                    try:
                        xet=int(xet)
                        if xet >= 500 and xet <= 2100: j.teex=xet
                        else: alertbox("Vous devez rentrer un nombre compris entre 500 et 2100")
                    except: alertbox("Vous n'avez pas écrit un nombre !")
                elif rpos.colliderect(lbpr[5]): 
                    import textbox
                    yet=textbox.main(str(j.tey),j.tex,j.tey)
                    try:
                        yet=int(yet)
                        if yet >= 400 and yet <= 2000: j.teey=yet
                        else: alertbox("Vous devez rentrer un nombre compris entre 400 et 2000")
                    except: alertbox("Vous n'avez pas écrit un nombre !")
                elif rpos.colliderect(lbpr[6]):
                    save(j)
                    alertbox("Veuillez relancer le jeu pour appliquer les parametres")
                    encour=False
            for bb in barensl:
                if bb!=None:
                    if rpos.colliderect(bb):
                        if barensl.index(bb) <= j.arene:
                            j.barensl=barensl.index(bb)
            ###for bouton in boutons
            for bt in bts:
                if bt != None:
                    if rpos.colliderect(bt):
                        di=bts.index(bt)
                        if di==0:
                            if len(j.deck)==8:
                                if j.modlp==1:
                                    try: subprocess.call("python3 a.py")
                                    except: os.system("python3 a.py")
                                else:
                                    try: subprocess.call("python a.py")
                                    except: os.system("python a.py")
                                fenetre.blit(pygame.font.SysFont("Serif",50).render("si votre partie est finie, cliquez",0,(0,200,150)),[20,j.tey/2])
                                pygame.display.update()
                                ac()
                                j=load(j)
                                musmenu=pygame.mixer.music.load(random.choice(mus))
                                if j.mpar==1: pygame.mixer.music.play()
                            else:
                                alertbox("votre deck n'est pas composé de 8 cartes !")
                        elif di==1: j.deck=deckale(j)
                        elif di==2: scrtm-=nbcm
                        elif di==3: scrtm+=nbcm
                        elif di==4: smenu=4
                        elif di==5: smenu=5
                        elif di==6: smenu=1
                        elif di==7: smenu=2
                        elif di==8: smenu=3
                        elif di==9: smenu,arsel=6,j.arene
                        elif di==10:
                            if j.mpar==1: j.mpar=2
                            else: j.mpar=1
                        elif di==11:
                            if arsel > 0: arsel-=1
                        elif di==12:
                            if arsel < len(atpp): arsel+=1
                        elif di==13: pageaide-=1
                        elif di==14: pageaide+=1
                        elif di==15: cracourcis()
                        elif di==16:
                            if j.sos==1: j.sos=2
                            else: j.sos=1
                        elif di==17: smenu=8
                        elif di==18: smenu=9
                        elif di==19: smenu=10
                        elif di==20: j.fpsmax+=5
                        elif di==21:
                            j.fpsmax-=5
                            if j.fpsmax < 5: j.fpsmax=5
                        #elif di==22: maj()
            ###
            save(j)
    


savetps()





