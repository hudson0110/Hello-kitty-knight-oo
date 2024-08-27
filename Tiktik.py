import pygame




class Tiktik(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho, x_inicial, y_inicial):
        super().__init__(grupo_de_desenho)
        self.image = pygame.image.load("Imagens/Tiktik.png")
        self.rect = pygame.Rect(x_inicial, y_inicial, 80, 80)  # Define a posição inicial
        self.direcao = 1  # 1 para a direita, -1 para a esquerda
        self.velocidade = 1  # Velocidade do inimigo

    def mover(self):
        # Movimenta o Tiktik horizontalmente
        self.rect.x += self.direcao * self.velocidade

        # Verifica se o Tiktik atingiu as bordas para mudar de direção
        if self.rect.left <= 160 or self.rect.right >= 720:
            self.direcao *= -1  # Inverte a direção

        # Debug: Imprime a posição atual
        print(f"Posição X do Tiktik: {self.rect.x}")
