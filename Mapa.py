import pygame
from Plataforma import Plataforma  # Importe a classe Plataforma

class Mapa(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho):
        super().__init__(grupo_de_desenho)
        self.__image = pygame.image.load("Imagens/Fundo.jpg")
        self.__rect = pygame.Rect(0, 0, 1000, 700)

        # Criando as plataformas
        self.__plataforma_1 = Plataforma(125, 462, 555, 20)  # DE CIMA
        self.__plataforma_2 = Plataforma(
            335, 334, 255, 20)  # TIKTIK x: 370, largura 245
        # MAIS ALTA x 792 largura tava 110
        self.__plataforma_3 = Plataforma(745, 243, 145, 20)
        self.__plataforma_4 = Plataforma(0, 618, 1000, 20)  # CHAO

        # Se necessário, armazene as plataformas em uma lista para facilitar o acesso
        self.__plataformas = [self.__plataforma_1, self.__plataforma_2, self.__plataforma_3, self.__plataforma_4]

    @property
    def plataforma_1(self):
        return self.__plataforma_1

    @plataforma_1.setter
    def plataforma_1(self, value):
        self.__plataforma_1 = value

    @property
    def plataforma_2(self):
        return self.__plataforma_2

    @plataforma_2.setter
    def plataforma_2(self, value):
        self.__plataforma_2 = value

    @property
    def plataforma_3(self):
        return self.__plataforma_3

    @plataforma_3.setter
    def plataforma_3(self, value):
        self.__plataforma_3 = value

    @property
    def plataforma_4(self):
        return self.__plataforma_4

    @plataforma_4.setter
    def plataforma_4(self, value):
        self.__plataforma_4 = value

    @property
    def plataformas(self):
        return self.__plataformas

    @plataformas.setter
    def plataformas(self, value):
        self.__plataformas = value



        #gets

    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
        #sets

    @image.setter
    def image(self,valor):
        self.__image = valor

    @rect.setter
    def rect(self,valor):
        self.__rect = valor
    
