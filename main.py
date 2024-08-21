import pygame
from hello_kitty import HelloKitty

pygame.init()

Gameloop = True

grupo_de_desenho = pygame.sprite.Group()  # Cria um grupo com minhas sprites

# MAPA
fundo = pygame.sprite.Sprite(grupo_de_desenho)
fundo.image = pygame.image.load("Imagens/Fundo.jpg")  # Adiciona o fundo
fundo.image = pygame.transform.scale(fundo.image, [1000, 700])
fundo.rect = pygame.Rect(0, 0, 1000, 700)

# Cria o personagem
personagem = HelloKitty(grupo_de_desenho)

# INIMIGO
Tiktik = pygame.sprite.Sprite(grupo_de_desenho)
Tiktik.image = pygame.image.load("Imagens/Tiktik.png")
Tiktik.rect = pygame.Rect(200, 429, 80, 80)

# Display
display = pygame.display.set_mode([1000, 700])  # Cria a janela
pygame.display.set_caption("Hello Kitty Knight")  # Nome da janela

if __name__ == "__main__":
    while Gameloop:
        for evento in pygame.event.get():  # Verifica se a tecla foi apertada
            if evento.type == pygame.QUIT:  # Aqui faz o jogo fechar
                Gameloop = False

        personagem.mover()  # Chama a função para mover o personagem

        grupo_de_desenho.draw(display)  # Desenha tudo na tela
        pygame.display.update()

pygame.quit()
