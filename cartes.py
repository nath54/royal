tex,tey=1000,800
ctpp=[0          ,1           ,2          ,3          ,4          ,5            ,6           ,7          ,8          ,9           ,10              ,11         ,12              ]
cnom=["tour1"    ,"tour2"     ,"chevalier","archer"   ,"mage"     ,"petit golem","golem"     ,"fantome"  ,"princesse","squelettes","tour a canons" ,"le géant" ,"le sniper"     ]
celi=[0          ,0           ,2          ,3          ,4          ,5            ,8           ,2          ,3          ,3           ,4               ,4          ,5               ]
cvie=[2500       ,5000        ,200        ,180        ,350        ,400          ,3000        ,50         ,150        ,40          ,400             ,4000       ,50              ]
catt=[20         ,50          ,15         ,10         ,50         ,100          ,500         ,50         ,100        ,10          ,100             ,1          ,1000            ]
cvat=[1          ,1           ,0.5        ,0.8        ,2          ,1.5          ,3           ,0.2        ,1.5        ,0.1         ,1.5             ,0.1        ,3               ]
ctpa=[1          ,1           ,1          ,1          ,1          ,2            ,2           ,1          ,1          ,1           ,2               ,2          ,1               ]
cvit=[0          ,0           ,3          ,3          ,3          ,2            ,2           ,4          ,3          ,3           ,0               ,1.1        ,1.1             ]
cpor=[150        ,200         ,50         ,150        ,200        ,40           ,55          ,50         ,350        ,50          ,125             ,50         ,350             ]
ctpc=[2          ,2           ,1          ,1          ,1          ,1            ,1           ,1          ,1          ,1           ,2               ,1          ,1               ]
crar=[0          ,0           ,0          ,0          ,1          ,1            ,2           ,3          ,3          ,0           ,1               ,1          ,1               ]
cnbp=[1          ,1           ,1          ,2          ,1          ,1            ,1           ,1          ,1          ,20          ,1               ,1          ,1               ]
cimg=["te1.png"  ,"te2.png"   ,"c0.png"   ,"c1.png"   ,"c2.png"   ,"c6.png"     ,"c3.png"    ,"c4.png"   ,"c5.png"   ,"c7.png"    ,"c8.png"        ,"c9.png"   ,"c10.png"       ]
ctxx=[75/1200*tex,100/1200*tex,50/1200*tex,50/1200*tex,50/1200*tex,50/1200*tex  ,100/1200*tex,50/1200*tex,50/1200*tex,30/1200*tex ,50/1200*tex     ,75/1200*tex,50/1200*tex     ]
ctyy=[75/1000*tey,100/1000*tey,50/1000*tey,50/1000*tey,50/1000*tey,50/1000*tey  ,100/1000*tey,50/1000*tey,50/1000*tey,30/1000*tey ,50/1000*tey     ,75/1000*tey,50/1000*tey     ]
nctxx,nctyy=[],[]
for c in ctxx: nctxx.append(int(c))
for c in ctyy: nctyy.append(int(c))
ctxx,ctyy=nctxx,nctyy
