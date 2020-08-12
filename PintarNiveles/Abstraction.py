from CreadorDeNiveles.Creador import *
import pygame as p


class Abstraction():
    def __init__(self, ventana):
        self.ventana = ventana

    def entregarlvl1(self):
        lvl1 = ConcreteImplementation1(self.ventana)
        return lvl1.pintarNivel()

    def entregarlvl2(self): pass
    def entregarlvl3(self): pass


class Implementation():
    def __init__(self, ventana):
        self.VERDE = (15, 255, 8)
        self.ROJO = (255, 0, 0)
        self.ventana = ventana
        self.X = 50
        self.Y = 50
        self.rectangles = []
        self.positions = []

    def pintarNivel(self): pass


class ConcreteImplementation1(Implementation):
    def __init__(self, ventana):
        super().__init__(ventana)

    def pintarNivel(self):
        creat = CreadorNivelFacil()
        prod = creat.diseñarNivel().crear()

        for i in range(len(prod)):
            for j in range(len(prod)):
                if prod[i][j] == "0":
                    p.draw.rect(self.ventana, self.VERDE,
                                (self.X, self.Y, 80, 80))
                    self.rectangles.append(p.Rect(self.X,self.Y,80,80))
                elif prod[i][j] == "1":
                    p.draw.rect(self.ventana, self.ROJO,
                                (self.X, self.Y, 80, 80))
                    self.positions.append((self.X, self.Y))

                self.X = self.X + 80

            self.Y = self.Y + 80
            self.X = 50
