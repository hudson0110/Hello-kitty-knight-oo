import pygame
import random

pygame.init()


#variaveis
gameloop = True           #mantem o jogo rodando

#display
display = pygame.display.set_mode([1000 ,700]) #cria a janela
pygame.display.set_caption("Hello Kitty Knight")  #nome da janela



#desenhos
grupo_de_desenho = pygame.sprite.Group()  #crio um grupo com minhas sprites

fundo = pygame.sprite.Sprite(grupo_de_desenho)
fundo.image = pygame.image.load("Imagens/Fundo.jpg")   #add o fundo
fundo.image = pygame.transform.scale(fundo.image,[1000,700])
fundo.rect = pygame.Rect(0,0,1000,700)

Personagem = pygame.sprite.Sprite(grupo_de_desenho)
Personagem.image = pygame.image.load("Imagens/Personagem.png") #add a hello kitty
Personagem.rect = pygame.Rect(50,552,100,100)



#musica
pygame.mixer.music.load("Audio/Musica.mp3")
pygame.mixer.music.play(-1)

#sons

pegar_item = pygame.mixer.Sound("Audio/pop.ogg")


#teclas

if __name__ == "__main__":
    while gameloop:
        for evento in pygame.event.get():       #verifica se a tecla foi apertada
            if evento.type == pygame.QUIT:      #aqui az o jogo fecha
                gameloop = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pegar_item.play()
            
        
        keys = pygame.key.get_pressed() #salva na fila quais teclas estao sendo apertadas
        
        if keys[pygame.K_d]:
            Personagem.rect.x += 1
        if keys[pygame.K_a]:
            Personagem.rect.x -= 1
        if keys[pygame.K_w]:
            Personagem.rect.y -= 1
        if keys[pygame.K_s]:
            Personagem.rect.y += 1

    
        #desenhar
        
        grupo_de_desenho.draw(display) #desenha tudo na tela
        pygame.display.update()
