import pygame
import random

# Constantes do jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLAYER_SPEED = 5
GRAVITY = 1
JUMP_STRENGTH = 15
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_SPEED = 3
GOAL_WIDTH = 50
GOAL_HEIGHT = 50
BULLET_WIDTH = 10
BULLET_HEIGHT = 5
BULLET_SPEED = 10
FPS = 60

# Classe para o jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x

        # Colisão com as bordas da tela
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.y += self.change_y

        # Colisão com as plataformas
        self.collide_platforms()

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += GRAVITY

        # Verificar se o jogador está no chão
        if self.rect.y >= SCREEN_HEIGHT - PLAYER_HEIGHT and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT

    def jump(self):
        # Verificar se o jogador está no chão ou em uma plataforma
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, self.platforms, False)
        self.rect.y -= 2
        if hits or self.rect.y >= SCREEN_HEIGHT - PLAYER_HEIGHT:
            self.change_y = -JUMP_STRENGTH

    def go_left(self):
        self.change_x = -PLAYER_SPEED

    def go_right(self):
        self.change_x = PLAYER_SPEED

    def stop(self):
        self.change_x = 0

    def collide_platforms(self):
        hits = pygame.sprite.spritecollide(self, self.platforms, False)
        if hits:
            for platform in hits:
                if self.change_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.change_y = 0

# Classe para as plataformas
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([PLATFORM_WIDTH, PLATFORM_HEIGHT])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Classe para os inimigos voadores
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([ENEMY_WIDTH, ENEMY_HEIGHT])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = ENEMY_SPEED

    def update(self):
        self.rect.x += self.change_x

        # Inverter direção ao atingir as bordas
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.change_x *= -1

# Classe para os projéteis
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BULLET_WIDTH, BULLET_HEIGHT])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += BULLET_SPEED
        if self.rect.x > SCREEN_WIDTH:
            self.kill()

# Classe para a meta
class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([GOAL_WIDTH, GOAL_HEIGHT])
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Classe para o jogo
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jogo de Plataforma")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.player = Player()
        self.player.platforms = self.platforms
        self.all_sprites.add(self.player)
        self.level = 1
        self.create_level()

    def create_level(self):
        # Limpar sprites
        self.all_sprites.empty()
        self.platforms.empty()
        self.enemies.empty()
        self.bullets.empty()
        self.goals.empty()

        # Re-adicionar o jogador
        self.all_sprites.add(self.player)
        self.player.rect.x = SCREEN_WIDTH // 2
        self.player.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT

        if self.level == 1:
            self.create_platforms_level1()
            self.create_enemies_level1()
            self.create_goal_level1()
        elif self.level == 2:
            self.create_platforms_level2()
            self.create_enemies_level2()
            self.create_goal_level2()

    def create_platforms_level1(self):
        # Criação de plataformas para o nível 1
        platforms = [
            (0, SCREEN_HEIGHT - 40),
            (200, SCREEN_HEIGHT - 150),
            (400, SCREEN_HEIGHT - 300),
            (600, SCREEN_HEIGHT - 450)
        ]
        for platform in platforms:
            p = Platform(platform[0], platform[1])
            self.all_sprites.add(p)
            self.platforms.add(p)

    def create_enemies_level1(self):
        # Criação de inimigos voadores para o nível 1
        enemies = [
            (100, 100),
            (400, 200),
            (700, 300)
        ]
        for enemy in enemies:
            e = Enemy(enemy[0], enemy[1])
            self.all_sprites.add(e)
            self.enemies.add(e)

    def create_goal_level1(self):
        # Criação da meta para o nível 1
        goal = Goal(SCREEN_WIDTH - GOAL_WIDTH, SCREEN_HEIGHT - GOAL_HEIGHT - 10)
        self.all_sprites.add(goal)
        self.goals.add(goal)

    def create_platforms_level2(self):
        # Criação de plataformas para o nível 2
        platforms = [
            (0, SCREEN_HEIGHT - 40),
            (300, SCREEN_HEIGHT - 150),
            (100, SCREEN_HEIGHT - 300),
            (500, SCREEN_HEIGHT - 450)
        ]
        for platform in platforms:
            p = Platform(platform[0], platform[1])
            self.all_sprites.add(p)
            self.platforms.add(p)

    def create_enemies_level2(self):
        # Criação de inimigos voadores para o nível 2
        enemies = [
            (200, 150),
            (500, 250),
            (300, 350)
        ]
        for enemy in enemies:
            e = Enemy(enemy[0], enemy[1])
            self.all_sprites.add(e)
            self.enemies.add(e)

    def create_goal_level2(self):
        # Criação da meta para o nível 2
        goal = Goal(SCREEN_WIDTH - GOAL_WIDTH, 10)
        self.all_sprites.add(goal)
        self.goals.add(goal)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.go_left()
                    if event.key == pygame.K_RIGHT:
                        self.player.go_right()
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                    if event.key == pygame.K_z:
                        self.shoot_bullet()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.player.change_x < 0:
                        self.player.stop()
                    if event.key == pygame.K_RIGHT and self.player.change_x > 0:
                        self.player.stop()

            self.all_sprites.update()

            # Verificar colisões entre o jogador e os inimigos
            if pygame.sprite.spritecollide(self.player, self.enemies, False):
                print("Game Over!")
                running = False

            # Verificar colisões entre projéteis e inimigos
            for bullet in self.bullets:
                enemy_hits = pygame.sprite.spritecollide(bullet, self.enemies, True)
                if enemy_hits:
                    bullet.kill()

            # Verificar se o jogador atingiu a meta
            if pygame.sprite.spritecollide(self.player, self.goals, True):
                if self.level == 1:
                    self.level = 2
                    self.create_level()
                else:
                    print("You Win!")
                    running = False

            self.screen.fill((255, 255, 255))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    def shoot_bullet(self):
        bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

# Execução do jogo
if __name__ == "__main__":
    game = Game()
    game.run()
