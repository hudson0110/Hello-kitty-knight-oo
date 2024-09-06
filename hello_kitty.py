import pygame
from Save import saves


class HelloKitty(pygame.sprite.Sprite,saves):
    def __init__(self, grupo_de_desenho, Ipos_x, Ipos_y):
        super().__init__(grupo_de_desenho)
        self.__image = pygame.image.load("Imagens/Personagem.png")
        # Posição inicial do personagem no chão (y = 552)
        self.__rect = pygame.Rect(50, 552, 20, 67)

        # Variáveis de movimento
        self.__pos_x = Ipos_x
        self.__pos_y = Ipos_y
        self.__vel_y = 0
        self.__gravidade = 0.004
        self.__pulo_forca = -1.2
        self.__no_chao = True
        self.__tempo_ultimo_pulo = 0
        self.__intervalo_pulo = 500  # Intervalo de 500ms entre pulos
        self.__velocidade = 0.3
        self.__grupo_de_desenho = grupo_de_desenho
        pygame.display.set_caption("Hello Kitty Knight")

        self.__pulo_duplo_disponivel = False
        self.__usou = False
        self.__comeu = False
        self.__carregar = False
        self.__salvou_uma_vez = False
        self.__pulo_song = pygame.mixer.Sound("Audio/pop.ogg")

    @property
    def usou(self):
        return self.__usou

    @usou.setter
    def usou(self, value):
        self.__usou = value

    @property
    def comeu(self):
        return self.__comeu

    @comeu.setter
    def comeu(self, value):
        self.__comeu = value

    @property
    def carregar(self):
        return self.__carregar

    @carregar.setter
    def carregar(self, value):
        self.__carregar = value

    @property
    def salvou_uma_vez(self):
        return self.__salvou_uma_vez

    @salvou_uma_vez.setter
    def salvou_uma_vez(self, value):
        self.__salvou_uma_vez = value

    @property
    def pulo_song(self):
        return self.__pulo_song

    @pulo_song.setter
    def pulo_song(self, value):
        self.__pulo_song = value


        # gets

    @property
    def image(self):
        return self.__image

    @property
    def pulo_duplo_disponivel(self):
        return self.__pulo_duplo_disponivel

    @property
    def rect(self):
        return self.__rect

    @property
    def pos_x(self):
        return self.__pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    @property
    def vel_y(self):
        return self.__vel_y

    @property
    def gravidade(self):
        return self.__gravidade

    @property
    def pulo_forca(self):
        return self.__pulo_forca

    @property
    def no_chao(self):
        return self.__no_chao

    @property
    def tempo_ultimo_pulo(self):
        return self.__tempo_ultimo_pulo

    @property
    def intervalo_pulo(self):
        return self.__intervalo_pulo

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def grupo_de_desenho(self):
        return self.__grupo_de_desenho

    # sets

    @pulo_duplo_disponivel.setter
    def pulo_duplo_disponivel(self, valor):
        self.__pulo_duplo_disponivel = valor
        self.comeu = valor

    @image.setter
    def image(self, valor):
        self.__image = valor

    @rect.setter
    def rect(self, valor):
        self.__rect = valor

    @pos_x.setter
    def pos_x(self, valor):
        self.__pos_x = valor

    @pos_y.setter
    def pos_y(self, valor):
        self.__pos_y = valor

    @vel_y.setter
    def vel_y(self, valor):
        self.__vel_y = valor

    @gravidade.setter
    def gravidade(self, valor):
        self.__gravidade = valor

    @pulo_forca.setter
    def pulo_forca(self, valor):
        self.__pulo_forca = valor

    @no_chao.setter
    def no_chao(self, valor):
        self.__no_chao = valor

    @tempo_ultimo_pulo.setter
    def tempo_ultimo_pulo(self, valor):
        self.__tempo_ultimo_pulo = valor

    @intervalo_pulo.setter
    def intervalo_pulo(self, valor):
        self.__intervalo_pulo = valor

    @velocidade.setter
    def velocidade(self, valor):
        self.__velocidade = valor

    @grupo_de_desenho.setter
    def grupo_de_desenho(self, valor):
        self.__grupo_de_desenho = valor


    def mover(self, plataformas):
        keys = pygame.key.get_pressed()
        tempo_atual = pygame.time.get_ticks()
        if not self.carregar:
            posicao = self.carregar_posicao()
            self.pos_x = posicao['x']
            self.pos_y = posicao['y']

            # Atualizar o rect para refletir a nova posição carregada
            self.rect.x = int(self.pos_x)
            # Certifique-se de atualizar rect.y também
            self.rect.y = int(self.pos_y)
            print(f"Posição carregada: X={self.pos_x}, Y={self.pos_y}")
            self.carregar = True
        if (self.comeu and not self.salvou_uma_vez):
            # Posição atual do personagem
            posicao_atual = {'x': self.pos_x, 'y': self.pos_y}
            self.salvar_posicao(posicao_atual)
            self.salvou_uma_vez = True

        # Movimentação horizontal
        if keys[pygame.K_a] and self.pos_x > 0:  # Limite à esquerda
            self.pos_x -= self.velocidade
        if keys[pygame.K_d] and self.pos_x < 1000 - self.rect.width:  # Limite à direita
            self.pos_x += self.velocidade
        # Pulo
        if keys[pygame.K_SPACE]:
            if self.no_chao and (tempo_atual - self.tempo_ultimo_pulo > self.intervalo_pulo):
                self.vel_y = self.pulo_forca
                self.no_chao = False
                self.pulo_song.play()
                
                
                self.tempo_ultimo_pulo = tempo_atual
                if (self.comeu):
                    self.usou = True
            if self.pulo_duplo_disponivel and not self.no_chao and self.usou and (tempo_atual - self.tempo_ultimo_pulo > (self.intervalo_pulo - 200)):
                self.vel_y = self.pulo_forca
                self.no_chao = False
                self.tempo_ultimo_pulo = tempo_atual
                self.usou = False
                self.pulo_song.play()
               

        # Aplicar gravidade
        self.vel_y += self.gravidade
        self.pos_y += self.vel_y

        # Verificar colisões com as plataformas
        self.no_chao = False  # Presumimos que não está no chão até verificar
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                # Verificar se o personagem está caindo
                if self.vel_y > 0:
                    # Ajusta a posição para cima da plataforma
                    self.pos_y = plataforma.rect.top - self.rect.height
                    self.vel_y = 0
                    self.no_chao = True
                    if (self.comeu):
                        self.pulo_duplo_disponivel = True  # tava false

        # Atualiza a posição do retângulo do personagem
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)