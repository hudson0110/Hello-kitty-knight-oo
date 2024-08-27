import pygame


class Tiktik(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho, x_inicial, y_inicial):
        super().__init__(grupo_de_desenho)
        self.image = pygame.image.load("Imagens/tiktik.png")
        self.rect = pygame.Rect(x_inicial, y_inicial, 80, 80)  # Define a posição inicial
        self.pos_x = float(x_inicial)  # Posição em ponto flutuante para precisão
        self.direcao = 1  # 1 para a direita, -1 para a esquerda
        self.velocidade = 0.2  # Velocidade do inimigo (agora pode ser menor que 1)

    def mover_tiktik(self):
        # Movimenta a tiktik horizontalmente com precisão em float
        self.pos_x += self.direcao * self.velocidade

        # Atualiza a posição do retângulo com a parte inteira da posição
        self.rect.x = int(self.pos_x)

        # Verifica se a tiktik atingiu as bordas para mudar de direção
        if self.rect.left <= 160 or self.rect.right >= 700:
            self.direcao *= -1  # Inverte a direção