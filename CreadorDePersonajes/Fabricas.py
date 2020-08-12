from CreadorDePersonajes.Poses import *
class AbstractFactory():
    def moverArriba(self): pass
    def moverDer(self): pass
    def moverAbajo(self): pass
    def moverIzq(self): pass
    def power(self): pass

class WarriorFactory(AbstractFactory):

    def moverAbajo(self):
        abajo = AbajoWarrior()
        return abajo.getSprites()

    def moverArriba(self):
        arriba = ArribaWarrior()
        return arriba.getSprites()

    def moverDer(self):
        der = DerWarrior()
        return der.getSprites()

    def moverIzq(self):
        izq = IzqWarrior()
        return izq.getSprites()

class QueenFactory(AbstractFactory):

    def moverAbajo(self):
        abajo = AbajoQueen()
        return abajo.getSprites()

    def moverArriba(self):
        arriba = ArribaQueen()
        return arriba.getSprites()

    def moverDer(self):
        der = DerQueen()
        return der.getSprites()

    def moverIzq(self):
        izq = IzqQueen()
        return izq.getSprites()