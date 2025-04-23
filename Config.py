import pygame

pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
Spawn_Ducks_Event = pygame.USEREVENT + 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

duckSpeeds = {
    "slow": 3,
    "medium": 5,
    "fast": 7
}

shotgun_sound = pygame.mixer.Sound("ShotgunShot.mp3")


