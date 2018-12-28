#coding:utf-8
import pygame
from pygame.locals import *

def main(txtaff,tx,ty):
    txe,tye=tx,ty
    texte=txtaff
    ncour=True
    fenetre2=pygame.display.set_mode([txe,tye])
    pygame.display.set_caption("text box")
    ztx,zty=tye/2,ty/2
    ctxt=(200,200,250)
    font=pygame.font.SysFont("Serif",50)
    fimg=pygame.transform.scale(pygame.image.load("images/fontxt.png"),[txe,tye])
    def aff():
        fenetre2.blit(fimg,[0,0])
        fenetre2.blit(font.render(texte,20,ctxt),[ztx,zty])
        pygame.display.update()
    tchsa=[[K_a,"a"],
          [K_b,"b"],
          [K_c,"c"],
          [K_d,"d"],
          [K_e,"e"],
          [K_f,"f"],
          [K_g,"g"],
          [K_h,"h"],
          [K_i,"i"],
          [K_j,"j"],
          [K_k,"k"],
          [K_l,"l"],
          [K_m,"m"],
          [K_n,"n"],
          [K_o,"o"],
          [K_p,"p"],
          [K_q,"q"],
          [K_r,"r"],
          [K_s,"s"],
          [K_t,"t"],
          [K_u,"u"],
          [K_v,"v"],
          [K_w,"w"],
          [K_x,"x"],
          [K_y,"y"],
          [K_z,"z"],
          [K_0,"0"],
          [K_1,"1"],
          [K_2,"2"],
          [K_3,"3"],
          [K_4,"4"],
          [K_5,"5"],
          [K_6,"6"],
          [K_7,"7"],
          [K_8,"8"],
          [K_9,"9"],
          [K_KP0,"0"],
          [K_KP1,"1"],
          [K_KP2,"2"],
          [K_KP3,"3"],
          [K_KP4,"4"],
          [K_KP5,"5"],
          [K_KP6,"6"],
          [K_KP7,"7"],
          [K_KP8,"8"],
          [K_KP9,"9"]]
    tchsq=[[K_a,"q"],
          [K_b,"b"],
          [K_c,"c"],
          [K_d,"d"],
          [K_e,"e"],
          [K_f,"f"],
          [K_g,"g"],
          [K_h,"h"],
          [K_i,"i"],
          [K_j,"j"],
          [K_k,"k"],
          [K_l,"l"],
          [K_COMMA,"m"],
          [K_n,"n"],
          [K_o,"o"],
          [K_p,"p"],
          [K_q,"a"],
          [K_r,"r"],
          [K_s,"s"],
          [K_t,"t"],
          [K_u,"u"],
          [K_v,"v"],
          [K_w,"z"],
          [K_x,"x"],
          [K_y,"y"],
          [K_z,"w"],
          [K_0,"0"],
          [K_1,"1"],
          [K_2,"2"],
          [K_3,"3"],
          [K_4,"4"],
          [K_5,"5"],
          [K_6,"6"],
          [K_7,"7"],
          [K_8,"8"],
          [K_9,"9"],
          [K_KP0,"0"],
          [K_KP1,"1"],
          [K_KP2,"2"],
          [K_KP3,"3"],
          [K_KP4,"4"],
          [K_KP5,"5"],
          [K_KP6,"6"],
          [K_KP7,"7"],
          [K_KP8,"8"],
          [K_KP9,"9"]]
    while ncour:
        aff()
        for event in pygame.event.get():
            if event.type==QUIT:
                if texte!="":
                    ncour=False
            elif event.type==KEYDOWN:
                for t in tchsa:
                    if t[0]==event.key: 
                        texte+=t[1]
                if event.key==K_RETURN:
                    if texte!=None:
                        ncour=False
                    return texte
                elif event.key==K_BACKSPACE:
                    texte=texte[:-1]
    return texte            







