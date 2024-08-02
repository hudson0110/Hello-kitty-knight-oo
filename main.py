import pygame
import random


pygame.init()


largura_da_janela = 840   #muda o tamanho
altura_da_janela= 480
gameloop = True           #mantem o jogo rodando



display = pygame.display.set_mode([largura_da_janela,altura_da_janela]) #cria a janela

pygame.display.set_caption("Hello Kitty Knight")  #nome da janela

def desenhar():
    display.fill([ 111,66,66])

if __name__ == "__main__":
    



    while gameloop:
        desenhar()

        pygame.display.update