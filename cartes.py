#coding:utf-8
tex,tey=1000,800
ctpp=[0          ,1           ,2          ,3          ,4          ,5            ,6           ,7          ,8          ,9           ,10              ,11         ,12         ,13          ,14          ,15               ,16          ,17         ,18                  ,19                     ,20          ,21           ,22              ,23         ,24                     ,25            ,26          ,27          ,28           ,29            ,30           ,31         ,32             ,33                 ,34           ,35         ,36               ,37                    ,38             ]
cnom=["tour1"    ,"tour2"     ,"chevalier","archer"   ,"mage"     ,"petit golem","golem"     ,"fantome"  ,"princesse","squelettes","tour a canons" ,"le géant" ,"le sniper","le psycho" ,"le dragon" ,"la boule de feu","la comète" ,"le zombie","la horde de zombie","le sorcier electrique","le cloneur","le geleur"  ,"le massdarmeur","l'oiseau" ,"la tour de electrique","la catapulte","la mouche" ,"le vampire","le soigneur","le bricoleur","les fleches","la foudre","le cimetière","l'arbre a oiseaux","le squelette","le gel"   ,"le nécromancien","le créateur d'élixir","l'assassin"   ]
celi=[0          ,0           ,2          ,3          ,4          ,5            ,8           ,2          ,3          ,3           ,3               ,4          ,5          ,5           ,6           ,4                ,7           ,1          ,5                   ,4                      ,4           ,5            ,5               ,1          ,5                     ,4             ,2           ,4            ,5            ,5             ,3            ,5          ,3              ,3                  ,1            ,4          ,5                ,4                     ,4              ]
cvie=[2500       ,5000        ,200        ,180        ,350        ,400          ,3000        ,50         ,150        ,40          ,700             ,4000       ,50         ,80          ,1200        ,0                ,0           ,150        ,170                 ,350                    ,200         ,250          ,650             ,125        ,750                   ,850           ,70          ,350          ,270          ,345           ,0            ,0          ,1450           ,1050               ,40           ,0          ,455              ,500                   ,356            ]
catt=[20         ,50          ,15         ,10         ,50         ,100          ,500         ,50         ,100        ,10          ,100             ,1          ,750        ,1           ,250         ,250              ,800         ,40         ,60                  ,75                     ,10          ,100          ,320             ,10         ,1                     ,100           ,20          ,25           ,15           ,10            ,150          ,550        ,0              ,0                  ,10           ,50         ,536              ,1                     ,55             ]
cvat=[1          ,1           ,0.5        ,0.8        ,2          ,1.5          ,3           ,0.2        ,1.5        ,0.1         ,1.5             ,0.1        ,3          ,2           ,1.5         ,5                ,5           ,1.3        ,1.2                 ,1.8                    ,2.5         ,5            ,2               ,0.3        ,0                     ,1.9           ,1.5         ,0.8          ,1            ,1             ,1            ,1          ,6              ,6                  ,0.1          ,1          ,6                ,5                     ,1              ]
ctpa=[1          ,1           ,1          ,1          ,2          ,2            ,2           ,1          ,1          ,1           ,2               ,2          ,1          ,1           ,2           ,2                ,2           ,1          ,1                   ,2                      ,2           ,1            ,2               ,1          ,1                     ,1             ,1           ,1            ,2            ,1             ,2            ,2          ,2              ,2                  ,1            ,2          ,2                ,2                     ,1              ]
cpta=[0          ,0           ,0          ,0          ,1          ,0            ,0           ,0          ,1          ,0           ,0               ,0          ,0          ,0           ,1           ,0                ,0           ,2          ,2                   ,0                      ,0           ,3            ,0               ,0          ,0                     ,0             ,4           ,5            ,6            ,7             ,0            ,0          ,0              ,0                  ,0            ,0          ,0                ,0                     ,8              ]
cvit=[0          ,0           ,3          ,3          ,3          ,2            ,2           ,4          ,3          ,3           ,0               ,1.1        ,1.1        ,1.5         ,1.3         ,0                ,0           ,1.2        ,1.2                 ,1.8                    ,1.3         ,1.5          ,1.12            ,2.5        ,0                     ,0             ,2.3         ,1.7          ,1.5          ,1.4           ,0            ,0          ,0              ,0                  ,3            ,0          ,1.4              ,0                     ,1.9            ]
cpor=[150        ,150         ,50         ,150        ,140        ,40           ,55          ,50         ,250        ,50          ,100             ,50         ,250        ,80          ,150         ,80               ,80          ,60         ,60                  ,125                    ,100         ,125          ,60              ,60         ,170                   ,225           ,40          ,60           ,125          ,125           ,100          ,50         ,100            ,100                ,50           ,50         ,125              ,1                     ,55             ]
ctpc=[2          ,2           ,1          ,1          ,1          ,1            ,1           ,1          ,1          ,1           ,2               ,1          ,1          ,1           ,1           ,3                ,3           ,1          ,1                   ,1                      ,1           ,1            ,1               ,1          ,2                     ,2             ,1           ,1            ,1            ,1             ,3            ,3          ,2              ,2                  ,1            ,3          ,1                ,2                     ,1              ]
crar=[0          ,0           ,0          ,0          ,1          ,1            ,2           ,3          ,3          ,0           ,1               ,1          ,1          ,3           ,4           ,1                ,2           ,0          ,0                   ,2                      ,4           ,2            ,1               ,0          ,0                     ,0             ,0           ,2            ,3            ,3             ,0            ,0          ,1              ,1                  ,0            ,2          ,3                ,1                     ,2              ]
cnbp=[1          ,1           ,1          ,2          ,1          ,1            ,1           ,1          ,1          ,8           ,1               ,1          ,1          ,1           ,1           ,1                ,1           ,1          ,5                   ,1                      ,1           ,1            ,1               ,1          ,1                     ,1             ,3           ,1            ,1            ,1             ,1            ,1          ,1              ,1                  ,1            ,1          ,1                ,1                     ,1              ]
cend=[1          ,1           ,1          ,1          ,1          ,1            ,1           ,1          ,1          ,1           ,1               ,1          ,1          ,1           ,2           ,1                ,1           ,1          ,1                   ,1                      ,1           ,1            ,1               ,2          ,1                     ,1             ,2           ,1            ,1            ,1             ,1            ,1          ,1              ,1                  ,1            ,1          ,1                ,1                     ,1              ]
caen=[[1,2]      ,[1,2]       ,[1]        ,[1,2]      ,[1,2]      ,[1]          ,[1]         ,[1]        ,[1,2]      ,[1]         ,[1]             ,[1]        ,[1,2]      ,[1,2]       ,[1,2]       ,[1,2]            ,[1,2]       ,[1]        ,[1]                 ,[1,2]                  ,[1,2]       ,[1,2]        ,[1]             ,[1,2]      ,[1,2]                 ,[1]           ,[1,2]       ,[1]          ,[1,2]        ,[1]           ,[1,2]        ,[1]        ,[1]            ,[1]                ,[1]          ,[1,2]      ,[1,2]            ,[1]                   ,[1]            ]
cims=[0          ,2           ,None       ,0          ,1          ,None         ,None        ,None       ,0          ,None        ,2               ,None       ,2          ,None        ,1           ,None             ,None        ,None       ,None                ,3                      ,None        ,4            ,None            ,None       ,3                     ,2             ,None        ,None         ,5            ,None          ,None         ,None       ,None           ,None               ,None         ,None       ,6                ,None                  ,None           ]
cimg=["tour1_1.png","te2.png" ,"c0.png"   ,"c1.png"   ,"c2.png"   ,"c6.png"     ,"c3.png"    ,"c4.png"   ,"c5.png"   ,"c7.png"    ,"c8.png"        ,"c9.png"   ,"c10.png"  ,"c11.png"   ,"c12.png"   ,"c13.png"        ,"c14.png"   ,"c15.png"  ,"c15.png"           ,"c16.png"              ,"c17.png"   ,"c18.png"    ,"c19.png"       ,"c20.png"  ,"c21.png"             ,"c22.png"     ,"c24.png"   ,"c23.png"    ,"c25.png"    ,"c26.png"     ,"c27.png"    ,"c28.png"  ,"c29.png"      ,"c30.png"          ,"c7.png"     ,"c31.png"  ,"c32.png"        ,"c33.png"             ,"c34.png"      ]
care=[0          ,0           ,0          ,0          ,0          ,0            ,0           ,1          ,0          ,1           ,0               ,0          ,0          ,0           ,0           ,0                ,0           ,1          ,1                   ,3                      ,0           ,0            ,2               ,0          ,3                     ,0             ,1           ,0            ,0            ,0             ,0            ,0          ,0              ,0                  ,0            ,0          ,0                ,0                     ,0              ]
ctxx=[75/1200*tex,100/1200*tex,50/1200*tex,50/1200*tex,50/1200*tex,50/1200*tex  ,100/1200*tex,50/1200*tex,50/1200*tex,30/1200*tex ,50/1200*tex     ,75/1200*tex,50/1200*tex,50/1200*tex ,100/1200*tex,100/1200*tex     ,100/1200*tex,50/1200*tex,50/1200*tex         ,50/1200*tex            ,50/1200*tex ,50/1200*tex  ,60/1200*tex     ,40/1200*tex,60/1200*tex           ,60/1200*tex   ,20/1200*tex ,50/1200*tex  ,50/1200*tex  ,50/1200*tex   ,100/1200*tex ,50/1200*tex,55/1200*tex    ,60/1200*tex        ,30/1200*tex  ,50/1200*tex,50/1200*tex      ,50/1200*tex           ,50/1200*tex    ]
ctyy=[75/1000*tey,100/1000*tey,50/1000*tey,50/1000*tey,50/1000*tey,50/1000*tey  ,100/1000*tey,50/1000*tey,50/1000*tey,30/1000*tey ,50/1000*tey     ,75/1000*tey,50/1000*tey,50/1000*tey ,100/1000*tey,100/1000*tey     ,100/1000*tey,50/1000*tey,50/1000*tey         ,50/1000*tey            ,50/1000*tey ,50/1000*tey  ,60/1000*tey     ,40/1000*tey,60/1000*tey           ,60/1000*tey   ,20/1000*tey ,50/1000*tey  ,50/1000*tey  ,50/1000*tey   ,100/1000*tey ,50/1000*tey,55/1000*tey    ,60/1000*tey        ,30/1000*tey  ,50/1000*tey,50/1000*tey      ,50/1000*tey           ,50/1000*tey    ]
cact=[None       ,None        ,None       ,None       ,None       ,None         ,None        ,None       ,None       ,None        ,None            ,None       ,None       ,None        ,None        ,None             ,None        ,None       ,None                ,None                   ,None        ,None         ,None            ,None       ,None                  ,None          ,None        ,None         ,None         ,None          ,None         ,None       ,34             ,23                 ,None         ,None       ,17               ,None                  ,None           ]
cdes=["C'est une petite tour qui a pour but de proteger la tour du roi",
      "C'est la tour du roi, la tour la plus importante de la partie",
      "Le chevalier est un attaquant basique, il a peu de vie et d'attaque",
      "L'archer est un attaquant a distant basique, quand vous posez cette carte, deux archers sont créés",
      "Le mage lance des boules de feu sur ces ennemis",
      "Le petit golem est un petite version du golem mais il a autant envie de détruire que le golem",
      "Le golem est titanesque, il détruit tout sur son passage",
      "Le fantome est rapide mais assez faible",
      "La princesse attaque de loin avec son arc",
      "les squelettes sont des petits attaquants assez faibles mais en groupe, ils deviennent plus fort",
      "La tour a canon est une tour qui attaque tout ce qui passe sous son nez",
      "Le géant est un attaquant qui a énormément de vie, mais qui a une très faible attaque, il sert a prendre a la place des autres les coups des ennemis",
      "Le sniper est très dangereux a distance, mais il ne sait pas ce battre de près",
      "Le psycho parvient à mettre un ennemi dans son camp, il a un bon mental, mais pas de qualité de combattant",
      "Le dragon est le maître des airs, il brule tout et il est très dangereux",
      "La boule de feu est un sort qui brule tout ce qu'elle touche",
      "La comète écrase tout ce qu'elle touche" ,
      "Le zombie est faible, mais après avoir tué quelqu'un, il le transforme en zombie",
      "La horde de zombie est encore plus dangereuse qu'un zombie seul",
      "Le sorcier électrique a peut-être été frappé par la foudre, il peut controler l'electricité et s'en servir pour attaquer ses adversaires",
      "Le cloneur est sans doute la technologie la plus avancée qui existe dans ce jeu, il arrive a cloner un ennemi, ce qui peux être très pratique",
      "Le geleur aime bien jouer avec la glace, il gèle tout ce qui est un peu trop chaud à son gout",
      "Le massdarmeur est un soldat lourd qui attaque avec une masse d'arme,il fait mal et a pas mal de vie",
      "loiseau est un petit oiseau qui vole dans le ciel",
      "la tour de foudre est un tour qui electrocute tout ce qui passa à côté d'elle",
      "la catapulte peut attaquer très loin",
      "la mouche fait apparaitre d'autres mouches à chaque attaque",
      "Il pique la vie des ses ennemis tout en buvant de leur sang",
      "Il aime soigner ses amis qui sont proches de lui",
      "Il répare les batiments endomagés et inflige plus de dégats aux batiments ennemis",
      "Une pluie de fleche tirée par des archers divins",
      "Des éclairs très puissants et très préssés d'electrocuter des ennemis",
      "De cette tombe, des squelettes apparaissent infiniment",
      "De cet arbre, des oiseaux naissent et s'envolent",
      "Le squelette est un combatant faible, mais il peut quand meme etre utile",
      "Gros bloc de glace venant du ciel et qui gèle instantanément tout les ennemis le touchant",
      "Le nécromancien aime les zombies, d'ailleurs, il en invoque à chaque attaque",
      "Rien de mieux qu'un batiment qui crée de l'exilir toutes les 5 secondes",
      "L'assassin empoisonne ses ennemis avec ses dagues"]
                                                                                                                                                                                                                                                                                                                                            
nctxx,nctyy=[],[]
for c in ctxx: nctxx.append(int(c))
for c in ctyy: nctyy.append(int(c))
ctxx=nctxx
ctyy=nctyy

cftpp=[0                ,1                  ,2                    ,3                        ,4                  ,5                ]
cfnom=["coffre de bois" ,"coffre en  bronze","coffre en argent"   ,"coffre en or"           ,"coffre légendaire","coffre divin"   ]
cfcrt=[[[0,5],[1,1]]    ,[[0,10],[1,5]]     ,[[0,15],[1,10],[2,5]],[[0,5],[1,5],[2,5],[3,1]],[[3,5]]            ,[[4,2]]          ]
cfore=[[0,50]           ,[50,150]           ,[100,500]            ,[350,750]                ,[500,1000]         ,[500,1000]       ]
cfimg=["cf1.png"        ,"cf2.png"          ,"cf3.png"            ,"cf4.png"                ,"cf5.png"          ,"cf6.png"        ]
cftxx=[int(200/1200*tex),int(200/1200*tex)  ,int(200/1200*tex)    ,int(200/1200*tex)        ,int(200/1200*tex)  ,int(200/1200*tex)]
cftyy=[int(200/1000*tey),int(200/1000*tey)  ,int(200/1000*tey)    ,int(200/1000*tey)        ,int(200/1000*tey)  ,int(200/1000*tey)]
cfarg=[100              ,250                ,750                  ,1500                     ,10000              ,20000            ]
ctxx,ctyy=nctxx,nctyy

mtpp=[0        ,1             ,2        ,3                 ,4              ,5              ,6               ]
mnom=["fleche" ,"boule de feu","boulet" ,"boule electrique","bloc ce glace","bloc de magie","magie noire"   ]
mimg=["ms1.png","ms2.png"     ,"ms3.png","ms4.png"         ,"ms5.png"      ,"ms6.png"      ,"ms7.png"       ]
mvit=[35       ,40            ,45       ,40                ,20             ,30             ,33              ]
mtxx=[30       ,25            ,10       ,20                ,20             ,20             ,25              ]
mtyy=[30       ,25            ,10       ,20                ,20             ,20             ,25              ]


atpp=[0                        ,1                     ,2                 ,3                 ]
anom=["arene de la tranquilité","arene des squelettes","arene de l'enfer","arene electrique"]
atro=[0                        ,400                   ,800               ,1200              ]
aimg=[1                        ,2                     ,3                 ,4                 ]



