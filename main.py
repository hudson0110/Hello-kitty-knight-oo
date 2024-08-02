import pygame
import random

pygame.init()

largura_da_janela = 1000   #muda o tamanho
altura_da_janela= 700
gameloop = True           #mantem o jogo rodando

grupo_de_desenho = pygame.sprite.Group()  #crio um grupo com minhas sprites

fundo = pygame.sprite.Sprite(grupo_de_desenho)
fundo.image = pygame.image.load("Imagens/Fundo.jpg")   #add o fundo
fundo.rect = pygame.Rect(0,0,largura_da_janela,altura_da_janela)

Personagem = pygame.sprite.Sprite(grupo_de_desenho)
Personagem.image = pygame.image.load("Imagens/Personagem.png") #add a hello kitty
Personagem.rect = pygame.Rect(50,552,50,50)


display = pygame.display.set_mode([largura_da_janela,altura_da_janela]) #cria a janela

pygame.display.set_caption("Hello Kitty Knight")  #nome da janela

if __name__ == "__main__":
    while gameloop:
        for evento in pygame.event.get():       #verifica se a tecla foi apertada
            if evento.type == pygame.QUIT:      #aqui az o jogo fecha
                gameloop = False
            
        
        keys = pygame.key.get_pressed() #salva na fila quais teclas estao sendo apertadas

    


        #desenhar
        
        grupo_de_desenho.draw(display) #desenha tudo na tela

        pygame.display.update()
