import pygame as p
import sys
from Board import *
from Musica.chainMusic import *
from Musica.AsignarSucesor import *
from Heroe import *

ventana = p.display.set_mode ((900,800),p.RESIZABLE)

board = Board(ventana)
p.display.set_caption("zombIES")
state = True
z=30
NEGRO = (0,0,0)
soundFx = Asigandora()
perso = Heroe(ventana)
timer = p.time.Clock()



while state:
    for event in p.event.get():
        if event.type == p.QUIT:
            sys.exit()
        if event.type == p.KEYDOWN:
            soundFx.listaSucesores[0].handlerRequest(event.key)
       

    ventana.fill(NEGRO)
    board.pintar()
    p.draw.rect(ventana, NEGRO, perso.update())
    timer.tick(30)
    p.display.update()
    
    