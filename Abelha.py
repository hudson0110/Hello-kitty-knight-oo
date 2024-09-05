import pygame
from projetil import Projetil  # Importe a classe Projetil
from inimigos import Inimigo  # Importe a classe base Inimigo

class Abelha(Inimigo):
    def __init__(self, grupo_de_desenho, x_inicial, y_inicial, alvo):
        super().__init__(grupo_de_desenho, x_inicial, y_inicial, 80, 80, 0.4, 100, 900)
        self.__image = pygame.image.load("Imagens/abelha.png")
        self.__alvo = alvo
        self.__tempo_ultimo_tiro = 1
        self.__intervalo_tiro = 2000  # Atira a cada 2000ms (2 segundos)
        self.vivo = True

    # Gets e Sets da Abelha

    @property
    def image(self):
        return self.__image

    @property
    def alvo(self):
        return self.__alvo

    @property
    def tempo_ultimo_tiro(self):
        return self.__tempo_ultimo_tiro

    @property
    def intervalo_tiro(self):
        return self.__intervalo_tiro

    @image.setter
    def image(self, valor):
        self.__image = valor

    @alvo.setter
    def alvo(self, valor):
        self.__alvo = valor

    @tempo_ultimo_tiro.setter
    def tempo_ultimo_tiro(self, valor):
        self.__tempo_ultimo_tiro = valor

    @intervalo_tiro.setter
    def intervalo_tiro(self, valor):
        self.__intervalo_tiro = valor

    def mover(self):
        # Sobrescrevendo o método mover para o comportamento específico da Abelha
        super().mover()  # Chama o movimento genérico da classe pai
        print("Abelha movida")
        # Abelha pode também atirar
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.tempo_ultimo_tiro > self.intervalo_tiro:
            self.atirar()

    def atirar(self):
        # Cria um novo projétil e adiciona ao grupo de desenho
        projetil = Projetil(self.grupo_de_desenho, self.rect.centerx, self.rect.centery, self.alvo)
