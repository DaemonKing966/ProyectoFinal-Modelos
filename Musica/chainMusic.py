import pygame as p
class ChainMusic():
    def __init__(self):
        self.__sucesor__ = None
        p.mixer.init()

    def handlerRequest(self,key): pass

    def setSucesor(self, sucesor):
        self.__sucesor__ = sucesor

class HandlerKey0(ChainMusic):
    def handlerRequest(self, key):
        p.mixer.music.load("Musica/0.mp3")
        if key == p.K_0:
            p.mixer.music.play()
        else:
            self.__sucesor__.handlerRequest(key)
    
class HandlerKey1(ChainMusic):
    def handlerRequest(self, key):
        p.mixer.music.load("Musica/1.mp3")
        if key == p.K_1:
            p.mixer.music.play()
        else:
            self.__sucesor__.handlerRequest(key)

class HandlerKey2(ChainMusic):
    def handlerRequest(self, key):
        p.mixer.music.load("Musica/2.mp3")
        if key == p.K_2:
            p.mixer.music.play()
        else:
            self.__sucesor__.handlerRequest(key)

class HandlerKey3(ChainMusic):
    def handlerRequest(self, key):
        p.mixer.music.load("Musica/3.mp3")
        if key == p.K_3:
            p.mixer.music.play()
        else:
            self.__sucesor__.handlerRequest(key)

class HandlerKey4(ChainMusic):
    def handlerRequest(self, key):
        p.mixer.music.load("Musica/4.mp3")
        if key == p.K_4:
            p.mixer.music.play()
        else:
            self.__sucesor__.handlerRequest(key)

class HandlerKey5(ChainMusic):
    def handlerRequest(self, key):
        p.mixer.music.load("Musica/5.mp3")
        if key == p.K_5:
            p.mixer.music.play()
        else:
            self.__sucesor__.handlerRequest(key)

class HandlreKeyDefault(ChainMusic):
    def handlerRequest(self, key): pass
        



            
        