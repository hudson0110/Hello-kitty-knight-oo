import pygame
from hello_kitty import HelloKitty
from Tiktik import Tiktik

pygame.init()

Gameloop = True

grupo_de_desenho = pygame.sprite.Group()  # Cria um grupo com minhas sprites

# MAPA

fundo = pygame.sprite.Sprite(grupo_de_desenho)
fundo.image = pygame.image.load("Imagens/Fundo.jpg")  # Adiciona o fundo
fundo.image = pygame.transform.scale(fundo.image, [1000, 700])
fundo.rect = pygame.Rect(0, 0, 1000, 700)

# Plataformas invisíveis
plataforma_1 = pygame.sprite.Sprite()
plataforma_1.rect = pygame.Rect(160, 462, 500, 20)  # Posição e tamanho da plataforma_1

plataforma_2 = pygame.sprite.Sprite()
plataforma_2.rect = pygame.Rect(350, 334, 245, 20)  # Posição e tamanho da plataforma_2

plataforma_3 = pygame.sprite.Sprite()
plataforma_3.rect = pygame.Rect(742, 243, 110, 20)  # Posição e tamanho da plataforma_3

plataforma_4 = pygame.sprite.Sprite()
plataforma_4.rect = pygame.Rect(0, 618, 1000, 20)  # Posição e tamanho da plataforma_3

# Cria o personagem
personagem = HelloKitty(grupo_de_desenho)
tiktik = Tiktik(grupo_de_desenho, 200, 429)

# Display
display = pygame.display.set_mode([1000, 700])  # Cria a janela
pygame.display.set_caption("Hello Kitty Knight")  # Nome da janela

if __name__ == "__main__":
    plataformas = [plataforma_1, plataforma_2, plataforma_3, plataforma_4]
    
    while Gameloop:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                Gameloop = False

        personagem.mover(plataformas)  # Chama a função para mover o personagem
        tiktik.mover()  # Movimento do Tiktik

        display.fill((0, 0, 0))  # Limpa a tela (opcional)
        grupo_de_desenho.draw(display)
        pygame.display.update()

pygame.quit()
