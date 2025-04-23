import pygame
import random
import Config

class Ducks:
    def __init__(self):
        self.type = random.choice(list(Config.duckSpeeds.keys()))
        self.speed = random.randint(3, 7)
        self.sprite = pygame.image.load("flyingDUCK.png").convert_alpha()
        self.rect = self.sprite.get_rect()
        self.spawn_sound = pygame.mixer.Sound("DuckQuack.mp3")
        self.direction = random.randint(1, 3)

    def duckMove(self):
        if self.direction == 1:
            self.rect.move_ip(0, -self.speed)
        if self.direction == 2:
            self.rect.move_ip(self.speed, -self.speed)
        if self.direction == 3:
            self.rect.move_ip(-self.speed, -self.speed)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)