import pygame

class Menu(pygame.sprite.Sprite):
    def __init__(self, menu):
        super().__init__(menu)
        self.__menu = True

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, value):
        self.__menu = value

        

    def draw(self, display):        
        fonte = pygame.font.Font(None, 36)
        header = fonte.render("Hello Kitty Knight", True, (255, 255, 255))
        texto = fonte.render("Enter para novo jogo", True, (255, 255, 255))
        save = fonte.render("(S) para continuar", True, (255, 255, 255))
        display.blit(header, (350, 150))  # Posição e texto
        display.blit(texto, (320, 300))  # Posição e texto
        display.blit(save, (450, 450))  # Posição e texto
        


    def inicia_jogo(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] :
            #print("teste")
            return True
        
    def inicia_saves(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] :
            #print("teste")
            return True 
    


               
       

