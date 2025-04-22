import pygame
import random
import Config

class duck():
    def __init__(self):
        self.type = random.choice(list(Config.duckSpeeds.keys()))
        self.speed = Config.duckSpeeds[self.type]
        sprite_path = Config.duckSprites[self.type]
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.sprite.get_rect()

    def duckMove(self):
        move = random.randint(1, 3)
        if move == 1:
            self.rect.move(0, self.speed)
        if move == 2:
            self.rect.move(self.speed, self.speed)
        if move == 3:
            self.rect.move(-self.speed, self.speed)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)