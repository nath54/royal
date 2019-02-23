#coding:utf-8

from lib3 import *


f=open(dire+fichp,"r").read().split(cac)
tex,tey=int(f[0]),int(f[1])


def rx(x): return int(x/1200*tex)
def ry(y): return int(y/1000*tey)
def rz(z): return int(z/(1000*1200)*(tex*tey))




