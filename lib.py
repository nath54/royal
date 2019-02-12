#coding:utf-8
from cartes import *

tex,tey=1000,750
teex,teey=1000,750
smenu=2
scrtm=0
cselec=None
sos=1
modlp=1
arsel=0
mpar=1
etren=0
fichtps="tps.nath"
pageaide=1
pageaidetot=3



fichs="stats.nath"
fichp="params.nath"
fichh="historique.nath"

cac="#"
cacc="|"
ccac="_"


rarete=["commun","rare","epique","legendaire","divin"]
craret=[(0,0,140),(150,105,25),(150,0,150),(20,150,20),(250,250,0)]

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
    txt=t1+cac+t2+cac+t3+cac+t4+cac+t5+cac+t6+cac+t7+cac+t8+cac+t9
    ff=open(fichs,"w")
    ff.write(txt)
    ff.close()
    #params
    txt=str(j.teex)+cac+str(j.teey)+cac+str(j.sos)+cac+str(j.modlp)+cac+str(j.mpar)
    ff=open(fichp,"w")
    ff.write(txt)
    ff.close()



def load(j):
    jjr=open(fichs,"r").read().split("#")
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
    spr=open(fichp,"r").read().split("#")
    j.tex=int(spr[0])
    j.tey=int(spr[1])
    j.teex=tex
    j.teey=tey
    j.sos=int(spr[2])
    j.modlp=int(spr[3])
    j.mpar=int(spr[4])
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



