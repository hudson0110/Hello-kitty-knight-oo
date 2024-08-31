import pygame
from projetil import Projetil  # Importe a classe Projetil

class Abelha(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho, x_inicial, y_inicial, alvo):
        super().__init__(grupo_de_desenho)
        self.image = pygame.image.load("Imagens/abelha.png")
        self.rect = pygame.Rect(x_inicial, y_inicial, 80, 80)
        self.pos_x = float(x_inicial)  # Posição em ponto flutuante para precisão
        self.direcao = 1
        self.velocidade = 0.4
        self.grupo_de_desenho = grupo_de_desenho
        self.alvo = alvo
        self.tempo_ultimo_tiro = 1
        self.intervalo_tiro = 2000  # Atira a cada 2000ms (2 segundos)

    def mover_abelha(self):
        self.pos_x += self.direcao * self.velocidade

        self.rect.x = int(self.pos_x)

        if self.rect.left <= 100 or self.rect.right >= 900:
            self.direcao *= -1

        # Verifica se é hora de atirar
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.tempo_ultimo_tiro > self.intervalo_tiro:
            self.atirar()
            self.tempo_ultimo_tiro = tempo_atual

    def atirar(self):
        # Cria um novo projétil e adiciona ao grupo de desenho
        projetil = Projetil(self.grupo_de_desenho, self.rect.centerx, self.rect.centery, self.alvo)
