import pygame
import random
import Config

class Ducks:
    def __init__(self):
        self.type = random.choice(list(Config.duckSpeeds.keys()))
        self.speed = Config.duckSpeeds[self.type]
        self.sprite = pygame.image.load("flyingDUCK.png").convert_alpha()
        self.rect = self.sprite.get_rect()
        self.spawn_sound = pygame.mixer.Sound("DuckQuack.mp3")
        self.direction = random.randint(1, 5)
        min = 0.1
        max = 0.9
        self.angle = random.uniform(min, max)

    def duckMove(self):
        if self.direction == 1:
            self.rect.move_ip(0, -self.speed)
        if self.direction == 2:
            self.rect.move_ip(self.speed, -self.speed)
        if self.direction == 3:
            self.rect.move_ip(-self.speed, -self.speed)
        if self.direction == 4:
            self.rect.move_ip(self.speed * self.angle, -self.speed)
        if self.direction == 5:
            self.rect.move_ip(-self.speed, -self.speed * self.angle)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)