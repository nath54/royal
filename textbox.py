#coding:utf-8
import pygame
from pygame.locals import *

def main():
    txe,tye=400,250
    texte="pseudo"
    ncour=True
    pygame.init()
    fenetre=pygame.display.set_mode([txe,tye])
    pygame.display.set_caption("text box")
    ztx,zty=tye/2,75
    ctxt=(200,200,250)
    font=pygame.font.SysFont("Serif",50)
    fimg=pygame.transform.scale(pygame.image.load("images/fontxt.png"),[txe,tye])
    def aff():
        fenetre.blit(fimg,[0,0])
        fenetre.blit(font.render(texte,20,ctxt),[ztx,zty])
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
          [K_z,"z"]]
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
          [K_z,"w"]]
    while ncour:
        aff()
        for event in pygame.event.get():
            if event.type==QUIT:
                if texte!="":
                    ncour=False
            elif event.type==KEYDOWN:
                for t in tchsq:
                    if t[0]==event.key: 
                        texte+=t[1]
                if event.key==K_RETURN:
                    if texte!=None:
                        ncour=False
                elif event.key==K_BACKSPACE:
                    texte=texte[:-1]
    return texte            







