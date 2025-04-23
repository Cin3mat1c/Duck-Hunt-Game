import pygame
import sys
from Ducks import Ducks
import Config
import random

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
pygame.display.set_caption("Duck spawns")


background = pygame.image.load("backgroundDUCK3.png").convert()
rock = pygame.transform.scale(pygame.image.load("DUCKGAMErock.png").convert_alpha(), (120, 120))
shrub = pygame.transform.scale(pygame.image.load("DUCKGAMEshrub.png").convert_alpha(), (150, 100))
bush = pygame.transform.scale(pygame.image.load("DUCKGAMEbush.png").convert_alpha(), (180, 100))

rock_pos = (250, 350)
shrub_pos = (450, 480)
bush_pos = (100, 450)

spawns = [(250,350), (450,480), (100,450)]

mouseRect = pygame.Rect(0, 0, 1, 1)

collisionCounter = 0
Lives = 3
game_over = False

ducks = []

clock = pygame.time.Clock()

font = pygame.font.SysFont("timesnewroman", 24)
def show_instructions():
    instructions = [
        "Welcome to Duck Hunt!",
        "Instructions:",
        "- Move your mouse to aim.",
        "- Click to shoot the ducks.",
        "- Don't let 3 ducks escape!",
        "",
        "Press any key to start..."
    ]
    screen.fill(Config.BLACK)
    for i, line in enumerate(instructions):
        text_surface = font.render(line, True, Config.WHITE)
        screen.blit(text_surface, (50, 50 + i * 30))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def countdown():
    for i in range(3, 0, -1):
        screen.fill(Config.BLACK)
        text_surface = font.render(str(i), True, Config.WHITE)
        text_rect = text_surface.get_rect(center=(Config.WIDTH // 2, Config.HEIGHT // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.delay(1000)

show_instructions()
countdown()

spawning = pygame.USEREVENT + 1
pygame.time.set_timer(spawning, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawning:
            duck = Ducks()
            x, y = random.choice(spawns)  # Random spawn location from the 3
            duck.rect.topleft = (x, y)  # Set position
            ducks.append(duck)
            duck.spawn_sound.play()

    screen.blit(background, (0, 0))

    mousePOS = pygame.mouse.get_pos()
    mouseRect.center = (mousePOS)

    for duck in ducks[:]:
        duck.draw(screen)
        duck.duckMove()
        if (duck.rect.top > Config.HEIGHT or
                duck.rect.bottom < 0 or
                duck.rect.left > Config.WIDTH or
                duck.rect.right < 0):
            ducks.remove(duck)
            Lives -= 1
            if Lives <= 0:
                game_over = True
                running = False
        if mouseRect.colliderect(duck.rect) and pygame.mouse.get_pressed()[0]:
            collisionCounter += 1
            Config.shotgun_sound.play()
            ducks.remove(duck)

    if game_over:
        screen.fill(Config.BLACK)
        game_over_text = font.render("Game Over", True, Config.RED)
        text_rect = game_over_text.get_rect(center=(Config.WIDTH // 2, Config.HEIGHT // 2))
        screen.blit(game_over_text, text_rect)
        pygame.display.flip()
        pygame.time.delay(3000)


    scoreText = font.render(f"Score: {collisionCounter}", True, Config.WHITE)
    text_rect1 = scoreText.get_rect()

    livesText = font.render(f"Lives: {Lives}", True, Config.WHITE)
    lives_rect = livesText.get_rect(topright=(Config.WIDTH - 10, 10))
    screen.blit(livesText, lives_rect)

    screen.blit(rock, rock_pos)
    screen.blit(shrub, shrub_pos)
    screen.blit(bush, bush_pos)
    screen.blit(scoreText, text_rect1)

    pygame.display.update()

    clock.tick(Config.FPS)

pygame.quit()
sys.exit()