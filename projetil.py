import pygame
import math

class Projetil(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho, x_inicial, y_inicial, alvo):
        super().__init__(grupo_de_desenho)
        self.image = pygame.image.load("Imagens/tiro.png")
        self.rect = pygame.Rect(x_inicial, y_inicial, 15, 15)
        self.velocidade = 1

        # Calcula a direção do projétil em relação ao alvo (Hello Kitty)
        direcao_x = alvo.rect.centerx - x_inicial
        direcao_y = alvo.rect.centery - y_inicial
        distancia = math.hypot(direcao_x, direcao_y)
        self.vel_x = (direcao_x / distancia) * self.velocidade
        self.vel_y = (direcao_y / distancia) * self.velocidade

    def update(self):
        # Move o projétil
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Se o projétil sair da tela, destruí-lo
        if self.rect.right < 0 or self.rect.left > 1000 or self.rect.bottom < 0 or self.rect.top > 700:
            self.kill()
