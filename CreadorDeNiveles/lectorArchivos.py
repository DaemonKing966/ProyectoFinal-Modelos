class LectorArchivo():

    def __init__(self):
        self.data=[]
        self.matriz=[]
        self.filas = 10
        self.columnas = 10

    def leerNivel(self, path):
        f = open(path, 'r')
        for line in f.readlines():
            self.data.append(line.replace('\n', '').split(' '))
        f.close()

        return self.data

    

    




