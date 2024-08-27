# plataforma.py
import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        #self.image = pygame.Surface([largura, altura])
        #self.image.fill((255, 0, 0))  # Define uma cor para a plataforma (vermelho)
        self.rect = pygame.Rect(x, y, largura, altura)  # Define a posição e o tamanho
