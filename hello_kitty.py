import pygame

class HelloKitty(pygame.sprite.Sprite):
    def __init__(self, grupo_de_desenho):
        super().__init__(grupo_de_desenho)
        self.image = pygame.image.load("Imagens/Personagem.png")
        self.rect = pygame.Rect(50, 552, 100, 100)  # Posição inicial do personagem no chão (y = 552)
        
        # Variáveis de movimento
        self.pos_x = 50.0
        self.pos_y = 552.0
        self.vel_y = 0   
        self.gravidade = 0.004
        self.pulo_forca = -1.2 
        self.no_chao = True
        self.tempo_ultimo_pulo = 0
        self.intervalo_pulo = 1000  # Intervalo de 1000ms entre pulos
        self.velocidade = 0.5

    def mover(self):
        keys = pygame.key.get_pressed()
        tempo_atual = pygame.time.get_ticks()
        
        if keys[pygame.K_a] and self.pos_x > 0: #faz o limite vertical
            self.pos_x -= self.velocidade
        if keys[pygame.K_d] and self.pos_x < 1045 - self.rect.width:     #faz o limite horizontal da tela
            self.pos_x += self.velocidade
        if keys[pygame.K_SPACE] and self.no_chao and (tempo_atual - self.tempo_ultimo_pulo > self.intervalo_pulo):
            self.vel_y = self.pulo_forca
            self.no_chao = False
            self.tempo_ultimo_pulo = tempo_atual

        # Aplicar gravidade
        self.vel_y += self.gravidade
        self.pos_y += self.vel_y

        # Verificar se o personagem está no chão
        if self.pos_y >= 552:  # Verificação da borda do chão (y = 552)
            self.pos_y = 552
            self.vel_y = 0
            self.no_chao = True

        # Atualiza a posição do retângulo do personagem
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)