import pygame

from hello_kitty import HelloKitty
from Tiktik import Tiktik
from menu import Menu
from Abelha import Abelha
from mapa import Mapa
from projetil import Projetil
from TortaDeMaca import TortaDeMaca
import os


class Jogo:
    def __init__(self):
        pygame.init()
        self.vitoria = 0
        self.flip = False
        self.flip2 = False
        self.Gameloop = True
        self.jogo_em_andamento = True
        self.novo_jogo = False

        # self.ataque = pygame.mixer.Sound("Audio/ataque.mp3")
        # self.morte = pygame.mixer.Sound("Audio/morri.mp3")
        # Display
        self.display = pygame.display.set_mode([1000, 700])
        pygame.display.set_caption("Hello Kitty Knight")

        # Grupo de desenhos
        self.grupo_de_desenho = pygame.sprite.Group()
        self.menu = pygame.sprite.Group()

        # Criação dos objetos
        self.menu = Menu(self.menu)
        self.mapa = Mapa(self.grupo_de_desenho)
        self.personagem = HelloKitty(self.grupo_de_desenho, 50, 552)
        self.tiktik = Tiktik(self.grupo_de_desenho, 200, 429)  # 200 429
        self.abelha = Abelha(self.grupo_de_desenho, 300,150, self.personagem)  # 300 150
        self.torta = TortaDeMaca(self.grupo_de_desenho, 830, 200)

        # Plataformas do mapa
        self.plataformas = self.mapa.plataformas

    def exibir_tela_perdeu(self):
        if self.vitoria == 2:
            fonte = pygame.font.Font(None, 150)
            texto = fonte.render("Venceu", True, (0, 255, 0))
            self.display.blit(texto, (330, 100))
            pygame.display.update()
            pygame.time.delay(3000)  # Espera 3 segundos antes de encerrar
            pygame.quit()
            exit()
        else:
            fonte = pygame.font.Font(None, 74)
            texto = fonte.render("Perdeu KK", True, (255, 0, 0))
            self.display.fill((0, 0, 0))
            self.display.blit(texto, (350, 300))
            pygame.display.update()
            pygame.time.delay(3000)  # Espera 3 segundos antes de encerrar
            pygame.quit()
            exit()
            
    def verificar_colisoes(self):

        if pygame.sprite.collide_rect(self.personagem, self.torta):
            self.personagem.pulo_duplo_disponivel = True
            # Remover a torta do jogo (opcional)
            self.torta.kill()

        # Verifica colisão com Tiktik
        if pygame.sprite.collide_rect(self.personagem, self.tiktik):
            if self.personagem.comeu:
                self.tiktik.kill()
                # self.morte.play()
                if not self.flip2:
                    self.vitoria += 1
                    self.flip2 = True

            else:
                self.jogo_em_andamento = False

        # Verifica colisão com Abelha
        if pygame.sprite.collide_rect(self.personagem, self.abelha):
            if self.personagem.comeu:
                self.abelha.kill()
                self.abelha.vivo = False
                if not self.flip:
                    self.vitoria += 1
                    self.flip = True
            else:
                self.jogo_em_andamento = False

        # Verifica colisão com qualquer projetil
        for projetil in self.grupo_de_desenho:
            if isinstance(projetil, Projetil) and pygame.sprite.collide_rect(self.personagem, projetil):
                self.jogo_em_andamento = False
                

    def executar(self):
        no_menu = False
        em_jogo = False
        pygame.mixer.music.load("Audio/Musica.mp3")
        pygame.mixer.music.play(-1)
        while self.Gameloop:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.Gameloop = False

            if self.jogo_em_andamento:
                self.menu.update()

                if (not em_jogo):
                    if self.menu.inicia_jogo() :
                        no_menu = True
                    elif self.menu.inicia_saves() :
                        no_menu = True
                    if self.menu.inicia_jogo():
                        if os.path.exists('save.json'):
                            os.remove('save.json')
                            print("Arquivo deletado com sucesso")
                        else:
                            print("O arquivo não existe")

                    if (no_menu):
                        em_jogo = True

                self.display.fill((0, 0, 0))
                if(no_menu):
                    #self.personagem.carregarPosicao()
                    if self.vitoria == 2:
                        self.jogo_em_andamento = False
                    self.personagem.mover(self.plataformas)
                    self.tiktik.mover()
                    self.abelha.mover()                   
                    self.verificar_colisoes()
                    self.grupo_de_desenho.update()  # Atualiza todos os sprites no grupo
                if(no_menu):
                    self.grupo_de_desenho.draw(self.display)
                else:
                    self.menu.draw(self.display)
                pygame.display.update()
            else:
                self.exibir_tela_perdeu()
                self.Gameloop = False

        pygame.quit()