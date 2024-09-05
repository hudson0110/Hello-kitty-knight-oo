import pygame
from Plataforma import Plataforma  # Importe a classe Plataforma

class Menu(pygame.sprite.Sprite):
    def __init__(self, menu):
        super().__init__(menu)
        self.menu = True
        

    def draw(self, display):        
        fonte = pygame.font.Font(None, 36)
        header = fonte.render("Hello Kitty Knight", True, (255, 255, 255))
        texto = fonte.render("Pressine Enter para começar", True, (255, 255, 255))
        save = fonte.render("Pressine Enter para começar", True, (255, 255, 255))
        display.blit(header, (350, 150))  # Posição e texto
        display.blit(texto, (320, 300))  # Posição e texto
        display.blit(save, (320, 450))  # Posição e texto
        


    def interage_menu(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] :
            print("nolas")
            return True
                
               
       
