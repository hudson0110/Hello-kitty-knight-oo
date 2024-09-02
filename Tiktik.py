import pygame


class Tiktik(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho, x_inicial, y_inicial):
        super().__init__(grupo_de_desenho)
        self.__image = pygame.image.load("Imagens/tiktik.png")
        self.__rect = pygame.Rect(x_inicial, y_inicial, 80, 80)  # Define a posição inicial
        self.__pos_x = float(x_inicial)  # Posição em ponto flutuante para precisão
        self.__direcao = 1  # 1 para a direita, -1 para a esquerda
        self.__velocidade = 0.2  # Velocidade do inimigo (agora pode ser menor que 1)

    #gets

    @property
    def image(self):
        return self.__image
    
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
    
    #sets

    @image.setter
    def image(self,valor):
        self.__image = valor

    @rect.setter
    def rect(self,valor):
        self.__rect = valor

    @pos_x.setter
    def pos_x(self,valor):
        self.__pos_x = valor

    @direcao.setter
    def direcao(self,valor):
        self.__direcao = valor

    @velocidade.setter
    def velocidade(self,valor):
        self.__velocidade = valor

    def mover_tiktik(self):
        # Movimenta a tiktik horizontalmente com precisão em float
        self.pos_x += self.direcao * self.velocidade

        # Atualiza a posição do retângulo com a parte inteira da posição
        self.rect.x = int(self.pos_x)

        # Verifica se a tiktik atingiu as bordas para mudar de direção
        if self.rect.left <= 160 or self.rect.right >= 700:
            self.direcao *= -1  # Inverte a direção