import pygame
import sys
import Config 

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
pygame.display.set_caption("Duck Hunt")

pygame.time.set_timer(Config.Spawn_Ducks_Event, 1000)

mouseRect = pygame.Rect(0, 0, 12, 12)

duckRect = pygame.Rect(375, 275, 50, 50)
duckSurf = pygame.Surface(duckRect.size)
duckSurf.fill(Config.RED)

ducks = []

clock = pygame.time.Clock()

collisionCounter = 0
Lives = 3

font = pygame.font.SysFont("timesnewroman", 24)

background = pygame.image.load().convert()

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

        screen.blit(background, (0, 0))

        if mouseRect.colliderect(duckRect) and pygame.mouse.get_pressed()[0]:
            collisionCounter += 1
            duckRect = pygame.Rect(0, 0, 0, 0)
            duckSurf = pygame.Surface(duckRect.size)
            pygame.draw.rect(screen, (0, 0, 0), duckRect)

        mousePOS = pygame.mouse.get_pos()
        mouseRect.center = (mousePOS)

        scoreText = font.render(f"Score: {collisionCounter}", True, Config.WHITE)
        text_rect1 = scoreText.get_rect()

        livesText = font.render(f"Lives: {Lives}", True, Config.WHITE)
        text_rect2 = livesText.get_rect()

        screen.fill(Config.BLACK)
        screen.blit(duckSurf, duckRect)
        screen.blit(scoreText, text_rect1)
        screen.blit(livesText, text_rect2)
        pygame.display.flip()


        clock.tick(Config.FPS)
