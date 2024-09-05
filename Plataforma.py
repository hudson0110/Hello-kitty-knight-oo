# plataforma.py
import pygame


class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.__rect = pygame.Rect(x, y, largura, altura)  # Define a posição e o tamanho

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self,valor):
        self.__rect = valor
    
