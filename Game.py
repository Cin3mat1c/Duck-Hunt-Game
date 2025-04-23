import pygame
import sys
import Ducks
import Config

pygame.init()

screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
pygame.display.set_caption("Duck spawns")


background = pygame.image.load("backgroundDUCK3.png").convert()
flying_duck = pygame.image.load("flyingDUCK.png").convert_alpha()
rock = pygame.transform.scale(pygame.image.load("DUCKGAMErock.png").convert_alpha(), (120, 120))
shrub = pygame.transform.scale(pygame.image.load("DUCKGAMEshrub.png").convert_alpha(), (150, 100))
bush = pygame.transform.scale(pygame.image.load("DUCKGAMEbush.png").convert_alpha(), (180, 100))



rock_pos = (250, 350)
shrub_pos = (450, 480)
bush_pos = (100, 450)

spawns = [(250,350), (450,480), (100,450)]

mouseRect = pygame.Rect(0, 0, 12, 12)

collisionCounter = 0

ducks = []

clock = pygame.time.Clock()

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

spawn_index = 0
def duck_spawn():
    global spawn_index
    if spawn_index < len(spawns):
        x, y = spawns[spawn_index]
        ducks.append({'x':x, 'y':y})
        spawn_index += 1
spawning = pygame.USEREVENT + 1
pygame.time.set_timer(spawning, 2000)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawning:
            duck_spawn()


    screen.blit(background, (0, 0))
    for duck in ducks:
        duckRect = pygame.Rect(0, 0, duck['x'], duck['y'])
        screen.blit(flying_duck, (duck['x'], duck['y']))
        if duckRect.top > Config.HEIGHT:
            ducks.remove(duck)
        if mouseRect.colliderect(duckRect) and pygame.mouse.get_pressed()[0]:
            collisionCounter += 1
            duckRect = pygame.Rect(0, 0, 0, 0)
            ducks.remove(duck)


        mousePOS = pygame.mouse.get_pos()
        mouseRect.center = (mousePOS)

    scoreText = font.render(f"Score: {collisionCounter}", True, Config.WHITE)
    text_rect1 = scoreText.get_rect()

    screen.blit(rock, rock_pos)
    screen.blit(shrub, shrub_pos)
    screen.blit(bush, bush_pos)
    screen.blit(scoreText, text_rect1)


    pygame.display.update()

    clock.tick(Config.FPS)

pygame.quit()
sys.exit()