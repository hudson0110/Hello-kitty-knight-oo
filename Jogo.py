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
        self.__vitoria = 0
        self.__flip = False
        self.__flip2 = False
        self.__Gameloop = True
        self.__jogo_em_andamento = True
        self.__novo_jogo = False
        self.__morte = pygame.mixer.Sound("Audio/morte.mp3")
        self.__display = pygame.display.set_mode([1000, 700])
        self.__grupo_de_desenho = pygame.sprite.Group()
        self.__menu = pygame.sprite.Group()
        self.__menu = Menu(self.__menu)
        self.__mapa = Mapa(self.__grupo_de_desenho)
        self.__personagem = HelloKitty(self.__grupo_de_desenho, 50, 552)
        self.__tiktik = Tiktik(self.__grupo_de_desenho, 200, 429)  # 200 429
        self.__abelha = Abelha(self.__grupo_de_desenho, 300,150, self.__personagem)  # 300 150
        self.__torta = TortaDeMaca(self.__grupo_de_desenho, 830, 200)
        self.__plataformas = self.__mapa.plataformas

    @property
    def morte(self):
        return self.__morte

    @morte.setter
    def morte(self, value):
        self.__morte = value

    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, value):
        self.__display = value

    @property
    def grupo_de_desenho(self):
        return self.__grupo_de_desenho

    @grupo_de_desenho.setter
    def grupo_de_desenho(self, value):
        self.__grupo_de_desenho = value

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, value):
        self.__menu = value

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, value):
        self.__menu = value

    @property
    def mapa(self):
        return self.__mapa

    @mapa.setter
    def mapa(self, value):
        self.__mapa = value

    @property
    def personagem(self):
        return self.__personagem

    @personagem.setter
    def personagem(self, value):
        self.__personagem = value

    @property
    def tiktik(self):
        return self.__tiktik

    @tiktik.setter
    def tiktik(self, value):
        self.__tiktik = value

    @property
    def abelha(self):
        return self.__abelha

    @abelha.setter
    def abelha(self, value):
        self.__abelha = value

    @property
    def torta(self):
        return self.__torta

    @torta.setter
    def torta(self, value):
        self.__torta = value

    @property
    def plataformas(self):
        return self.__plataformas

    @plataformas.setter
    def plataformas(self, value):
        self.__plataformas = value





    @property
    def vitoria(self):
        return self.__vitoria

    @vitoria.setter
    def vitoria(self, value):
        self.__vitoria = value

    @property
    def flip(self):
        return self.__flip

    @flip.setter
    def flip(self, value):
        self.__flip = value

    @property
    def flip2(self):
        return self.__flip2

    @flip2.setter
    def flip2(self, value):
        self.__flip2 = value

    @property
    def Gameloop(self):
        return self.__Gameloop

    @Gameloop.setter
    def Gameloop(self, value):
        self.__Gameloop = value

    @property
    def jogo_em_andamento(self):
        return self.__jogo_em_andamento

    @jogo_em_andamento.setter
    def jogo_em_andamento(self, value):
        self.__jogo_em_andamento = value

    @property
    def novo_jogo(self):
        return self.__novo_jogo

    @novo_jogo.setter
    def novo_jogo(self, value):
        self.__novo_jogo = value



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
            self.morte.play()
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