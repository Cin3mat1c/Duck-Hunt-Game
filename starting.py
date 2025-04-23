import pygame
import sys
import Config

pygame.init()
screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
pygame.display.set_caption("Duck Hunt")
font = pygame.font.SysFont("timesnewroman", 24)

def show_instructions():
    instructions = [
        "Welcome to Duck Hunt!",
        "Instructions:",
        "- Move your mouse to aim.",
        "- Click to shoot the ducks.",
        "- You can shoot 6 times before reloading.",
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
