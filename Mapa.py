import pygame
from Plataforma import Plataforma  # Importe a classe Plataforma

class Mapa(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho):
        super().__init__(grupo_de_desenho)
        self.__image = pygame.image.load("Imagens/Fundo.jpg")
        self.__rect = pygame.Rect(0, 0, 1000, 700)

        # Criando as plataformas
        self.plataforma_1 = Plataforma(125, 462, 555, 20)#DE CIMA
        self.plataforma_2 = Plataforma(335, 334, 255, 20)#TIKTIK x: 370, largura 245
        self.plataforma_3 = Plataforma(745, 243, 145, 20)#MAIS ALTA x 792 largura tava 110
        self.plataforma_4 = Plataforma(0, 618, 1000, 20)#CHAO
        
        # Se necessário, armazene as plataformas em uma lista para facilitar o acesso
        self.plataformas = [self.plataforma_1, self.plataforma_2, self.plataforma_3, self.plataforma_4]


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
    
