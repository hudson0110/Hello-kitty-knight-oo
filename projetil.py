import pygame
import math

class Projetil(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho, x_inicial, y_inicial, alvo):
        super().__init__(grupo_de_desenho)
        self.__image = pygame.image.load("Imagens/tiro.png")
        self.__rect = pygame.Rect(x_inicial, y_inicial, 15, 15)
        self.__velocidade = 0.9

        # Calcula a direção do projétil em relação ao alvo (Hello Kitty)
        direcao_x = alvo.rect.centerx - x_inicial
        direcao_y = alvo.rect.centery - y_inicial
        distancia = math.hypot(direcao_x, direcao_y)
        self.__vel_x = (direcao_x / distancia) / self.velocidade
        self.__vel_y = (direcao_y  / distancia) / self.velocidade

    #gets

    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @property 
    def vel_y(self):
        return self.__vel_y
    
    @property 
    def vel_x(self):
        return self.__vel_x
    
    
    
    #sets

    @image.setter
    def image(self,valor):
        self.__image = valor

    @rect.setter
    def rect(self,valor):
        self.__rect = valor

    @velocidade.setter
    def velocidade(self,valor):
        self.__velocidade = valor

    @vel_y.setter
    def vel_y(self,valor):
        self.__vel_y = valor

    @vel_x.setter
    def vel_x(self,valor):
        self.__vel_x = valor
        

    def update(self):
        # Move o projétil
        self.rect.x += (self.vel_x )
        self.rect.y += (self.vel_y )

        # Se o projétil sair da tela, destruí-lo
        if self.rect.right < 0 or self.rect.left > 1000 or self.rect.bottom < 0 or self.rect.top > 700:
            self.kill()
