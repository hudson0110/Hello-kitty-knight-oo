import pygame

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho, x_inicial, y_inicial, largura, altura, velocidade, limite_esquerdo, limite_direito):
        super().__init__(grupo_de_desenho)
        self.__rect = pygame.Rect(x_inicial, y_inicial, largura, altura)  # Retângulo do inimigo
        self.__pos_x = float(x_inicial)  # Posição em ponto flutuante para precisão
        self.__direcao = 1  # 1 para direita, -1 para esquerda
        self.__velocidade = velocidade  # Velocidade do inimigo
        self.__grupo_de_desenho = grupo_de_desenho
        self.__limite_esquerdo = limite_esquerdo
        self.__limite_direito = limite_direito

    @property
    def limite_esquerdo(self):
        return self.__limite_esquerdo

    @limite_esquerdo.setter
    def limite_esquerdo(self, value):
        self.__limite_esquerdo = value

    @property
    def limite_direito(self):
        return self.__limite_direito

    @limite_direito.setter
    def limite_direito(self, value):
        self.__limite_direito = value


    # Gets

    @property
    def rect(self):
        return self.__rect

    @property
    def pos_x(self):
        return self.__pos_x

    @property
    def direcao(self):
        return self.__direcao

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def grupo_de_desenho(self):
        return self.__grupo_de_desenho

    # Sets

    @rect.setter
    def rect(self, valor):
        self.__rect = valor

    @pos_x.setter
    def pos_x(self, valor):
        self.__pos_x = valor

    @direcao.setter
    def direcao(self, valor):
        self.__direcao = valor

    @velocidade.setter
    def velocidade(self, valor):
        self.__velocidade = valor

    def mover(self):
        # Movimenta o inimigo horizontalmente
        self.pos_x += self.direcao * self.velocidade

        # Atualiza a posição do retângulo
        self.rect.x = int(self.pos_x)

        # Verifica se o inimigo atingiu as bordas para mudar de direção
        if self.rect.left <= self.limite_esquerdo or self.rect.right >= self.limite_direito:
            self.direcao *= -1  # Inverte a direção
