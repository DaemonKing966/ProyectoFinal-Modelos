from Musica.chainMusic import *
class Asigandora():
    def __init__(self):
        self.listaSucesores = [HandlerKey0(), HandlerKey1(), HandlerKey2(), HandlerKey3(),
        HandlerKey4(), HandlerKey5(), HandlreKeyDefault()]
        self.asignarSucesores()

    def asignarSucesores(self):
        for suc in range(len(self.listaSucesores)-1):
            self.listaSucesores[suc].setSucesor(self.listaSucesores[suc + 1 ])