import pygame
import random
import Config

class Ducks:
    def __init__(self):
        self.type = random.choice(list(Config.duckSpeeds.keys()))
        self.speed = Config.duckSpeeds[self.type]
        self.sprite1 = pygame.image.load(Config.duck1).convert_alpha()
        self.sprite2 = pygame.image.load(Config.duck2).convert_alpha()
        self.sprite = self.sprite1
        self.rect = self.sprite.get_rect()
        self.spawn_sound = pygame.mixer.Sound(Config.quack)
        self.direction = random.randint(1, 5)
        self.angle = random.uniform(0.1, 0.9)
        self.animation_timer = 0
        self.interval = 200

    def update_animation(self, time):
        if time - self.animation_timer > self.interval:
            self.sprite = self.sprite2 if self.sprite == self.sprite1 else self.sprite1
            self.animation_timer = time

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

    def draw(self, surface, time):
        self.update_animation(time)
        surface.blit(self.sprite, self.rect)