import pygame
import random

# Models are called Sprites

# Controller => Sprites => Surface => Rectangle


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # initializes the sprite library
        self.health = 3
        self.direction = 'R'
        # required by sprite
        self.image = pygame.image.load('assets/hero.png').convert_alpha()
        self.rect = self.image.get_rect()  # rectangle
        self.rect.inflate_ip(-25, -25)
        self.speed = 10
        self.rect.x = 10
        self.rect.y = 10

    def move(self, direction):
        if direction == "U":
            self.rect.y -= self.speed
        elif direction == "D":
            self.rect.y += self.speed
        elif direction == "L":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def fight(self, opponent):
        # 50% chance of winning
        return not bool(random.randrange(3))
