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
def show_instructions():
    instructions = [
        "Welcome to Duck Hunt!",
        "Instructions:",
        "- Move your mouse to aim.",
        "- Click to shoot the duck.",
        "- ESC to quit.",
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
    def countdown():
        for i in range(3, 0, -1):
            screen.fill(Config.BLACK)
            text_surface = font.render(str(i), True, Config.WHITE)
            text_rect = text_surface.get_rect(center=(Config.WIDTH // 2, Config.HEIGHT // 2))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()
            pygame.time.delay(1000)
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

    countdown()
show_instructions()

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

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