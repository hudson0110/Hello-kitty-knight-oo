import pygame
from inimigos import Inimigo  # Importe a classe base Inimigo

class Tiktik(Inimigo):
    def __init__(self, grupo_de_desenho, x_inicial, y_inicial):
        super().__init__(grupo_de_desenho, x_inicial, y_inicial, 80, 80, 0.2, 160, 700)
        self.__image = pygame.image.load("Imagens/tiktik.png")

    # Gets e Sets da Tiktik

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, valor):
        self.__image = valor

    def mover(self):        
        super().mover()  
        print("Tiktik movida")
