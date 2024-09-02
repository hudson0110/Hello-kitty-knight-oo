import pygame

class HelloKitty(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho):
        super().__init__(grupo_de_desenho)
        self.__image = pygame.image.load("Imagens/Personagem.png")
        self.__rect = pygame.Rect(50, 552, 67, 67)  # Posição inicial do personagem no chão (y = 552)
        
        # Variáveis de movimento
        self.__pos_x = 50.0
        self.__pos_y = 552.0
        self.__vel_y = 0   
        self.__gravidade = 0.004
        self.__pulo_forca = -1.2 
        self.__no_chao = True
        self.__tempo_ultimo_pulo = 0
        self.__intervalo_pulo = 500  # Intervalo de 500ms entre pulos
        self.__velocidade = 0.3
        self.__grupo_de_desenho = grupo_de_desenho

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

    @pos_y.setter
    def pos_y(self,valor):
        self.__pos_y = valor

    @vel_y.setter
    def vel_y(self,valor):
        self.__vel_y = valor
    
    @gravidade.setter
    def gravidade(self,valor):
        self.__gravidade = valor

    @pulo_forca.setter
    def pulo_forca(self,valor):
        self.__pulo_forca = valor

    @no_chao.setter
    def no_chao(self,valor):
        self.__no_chao = valor

    @tempo_ultimo_pulo.setter
    def tempo_ultimo_pulo(self,valor):
        self.__tempo_ultimo_pulo = valor

    @intervalo_pulo.setter
    def intervalo_pulo(self,valor):
        self.__intervalo_pulo = valor

    @velocidade.setter
    def velocidade(self,valor):
        self.__velocidade = valor

    @grupo_de_desenho.setter
    def grupo_de_desenho(self,valor):
        self.__grupo_de_desenho = valor




    def mover(self, plataformas):
        keys = pygame.key.get_pressed()
        tempo_atual = pygame.time.get_ticks()
        
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
                self.pulo_duplo_disponivel = True
                self.tempo_ultimo_pulo = tempo_atual
           
                self.vel_y = self.pulo_forca


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
                    self.pulo_duplo_disponivel = False

        # Verificar se o personagem está no chão (fundo do mapa)
        if self.pos_y >= 552:
            self.pos_y = 552
            self.vel_y = 0
            self.no_chao = True
            self.pulo_duplo_disponivel = False

        # Atirar
        if keys[pygame.K_2] and self.pode_atirar:
            self.atirar()

        # Atualiza a posição do retângulo do personagem
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)

