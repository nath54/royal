#coding:utf-8
tex,tey=1000,800
ctpp=[0          ,1           ,2          ,3          ,4          ,5            ,6           ,7          ,8          ,9           ,10              ,11         ,12         ,13          ,14          ,15               ,16          ,17         ,18                  ,19                     ,20            ]
cnom=["tour1"    ,"tour2"     ,"chevalier","archer"   ,"mage"     ,"petit golem","golem"     ,"fantome"  ,"princesse","squelettes","tour a canons" ,"le géant" ,"le sniper","le psycho" ,"le dragon" ,"la boule de feu","la comète" ,"le zombie","la horde de zombie","le sorcier electrique","le cloneur"]
celi=[0          ,0           ,2          ,3          ,4          ,5            ,8           ,2          ,3          ,3           ,4               ,4          ,5          ,5           ,6           ,4                ,6           ,3          ,5                   ,4                      ,4]
cvie=[2500       ,5000        ,200        ,180        ,350        ,400          ,3000        ,50         ,150        ,40          ,400             ,4000       ,50         ,80          ,1200        ,0                ,0           ,150        ,170                 ,350                    ,200]
catt=[20         ,50          ,15         ,10         ,50         ,100          ,500         ,50         ,100        ,10          ,100             ,1          ,1000       ,1           ,250         ,250              ,1000        ,40         ,60                  ,50                     ,10]
cvat=[1          ,1           ,0.5        ,0.8        ,2          ,1.5          ,3           ,0.2        ,1.5        ,0.1         ,1.5             ,0.1        ,3          ,2           ,1.5         ,0                ,0           ,1.3        ,1.2                 ,1                      ,2.5]
ctpa=[1          ,1           ,1          ,1          ,1          ,2            ,2           ,1          ,1          ,1           ,2               ,2          ,1          ,1           ,2           ,2                ,2           ,1          ,1                   ,2                      ,2]
cpta=[0          ,0           ,0          ,0          ,1          ,0            ,0           ,0          ,1          ,0           ,0               ,0          ,0          ,0           ,1           ,0                ,0           ,2          ,2                   ,0                      ,0]
cvit=[0          ,0           ,3          ,3          ,3          ,2            ,2           ,4          ,3          ,3           ,0               ,1.1        ,1.1        ,1.5         ,1.3         ,0                ,0           ,1.2        ,1.2                 ,1.8                    ,1.3]
cpor=[150        ,110         ,50         ,150        ,140        ,40           ,55          ,50         ,250        ,50          ,100             ,50         ,250        ,80          ,150         ,80               ,80          ,60         ,60                  ,125                    ,100]
ctpc=[2          ,2           ,1          ,1          ,1          ,1            ,1           ,1          ,1          ,1           ,2               ,1          ,1          ,1           ,1           ,3                ,3           ,1          ,1                   ,1                      ,1]
crar=[0          ,0           ,0          ,0          ,1          ,1            ,2           ,3          ,3          ,0           ,1               ,1          ,1          ,3           ,4           ,1                ,2           ,0          ,0                   ,2                      ,4]
cnbp=[1          ,1           ,1          ,2          ,1          ,1            ,1           ,1          ,1          ,8           ,1               ,1          ,1          ,1           ,1           ,1                ,1           ,1          ,5                   ,1                      ,1]
cend=[1          ,1           ,1          ,1          ,1          ,1            ,1           ,1          ,1          ,1           ,1               ,1          ,1          ,1           ,2           ,1                ,1           ,1          ,1                   ,1                      ,1]
caen=[[1,2]      ,[1,2]       ,[1]        ,[1,2]      ,[1,2]      ,[1]          ,[1]         ,[1]        ,[1,2]      ,[1]         ,[1]             ,[1]        ,[1,2]      ,[1,2]       ,[1,2]       ,[1,2]            ,[1,2]       ,[1]        ,[1]                 ,[1,2]                  ,[1,2]]
cims=[0          ,2           ,None       ,0          ,1          ,None         ,None        ,None       ,0          ,None       ,2                ,None       ,2          ,None        ,1           ,None             ,None        ,None       ,None                ,3                      ,None]                                                                                          
cimg=["te1.png"  ,"te2.png"   ,"c0.png"   ,"c1.png"   ,"c2.png"   ,"c6.png"     ,"c3.png"    ,"c4.png"   ,"c5.png"   ,"c7.png"    ,"c8.png"        ,"c9.png"   ,"c10.png"  ,"c11.png"   ,"c12.png"   ,"c13.png"        ,"c14.png"   ,"c15.png"  ,"c15.png"           ,"c16.png"              ,"c17.png"] 
ctxx=[75/1200*tex,100/1200*tex,50/1200*tex,50/1200*tex,50/1200*tex,50/1200*tex  ,100/1200*tex,50/1200*tex,50/1200*tex,30/1200*tex ,50/1200*tex     ,75/1200*tex,50/1200*tex,50/1200*tex ,100/1200*tex,100/1200*tex     ,100/1200*tex,50/1200*tex,50/1200*tex         ,50/1200*tex            ,50/1200*tex]
ctyy=[75/1000*tey,100/1000*tey,50/1000*tey,50/1000*tey,50/1000*tey,50/1000*tey  ,100/1000*tey,50/1000*tey,50/1000*tey,30/1000*tey ,50/1000*tey     ,75/1000*tey,50/1000*tey,50/1000*tey ,100/1000*tey,100/1000*tey     ,100/1000*tey,50/1000*tey,50/1000*tey         ,50/1000*tey            ,50/1000*tey]
                                                                                                                                                                                                                                                                                                                                            
nctxx,nctyy=[],[]
for c in ctxx: nctxx.append(int(c))
for c in ctyy: nctyy.append(int(c))

cftpp=[0                ,1                  ,2                    ,3                        ,4                  ,5                ]
cfnom=["coffre de bois" ,"coffre en  bronze","coffre en argent"   ,"coffre en or"           ,"coffre légendaire","coffre divin"   ]
cfcrt=[[[0,5],[1,1]]    ,[[0,10],[1,5]]     ,[[0,15],[1,10],[2,5]],[[0,5],[1,5],[2,5],[3,1]],[[3,5]]            ,[[4,2]]            ]
cfore=[[0,1000]         ,[500,3500]         ,[1000,5000]          ,[3500,7500]              ,[5000,10000]       ,[5000,10000]     ]
cfimg=["cf1.png"        ,"cf2.png"          ,"cf3.png"            ,"cf4.png"                ,"cf5.png"          ,"cf6.png"        ]
cftxx=[int(200/1200*tex),int(200/1200*tex)  ,int(200/1200*tex)    ,int(200/1200*tex)        ,int(200/1200*tex)  ,int(200/1200*tex)]
cftyy=[int(200/1000*tey),int(200/1000*tey)  ,int(200/1000*tey)    ,int(200/1000*tey)        ,int(200/1000*tey)  ,int(200/1000*tey)]
ctxx,ctyy=nctxx,nctyy

mtpp=[0        ,1             ,2        ,3                      ]
mnom=["fleche" ,"boule de feu","boulet" ,"boule electrique"     ]
mimg=["ms1.png","ms2.png"     ,"ms3.png","ms4.png"              ]
mvit=[35       ,40            ,45       ,40                     ]
mtxx=[30       ,25            ,10       ,20                     ]
mtyy=[30       ,25            ,10       ,20                     ]
