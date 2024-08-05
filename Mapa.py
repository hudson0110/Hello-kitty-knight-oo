import pygame
from pygame.sprite import _Group


class Mapa(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("Imagens/Fundo.jpg")   #add o fundo
        self.image = pygame.transform.scale(self.image,[1000,700])
        self.rect = pygame.Rect(0,0,1000,700)