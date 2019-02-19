#coding:utf-8


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

dire="./"

fichs="stats.nath"
fichp="params.nath"
fichh="historique.nath"
ficht="tps.nath"
fichd="dc.nath"

cac="#"
cacc="|"
ccac="_"



rarete=["commun","rare","epique","legendaire","divin"]
craret=[(0,0,140),(150,105,25),(150,0,150),(20,150,20),(250,250,0)]


f=open(dire+fichp,"r").read().split(cac)
tex,tey=int(f[0]),int(f[1])


def rx(x): return int(x/1200*tex)
def ry(y): return int(y/1000*tey)
def rz(z): return int(z/(1000*1200)*(tex*tey))

