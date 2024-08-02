import pygame
import random

pygame.init()

largura_da_janela = 840   #muda o tamanho
altura_da_janela= 480
gameloop = True           #mantem o jogo rodando


display = pygame.display.set_mode([largura_da_janela,altura_da_janela]) #cria a janela

pygame.display.set_caption("Hello Kitty Knight")  #nome da janela

def desenhar():
    display.fill([255,192,203])

if __name__ == "__main__":
    while gameloop:
        for evento in pygame.event.get():       #verifica se a tecla foi apertada
            if evento.type == pygame.QUIT:      #aqui az o jogo fecha
                gameloop = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:    #verifica se a tecla foi apertada
                    print("funciona")  
        
        keys = pygame.key.get_pressed() #salva na fila quais teclas estao sendo apertadas

        if keys[pygame.K_w]:
            print("segurando")


        desenhar()
        pygame.display.update()
