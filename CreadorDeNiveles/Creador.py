from abc import ABC, abstractmethod
from CreadorDeNiveles.Niveles import *

class CreadorNivel(ABC):
    def diseñarNivel(self):
        return self.crearTablero()

    @abstractmethod
    def crearTablero(self): pass


class CreadorNivelFacil(CreadorNivel):
    def crearTablero(self):
        return NivelFacil()


class CreadorNivelMedio(CreadorNivel):
    def crearTablero(self): pass


class CreadorNivelDificil(CreadorNivel):
    def crearTablero(self): pass
