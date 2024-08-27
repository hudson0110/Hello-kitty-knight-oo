import pygame
from Plataforma import Plataforma  # Importe a classe Plataforma

class Mapa(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho):
        super().__init__(grupo_de_desenho)
        self.image = pygame.image.load("Imagens/Fundo.jpg")
        self.rect = pygame.Rect(0, 0, 1000, 700)

        # Criando as plataformas
        self.plataforma_1 = Plataforma(180, 462, 500, 20)#DE CIMA
        self.plataforma_2 = Plataforma(370, 334, 245, 20)#TIKTIK
        self.plataforma_3 = Plataforma(792, 243, 110, 20)#MAIS ALTA
        self.plataforma_4 = Plataforma(0, 618, 1000, 20)#CHAO
        
        # Se necessário, armazene as plataformas em uma lista para facilitar o acesso
        self.plataformas = [self.plataforma_1, self.plataforma_2, self.plataforma_3, self.plataforma_4]
