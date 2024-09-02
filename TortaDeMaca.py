import pygame

class TortaDeMaca(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho, x_inicial, y_inicial):
        super().__init__(grupo_de_desenho)
        self.__image = pygame.image.load("Imagens/torta_de_maca.png")  # Imagem da torta de maçã
        self.__rect = pygame.Rect(x_inicial, y_inicial, 80, 40)  # Tamanho da torta de maçã

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