#coding:utf-8
import os
from os.path import expanduser
home = expanduser("~")

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

cd="/"

dires="royal_stats"
if not dires in os.listdir(home):
    os.mkdir(home+cd+dires)

dire=home+cd+dires+cd

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

ctpp=[0          ,1           ,2           ,3          ,4          ,5            ,6           ,7          ,8          ,9           ,10              ,11         ,12         ,13          ,14          ,15               ,16          ,17         ,18                  ,19                     ,20          ,21           ,22              ,23         ,24                     ,25            ,26          ,27          ,28           ,29            ,30           ,31         ,32             ,33                 ,34           ,35         ,36               ,37                    ,38          ,39         ,40         ,41           ,42                 ,43                  ,44          ,45         ,46           ,47                  ,48             ,49         ,50          ,51         ,52         ,53         ,54          ,55              ]
care=[0          ,0           ,0           ,0          ,0          ,1            ,2           ,2          ,0          ,2           ,0               ,0          ,10         ,10          ,3           ,3                ,3           ,2          ,2                   ,4                      ,10          ,5            ,8               ,1          ,4                      ,2             ,2           ,2            ,9            ,10            ,0            ,4          ,2              ,6                  ,2            ,5          ,2                ,10                    ,6           ,6          ,0          ,1            ,7                  ,3                   ,10          ,10         ,3            ,1                   ,6              ,6          ,6           ,10         ,3          ,9          ,9          ,3               ]

