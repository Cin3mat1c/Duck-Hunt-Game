import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


mouseRect = pygame.Rect(0, 0, 12, 12)
mouseSurf = pygame.Surface(mouseRect.size)
mouseSurf.fill((0, 255, 0))


duckRect = pygame.Rect(375, 275, 50, 50)
duckSurf = pygame.Surface(duckRect.size)
duckSurf.fill((255, 0, 0))

clock = pygame.time.Clock()

collisionCounter = 0

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

        if mouseRect.colliderect(duckRect) and pygame.mouse.get_pressed()[0]:
            collisionCounter += 1
            print(collisionCounter)

        mousePOS = pygame.mouse.get_pos()
        mouseRect.center = (mousePOS)


        screen.fill((0, 0, 0))
        screen.blit(duckSurf, duckRect)
        pygame.draw.rect(screen, (0, 255, 0), mouseRect)
        pygame.display.flip()


        clock.tick(60)
