import pygame
from projetil import Projetil  # Importe a classe Projetil

class Abelha(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho, x_inicial, y_inicial, alvo):
        super().__init__(grupo_de_desenho)
        self.__image = pygame.image.load("Imagens/abelha.png")
        self.__rect = pygame.Rect(x_inicial, y_inicial, 80, 80)
        self.__pos_x = float(x_inicial)  # Posição em ponto flutuante para precisão
        self.__direcao = 1
        self.__velocidade = 0.4
        self.__grupo_de_desenho = grupo_de_desenho
        self.__alvo = alvo
        self.__tempo_ultimo_tiro = 1
        self.__intervalo_tiro = 2000  # Atira a cada 2000ms (2 segundos)

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
    
    @property
    def grupo_de_desenho(self):
        return self.__grupo_de_desenho
    
    @property
    def alvo(self):
        return self.__alvo
    
    @property
    def tempo_ultimo_tiro(self):
        return self.__tempo_ultimo_tiro
    
    @property
    def intervalo_tiro(self):
        return self.__intervalo_tiro

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

    @grupo_de_desenho.setter
    def grupo_de_desenho(self,valor):
        self.__grupo_de_desenho = valor

    @alvo.setter
    def alvo(self,valor):
        self.__alvo = valor

    @tempo_ultimo_tiro.setter
    def tempo_ultimo_tiro(self,valor):
        self.__tempo_ultimo_tiro = valor

    @intervalo_tiro.setter
    def intervalo_tiro(self,valor):
        self.__intervalo_tiro = valor
    

    def mover_abelha(self):
        self.pos_x += self.direcao * self.velocidade

        self.rect.x = int(self.pos_x)

        if self.rect.left <= 100 or self.rect.right >= 900:
            self.direcao *= -1

        # Verifica se é hora de atirar
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.tempo_ultimo_tiro > self.intervalo_tiro:
            #self.atirar()
            self.tempo_ultimo_tiro = tempo_atual

    def atirar(self):
        # Cria um novo projétil e adiciona ao grupo de desenho
        projetil = Projetil(self.grupo_de_desenho, self.rect.centerx, self.rect.centery, self.alvo)
