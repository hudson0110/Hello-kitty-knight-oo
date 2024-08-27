import pygame
from hello_kitty import HelloKitty
from Tiktik import Tiktik
from Abelha import Abelha
from mapa import Mapa


pygame.init()

# Display
display = pygame.display.set_mode([1000, 700])  # Cria a janela
pygame.display.set_caption("Hello Kitty Knight")  # Nome da janela

Gameloop = True

grupo_de_desenho = pygame.sprite.Group()  # Cria um grupo com minhas sprites

# Cria os objetos
mapa = Mapa(grupo_de_desenho)
personagem = HelloKitty(grupo_de_desenho)
tiktik = Tiktik(grupo_de_desenho, 200, 429)
abelha = Abelha(grupo_de_desenho, 300, 150)




if __name__ == "__main__":
 
    while Gameloop:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                Gameloop = False

        personagem.mover(mapa.plataformas)  # Chama a função para mover o personagem
        tiktik.mover_tiktik()  # Movimento do Tiktik
        abelha.mover_abelha()

        display.fill((0, 0, 0))  # Limpa a tela (opcional)
        grupo_de_desenho.draw(display)
        pygame.display.update()

pygame.quit()
