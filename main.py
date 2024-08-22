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
'''
# plataforma_1
plataforma_1 = pygame.sprite.Sprite(grupo_de_desenho)
plataforma_1.image = pygame.Surface([500, 20])
plataforma_1.image.fill((255, 0, 0))  # Cor vermelha para a plataforma_1
plataforma_1.rect = pygame.Rect(160, 462, 500, 20)

# Plataforma_2
plataforma_2 = pygame.sprite.Sprite(grupo_de_desenho)
plataforma_2.image = pygame.Surface([245, 20])
plataforma_2.image.fill((255, 0, 0))  # Cor vermelha para a plataforma_2
plataforma_2.rect = pygame.Rect(350, 334, 245, 20)

# Plataforma_3
plataforma_3 = pygame.sprite.Sprite(grupo_de_desenho)
plataforma_3.image = pygame.Surface([130, 20])
plataforma_3.image.fill((255, 0, 0))  # Cor vermelha para a plataforma_3
plataforma_3.rect = pygame.Rect(742, 243, 130, 20)

# Plataforma_4
plataforma_4 = pygame.sprite.Sprite(grupo_de_desenho)
plataforma_4.image = pygame.Surface([1000, 20])
plataforma_4.image.fill((255, 0, 0))  # Cor vermelha para a plataforma_3
plataforma_4.rect = pygame.Rect(0, 618, 1000, 20)
'''
# Plataformas invisíveis
plataforma_1 = pygame.sprite.Sprite()
plataforma_1.rect = pygame.Rect(160, 462, 500, 20)  # Posição e tamanho da plataforma_1

plataforma_2 = pygame.sprite.Sprite()
plataforma_2.rect = pygame.Rect(350, 334, 245, 20)  # Posição e tamanho da plataforma_2

plataforma_3 = pygame.sprite.Sprite()
plataforma_3.rect = pygame.Rect(742, 243, 130, 20)  # Posição e tamanho da plataforma_3

plataforma_4 = pygame.sprite.Sprite()
plataforma_4.rect = pygame.Rect(0, 618, 1000, 20)  # Posição e tamanho da plataforma_3



# Cria o personagem
personagem = HelloKitty(grupo_de_desenho)

# INIMIGO
Tiktik = pygame.sprite.Sprite(grupo_de_desenho)
Tiktik.image = pygame.image.load("Imagens/Tiktik.png")
Tiktik.rect = pygame.Rect(200, 429, 80, 80)

#

# Display
display = pygame.display.set_mode([1000, 700])  # Cria a janela
pygame.display.set_caption("Hello Kitty Knight")  # Nome da janela

if __name__ == "__main__":
    plataformas = [plataforma_1, plataforma_2, plataforma_3, plataforma_4]  # Adicione as plataformas em uma lista
    
    while Gameloop:
        for evento in pygame.event.get():  # Verifica se a tecla foi apertada
            if evento.type == pygame.QUIT:  # Aqui faz o jogo fechar
                Gameloop = False

        personagem.mover(plataformas)  # Chama a função para mover o personagem, passando as plataformas

        grupo_de_desenho.draw(display)  # Desenha tudo na tela
        pygame.display.update()

pygame.quit()
