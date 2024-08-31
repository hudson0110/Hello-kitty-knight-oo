import pygame
from hello_kitty import HelloKitty
from Tiktik import Tiktik
from Abelha import Abelha
from mapa import Mapa

pygame.init()

Gameloop = True

grupo_de_desenho = pygame.sprite.Group()

# Cria os objetos
mapa = Mapa(grupo_de_desenho)
personagem = HelloKitty(grupo_de_desenho)
tiktik = Tiktik(grupo_de_desenho, 200, 429)
abelha = Abelha(grupo_de_desenho, 300, 150, personagem)  # Passa Hello Kitty como alvo

# Display
display = pygame.display.set_mode([1000, 700])
pygame.display.set_caption("Hello Kitty Knight")

if __name__ == "__main__":
    plataformas = mapa.plataformas
    
    while Gameloop:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                Gameloop = False

        personagem.mover(plataformas)
        tiktik.mover_tiktik()
        abelha.mover_abelha()
        
        grupo_de_desenho.update()  # Atualiza todos os sprites no grupo
        display.fill((0, 0, 0))
        grupo_de_desenho.draw(display)
        pygame.display.update()

pygame.quit()
