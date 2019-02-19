#coding:utf-8
from lib2 import *

tex,tey=1000,800
aa=1200/tex
ctpp=[0          ,1           ,2           ,3          ,4          ,5            ,6           ,7          ,8          ,9           ,10              ,11         ,12         ,13          ,14          ,15               ,16          ,17         ,18                  ,19                     ,20          ,21           ,22              ,23         ,24                     ,25            ,26          ,27          ,28           ,29            ,30           ,31         ,32             ,33                 ,34           ,35         ,36               ,37                    ,38          ,39         ,40         ,41           ,42                 ,43                  ,44          ,45         ,46           ,47                  ,48             ,49         ,50          ,51         ,52         ,53         ,54          ,55              ]
cnom=["tour1"    ,"tour2"     ,"chevalier" ,"archer"   ,"mage"     ,"petit golem","golem"     ,"fantome"  ,"princesse","squelettes","tour a canons" ,"le géant" ,"le sniper","le psycho" ,"le dragon" ,"la boule de feu","la comète" ,"le zombie","la horde de zombie","le sorcier electrique","le cloneur","le geleur"  ,"le massdarmeur","l'oiseau" ,"la tour de electrique","la catapulte","la mouche" ,"le vampire","le soigneur","le bricoleur","les fleches","la foudre","le cimetière","l'arbre a oiseaux","le squelette","le gel"   ,"le nécromancien","le créateur d'élixir","l'assassin","Le poison","la reine" ,"le kamikaze","les esprits d'eau","les esprits de feu","le clonage","le piege" ,"l'emmerdeur","le fut à chevalier","le champignon","Larbre"   ,"Le buisson","La bombe" ,"La rage"  ,"Le soin"  ,"l'ange"    ,"les diablotins"  ]
celi=[0          ,0           ,3           ,3          ,4          ,4            ,8           ,2          ,3          ,3           ,3               ,4          ,5          ,5           ,6           ,4                ,7           ,1          ,5                   ,4                      ,4           ,5            ,5               ,1          ,5                      ,4             ,2           ,4            ,5            ,5             ,3            ,5          ,3              ,3                  ,1            ,4          ,5                ,4                     ,4           ,4          ,5          ,5            ,2                  ,3                   ,4           ,4          ,7            ,5                   ,5              ,6          ,1           ,5          ,6          ,5          ,4          ,3               ]
cvie=[2500       ,5000        ,250         ,180        ,500        ,450          ,3000        ,99         ,150        ,50          ,900             ,3700       ,61         ,90          ,1200        ,0                ,0           ,250        ,200                 ,340                    ,200         ,250          ,750             ,125        ,1050                   ,1150          ,60          ,350          ,250          ,145           ,0            ,0          ,1850           ,1850               ,60           ,0          ,455              ,500                   ,356         ,0          ,400        ,90           ,150                ,150                 ,15          ,100        ,270          ,0                   ,1000           ,1250       ,50          ,500        ,0          ,15         ,435        ,335             ]
ctap=[2          ,2           ,1           ,2          ,2          ,1            ,1           ,1          ,2          ,1           ,2               ,1          ,2          ,2           ,2           ,3                ,3           ,1          ,1                   ,2                      ,2           ,2            ,1               ,1          ,2                      ,2             ,1           ,1            ,2            ,2             ,3            ,3          ,4              ,4                  ,1            ,3          ,2                ,4                     ,1           ,3          ,2          ,1            ,2                  ,2                   ,3           ,3          ,2            ,3                   ,2              ,1          ,1           ,2          ,3          ,3          ,1          ,1               ]
catt=[50         ,80          ,55          ,30         ,170        ,200          ,500         ,70         ,150        ,20          ,200             ,2          ,700        ,1           ,250         ,250              ,950         ,60         ,60                  ,65                     ,10          ,100          ,420             ,20         ,10                     ,110           ,20          ,30           ,35           ,5             ,150          ,650        ,0              ,0                  ,20           ,50         ,536              ,1                     ,55          ,55         ,180        ,1020         ,20                 ,200                 ,1           ,525        ,2            ,10                  ,1              ,350        ,35          ,1500       ,25         ,10         ,52         ,55              ]
cvat=[1          ,1           ,0.4         ,0.8        ,2          ,1.5          ,3           ,0.2        ,1.5        ,0.3         ,1.5             ,0.1        ,4          ,2           ,1.5         ,5                ,5           ,1.3        ,1.2                 ,1.8                    ,2.5         ,5            ,2               ,0.3        ,0.1                    ,1.9           ,1.5         ,0.8          ,1            ,0.5           ,1            ,1          ,5              ,5                  ,0.1          ,1          ,6                ,5                     ,1           ,1          ,1.8        ,100          ,0                  ,0                   ,1           ,1          ,0.5          ,1                   ,0.1            ,3.5        ,1           ,300        ,1          ,1          ,0.9        ,0.5             ]
ctpa=[1          ,1           ,1           ,1          ,2          ,2            ,2           ,1          ,1          ,1           ,2               ,2          ,1          ,1           ,2           ,2                ,2           ,1          ,1                   ,2                      ,2           ,1            ,2               ,1          ,1                      ,1             ,1           ,1            ,2            ,1             ,2            ,2          ,2              ,2                  ,1            ,2          ,2                ,2                     ,1           ,2          ,2          ,1            ,1                  ,1                   ,2           ,2          ,1            ,2                   ,2              ,1          ,2           ,2          ,2          ,2          ,1          ,1               ]
cpta=[0          ,0           ,0           ,0          ,1          ,0            ,0           ,0          ,1          ,0           ,0               ,0          ,0          ,0           ,1           ,0                ,0           ,2          ,2                   ,0                      ,0           ,3            ,0               ,0          ,0                      ,0             ,4           ,5            ,6            ,7             ,0            ,0          ,0              ,0                  ,0            ,9          ,0                ,0                     ,8           ,8          ,0          ,9            ,9                  ,9                   ,0           ,10         ,11           ,0                   ,8              ,12         ,0           ,0          ,11         ,0          ,0          ,0               ]
cvit=[0          ,0           ,2.7         ,1.7        ,2          ,1.5          ,2           ,4          ,3          ,2           ,0               ,1.1        ,1.1        ,1.5         ,1.3         ,0                ,0           ,1.2        ,1.2                 ,1.8                    ,1.3         ,1.5          ,1.12            ,2.5        ,0                      ,0             ,2.3         ,1.7          ,1.5          ,1.4           ,0            ,0          ,0              ,0                  ,3            ,0          ,1.4              ,0                     ,3.9         ,0          ,1.8        ,3.5          ,2.8                ,3.4                 ,0           ,0          ,2.3          ,0                   ,0              ,1.3        ,2           ,0          ,0          ,0          ,3          ,3.3             ]
cpor=[(140)      ,(150)       ,int(50*aa+1),150        ,140        ,40           ,55          ,50         ,250        ,50          ,100             ,50         ,215        ,80          ,150         ,80               ,80          ,60         ,60                  ,125                    ,100         ,125          ,60              ,60         ,170                    ,225           ,40          ,60           ,125          ,55            ,150          ,50         ,100            ,100                ,50           ,50         ,125              ,1                     ,55          ,50         ,215        ,40           ,125                ,125                 ,30          ,50         ,85           ,50                  ,125            ,70         ,60          ,125        ,75         ,30         ,226        ,100             ]
ctpc=[2          ,2           ,1           ,1          ,1          ,1            ,1           ,1          ,1          ,1           ,2               ,1          ,1          ,1           ,1           ,3                ,3           ,1          ,1                   ,1                      ,1           ,1            ,1               ,1          ,2                      ,2             ,1           ,1            ,1            ,1             ,3            ,3          ,2              ,2                  ,1            ,3          ,1                ,2                     ,1           ,3          ,1          ,1            ,1                  ,1                   ,4           ,4          ,1            ,3                   ,2              ,1          ,1           ,2          ,3          ,4          ,1          ,1               ]
crar=[0          ,0           ,0           ,0          ,2          ,1            ,2           ,3          ,3          ,0           ,1               ,1          ,1          ,3           ,4           ,1                ,2           ,0          ,0                   ,2                      ,4           ,2            ,1               ,0          ,0                      ,0             ,0           ,2            ,3            ,3             ,0            ,0          ,1              ,1                  ,0            ,2          ,3                ,1                     ,2           ,2          ,4          ,2            ,0                  ,0                   ,2           ,1          ,1            ,2                   ,1              ,0          ,0           ,2          ,2          ,2          ,0          ,1               ]
cnbp=[1          ,1           ,1           ,2          ,1          ,1            ,1           ,1          ,1          ,8           ,1               ,1          ,1          ,1           ,1           ,1                ,1           ,1          ,5                   ,1                      ,1           ,1            ,1               ,1          ,1                      ,1             ,3           ,1            ,1            ,1             ,1            ,1          ,1              ,1                  ,1            ,1          ,1                ,1                     ,1           ,1          ,1          ,1            ,3                  ,3                   ,1           ,1          ,1            ,1                   ,1              ,1          ,2           ,1          ,1          ,1          ,1          ,2               ]
cend=[1          ,1           ,1           ,1          ,1          ,1            ,1           ,1          ,1          ,1           ,1               ,1          ,1          ,1           ,2           ,1                ,1           ,1          ,1                   ,1                      ,1           ,1            ,1               ,2          ,1                      ,1             ,2           ,1            ,1            ,1             ,1            ,1          ,1              ,1                  ,1            ,1          ,1                ,1                     ,1           ,1          ,1          ,1            ,1                  ,1                   ,3           ,3          ,1            ,1                   ,1              ,1          ,1           ,1          ,1          ,3          ,2          ,1               ]
caen=[[1,2]      ,[1,2]       ,[1]         ,[1,2]      ,[1,2]      ,[1]          ,[1]         ,[1]        ,[1,2]      ,[1]         ,[1]             ,[1]        ,[1,2]      ,[1,2]       ,[1,2]       ,[1,2]            ,[1,2]       ,[1]        ,[1]                 ,[1,2]                  ,[1,2]       ,[1,2]        ,[1]             ,[1,2]      ,[1,2]                  ,[1]           ,[1,2]       ,[1]          ,[1,2]        ,[1]           ,[1,2]        ,[1]        ,[1]            ,[1]                ,[1]          ,[1,2]      ,[1,2]            ,[1]                   ,[1]         ,[1,2]      ,[1,2]      ,[1,2]        ,[1,2]              ,[1,2]               ,[1,2]       ,[1]        ,[1]          ,[1,2]               ,[1,2]          ,[1]        ,[1]         ,[1,2]      ,[1,2]      ,[1,2]      ,[1,2]      ,[1]             ]
cims=[0          ,2           ,None        ,0          ,1          ,None         ,None        ,None       ,0          ,None        ,2               ,None       ,2          ,None        ,1           ,None             ,None        ,None       ,None                ,3                      ,None        ,4            ,None            ,None       ,3                      ,2             ,None        ,None         ,5            ,None          ,None         ,None       ,None           ,None               ,None         ,None       ,6                ,None                  ,None        ,None       ,0          ,None         ,7                  ,8                   ,None        ,None       ,None         ,None                ,6              ,None       ,None        ,None       ,None       ,None       ,9          ,None            ]
cimg=["tour1_1.png","te2.png" ,"c0.png"    ,"c1.png"   ,"c2.png"   ,"c6.png"     ,"c3.png"    ,"c4.png"   ,"c5.png"   ,"c7.png"    ,"c8.png"        ,"c9.png"   ,"c10.png"  ,"c11.png"   ,"c12.png"   ,"c13.png"        ,"c14.png"   ,"c15.png"  ,"c15.png"           ,"c16.png"              ,"c17.png"   ,"c18.png"    ,"c19.png"       ,"c20.png"  ,"c21.png"              ,"c22.png"     ,"c24.png"   ,"c23.png"    ,"c25.png"    ,"c26.png"     ,"c27.png"    ,"c35.png"  ,"c29.png"      ,"c30.png"          ,"c7.png"     ,"c31.png"  ,"c32.png"        ,"c33.png"             ,"c34.png"   ,"c36.png"  ,"c37.png"  ,"c38.png"    ,"c39.png"          ,"c40.png"           ,"c41.png"   ,"c42.png"  ,"c43.png"    ,"c44.png"           ,"c45.png"      ,"c46.png"  ,"c47.png"   ,"c48.png"  ,"c49.png"  ,"c50.png"  ,"c51.png"  ,"c52.png"       ]
care=[0          ,0           ,0           ,0          ,0          ,1            ,2           ,2          ,0          ,2           ,0               ,0          ,10         ,10          ,3           ,3                ,3           ,2          ,2                   ,4                      ,10          ,5            ,8               ,1          ,4                      ,2             ,2           ,2            ,9            ,10            ,0            ,4          ,2              ,6                  ,2            ,5          ,2                ,10                    ,6           ,6          ,0          ,1            ,7                  ,3                   ,10          ,10         ,3            ,1                   ,6              ,6          ,6           ,10         ,3          ,9          ,9          ,3               ]
ctxx=[rx(75)     ,rx(100)     ,rx(50)      ,rx(50)     ,rx(50)     ,rx(50)       ,rx(100)     ,rx(50)     ,rx(50)     ,rx(30)      ,rx(50)          ,rx(75)     ,rx(50)     ,rx(50)      ,rx(100)     ,rx(100)          ,rx(100)     ,rx(50)     ,rx(50)              ,rx(50)                 ,rx(50)      ,rx(50)       ,rx(60)          ,rx(40)     ,rx(60)                 ,rx(60)        ,rx(20)      ,rx(50)       ,rx(50)       ,rx(50)        ,rx(100)      ,rx(90)     ,rx(55)         ,rx(60)             ,rx(30)       ,rx(50)     ,rx(50)           ,rx(50)                ,rx(50)      ,rx(50)     ,rx(55)     ,rx(48)       ,rx(26)             ,rx(26)              ,rx(80)      ,rx(50)     ,rx(50)       ,rx(50)              ,rx(50)         ,rx(65)     ,rx(45)      ,rx(50)     ,rx(50)     ,rx(80)     ,rx(50)     ,rx(50)          ]
ctyy=[ry(75)     ,ry(100)     ,ry(50)      ,ry(50)     ,ry(50)     ,ry(50)       ,ry(100)     ,ry(50)     ,ry(50)     ,ry(30)      ,ry(50)          ,ry(75)     ,ry(50)     ,ry(50)      ,ry(100)     ,ry(100)          ,ry(100)     ,ry(50)     ,ry(50)              ,ry(50)                 ,ry(50)      ,ry(50)       ,ry(60)          ,ry(40)     ,ry(60)                 ,ry(60)        ,ry(20)      ,ry(50)       ,ry(50)       ,ry(50)        ,ry(100)      ,ry(90)     ,ry(55)         ,ry(60)             ,ry(30)       ,ry(50)     ,ry(50)           ,ry(50)                ,ry(50)      ,ry(50)     ,ry(55)     ,ry(48)       ,ry(26)             ,ry(26)              ,ry(80)      ,ry(50)     ,ry(50)       ,ry(50)              ,ry(50)         ,ry(65)     ,ry(45)      ,ry(50)     ,ry(50)     ,ry(80)     ,ry(50)     ,ry(50)          ]
cact=[None       ,None        ,None        ,None       ,None       ,None         ,None        ,None       ,None       ,None        ,None            ,None       ,None       ,None        ,None        ,None             ,None        ,None       ,None                ,None                   ,None        ,None         ,None            ,None       ,None                   ,None          ,None        ,None         ,None         ,None          ,None         ,None       ,34             ,23                 ,None         ,None       ,17               ,None                  ,None        ,None       ,None       ,None         ,None               ,None                ,None        ,None       ,None         ,None                ,None           ,None       ,None        ,None       ,None       ,None       ,None       ,None            ]
cccd=[None       ,None        ,None        ,None       ,None       ,None         ,None        ,None       ,None       ,None        ,None            ,None       ,None       ,None        ,None        ,None             ,None        ,None       ,None                ,None                   ,None        ,None         ,None            ,None       ,None                   ,None          ,None        ,None         ,None         ,None          ,None         ,None       ,None           ,None               ,None         ,None       ,None             ,None                  ,None        ,None       ,None       ,None         ,None               ,None                ,None        ,None       ,None         ,[3,2]               ,None           ,[3,50]     ,None        ,[1,41]     ,None       ,[1,28]     ,None       ,None            ]
cdes=["C'est une petite tour qui a pour but de proteger la tour du roi",
      "C'est la tour du roi, la tour la plus importante de la partie",
      "Le chevalier attaque de près ces ennemis avec son épée",
      "L'archer est le maître de son arc, personne ne peut l'égaler ni le surpasser dans son domaine",
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
      "Il répare les batiments endomagés",
      "Une pluie de fleche tirée par des archers divins",
      "Des éclairs très puissants et très préssés d'electrocuter des ennemis",
      "De cette tombe, des squelettes apparaissent infiniment",
      "De cet arbre, des oiseaux naissent et s'envolent",
      "Le squelette est un combatant faible, mais il peut quand meme etre utile",
      "Gros bloc de glace venant du ciel et qui gèle instantanément tout les ennemis le touchant",
      "Le nécromancien aime les zombies, d'ailleurs, il en invoque à chaque attaque",
      "Rien de mieux qu'un batiment qui crée de l'exilir toutes les 5 secondes",
      "L'assassin empoisonne ses ennemis avec ses dagues",
      "Le poison est un sort empoisonnant tous les ennemis le touchant",
      "La reine est la mère de la princesse, c'est à dire qu'elle fait tout pareil que la princesse, mais en mieux",
      "Le kamikaze explose quand il meurt, il est aussi efficace que taré",
      "Les esprits de l'eau fait reculer sa cible avec la force de l'eau",
      "Les esprits du feu se jettent sur leurs cibles pour leur infliger des dégats",
      "Il crée un clone de toutes les cartes du même camp qui le touchent",
      "Il s'active quanq un ennemi lui marche dessus, il fait très mal",
      "Il a le talent d'énerver toutes les troupes dans le même camp que lui",
      "Quand il tombe par terre, des chevaliers en sortent",
      "Tout ceux qui l'approchent sont empoisonnés",
      "Il aime assomer ses ennemis",
      "Ce sont des buissons tout mignons",
      "Quand elle est détruite, elle explose et un kamikaze en sort",
      "Le sort de rage énerve toutes les cartes qui le touchent",
      "Le soin soigne",
      "Il est venu du ciel pour purifier la Terre",
      "Le diablotin a une très forte envie de sang"]
                                                                                                                                                                                                                                                                                                                                            
nctxx,nctyy=[],[]
for c in ctxx: nctxx.append(int(c))
for c in ctyy: nctyy.append(int(c))
ctxx=nctxx
ctyy=nctyy

ncpor=[]
for c in cpor: ncpor.append(rz(c))
cpor=ncpor

cftpp=[0                ,1                  ,2                    ,3                        ,4                  ,5                ,6                ]
cfnom=["coffre de bois" ,"coffre en  bronze","coffre en argent"   ,"coffre en or"           ,"coffre légendaire","coffre divin"   ,"coffre gratuit" ]
cfcrt=[[[0,5],[1,1]]    ,[[0,10],[1,5]]     ,[[0,15],[1,10],[2,5]],[[0,5],[1,5],[2,5],[3,1]],[[3,5]]            ,[[4,2]]          ,[[0,1],[1,0]]    ]
cfore=[[0,50]           ,[50,150]           ,[100,300]            ,[250,400]                ,[250,500]          ,[500,750]        ,[1,2]            ]
cfimg=["cf1.png"        ,"cf2.png"          ,"cf3.png"            ,"cf4.png"                ,"cf5.png"          ,"cf6.png"        ,"cf7.png"        ]
cftxx=[rx(200)          ,rx(200)            ,rx(200)              ,rx(200)                  ,rx(200)            ,rx(200)          ,rx(200)          ]
cftyy=[ry(200)          ,ry(200)            ,ry(200)              ,ry(200)                  ,ry(200)            ,ry(200)          ,ry(200)          ]
cfarg=[100              ,250                ,750                  ,1500                     ,5000               ,10000            ,0                ]
ctxx,ctyy=nctxx,nctyy

mtpp=[0        ,1             ,2        ,3                 ,4              ,5              ,6            ,7        ,8        ,9             ]
mnom=["fleche" ,"boule de feu","boulet" ,"boule electrique","bloc ce glace","bloc de magie","magie noire","mis eau","mis feu","mis divin"   ]
mimg=["ms1.png","ms2.png"     ,"ms3.png","ms4.png"         ,"ms5.png"      ,"ms6.png"      ,"ms7.png"    ,"ms8.png","ms9.png","ms10.png"    ]
mvit=[35       ,40            ,45       ,40                ,20             ,30             ,33           ,25       ,24       ,35            ]
mtxx=[30       ,25            ,10       ,20                ,20             ,20             ,25           ,25       ,25       ,25            ]
mtyy=[30       ,25            ,10       ,20                ,20             ,20             ,25           ,25       ,25       ,25            ]


atpp=[0                      ,1                        ,2              ,3                 ,4                 ,5                  ,6                  ,7               ,8              ,9                 ,10                        ]
anom=["arene du commencement","arene de la tranquilité","arene osseuse","arene de l'enfer","arene electrique","arene de la neige","arene de la foret","arene de l'eau","arene anciene","arène du paradis","arene de la technologie"]
atro=[0                      ,100                      ,400            ,800               ,1200              ,1500               ,2000               ,2500            ,3500           ,4000              ,4500                     ]
aimg=[10                     ,1                        ,2              ,3                 ,4                 ,5                  ,6                  ,7               ,8              ,11                ,9                        ]



