from PintarNiveles.Abstraction import *
class Board():
    def __init__(self, ventana):
        self.pintado = Abstraction(ventana)

    def pintar(self):
        return self.pintado.entregarlvl1()

    

