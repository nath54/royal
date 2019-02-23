#coding:utf-8
from cartes import *
from lib2 import *
from lib3 import *

class Joueure:
    def __init__(self):
        self.nom="None"
        self.deck=[]
        self.argent=0
        self.trophes=0
        self.cartpos=[]
        self.arene=1
        for ar in atpp:
            if self.trophes >= atro[ar]: self.arene=ar
        self.exp=0
        self.niveau=0
        self.xpmax=100
        self.arensl=None
        self.fpsmax=60
        self.tex=100
        self.tey=70
    

def save(j):
    #stats
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
    t7=""
    for jj in j.cartdeb: t7+=str(jj)+"|"
    t7=t7[:-1]
    t8=str(j.exp)
    t9=str(j.niveau)
    if j.arensl != None: t10=str(j.arensl)
    else: t10="N"
    txt=t1+cac+t2+cac+t3+cac+t4+cac+t5+cac+t6+cac+t7+cac+t8+cac+t9+cac+t10
    ff=open(dire+fichs,"w")
    ff.write(txt)
    ff.close()
    #params
    txt=str(j.teex)+cac+str(j.teey)+cac+str(j.sos)+cac+str(j.modlp)+cac+str(j.mpar)+cac+str(j.fpsmax)
    ff=open(dire+fichp,"w")
    ff.write(txt)
    ff.close()



def load(j):
    jjr=open(dire+fichs,"r").read().split("#")
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
    try: ara,ran=jjr[6].split("|"),[]
    except: ara=[],ran=[]
    for a in ara:
        try: ran.append(int(a))
        except: ran.append(0)
    j.cartdeb=ran
    while len(ctpp)>len(j.cartpos): j.cartpos.append(0)
    aa=0
    while len(ctpp)>len(j.cartdeb): 
        if j.cartpos[aa]>0: j.cartdeb.append(1)
        else: j.cartdeb.append(0)
        aa+=1
    j.arene=1
    for ar in atpp:
        if j.trophes >= atro[ar]: j.arene=ar
    j.exp=int(jjr[7])
    j.niveau=int(jjr[8])
    j.xpmax=int(100)
    if jjr[9][0]=="N": j.arensl=None
    else:    j.arensl=int(jjr[9])
    for x in range(j.niveau-1): j.xpmax=j.xpmax+int(j.xpmax*0.3)
    spr=open(dire+fichp,"r").read().split("#")
    j.tex=int(spr[0])
    j.tey=int(spr[1])
    print(j.tex,j.tey)
    j.teex=j.tex
    j.teey=j.tey
    j.sos=int(spr[2])
    j.modlp=int(spr[3])
    j.mpar=int(spr[4])
    #print(spr)
    j.fpsmax=int(spr[5])
    return j

def rhisto(j1deck,j2deck,jvict,j1cr,j2cr,j1nom,j2nom,nbj1):
    txt=""
    for a in j1deck:
        txt+=str(a)+ccac
    txt=txt[:-1]+cacc
    for a in j2deck:
        txt+=str(a)+ccac
    txt=txt[:-1]+cacc+str(jvict)+cacc+str(j1cr)+cacc+str(j2cr)+cacc+j1nom+cacc+j2nom+cacc+str(nbj1)+cac
    f=open(fichh,"a")
    f.write(txt)
    f.close()
    #0=deck j1 1=deck j2 2=joueur victorieux 3=j1 crowns 4=j2 crowns 5=j1 nom 6=j2 nom 7=nbj1

def lhisto():
    lst=[]
    f=open(fichh,"r").read().split(cac)
    if f != []:
        for ff in f:
            if len(ff)>5:
                ll=[]
                g=ff.split(cacc)
                g1=g[0].split(ccac)
                lg=[]
                for gg in g1: lg.append( int(gg) )
                ll.append(lg)
                g1=g[1].split(ccac)
                lg=[]
                for gg in g1: lg.append( int(gg) )
                ll.append(lg)
                ll.append(int(g[2]))
                ll.append(int(g[3]))
                ll.append(int(g[4]))
                ll.append(g[5])
                ll.append(g[6])
                ll.append(int(g[7]))
                lst.append(ll)
    return lst

