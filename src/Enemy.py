import pygame
import random
# Models are called Sprites

# Controller => Sprites => Surface => Rectangle


class Enemy(pygame.sprite.Sprite):

    def __init__(self, start_range, range):
        super().__init__()  # initializes the sprite library
        # required by sprite
        self.image = pygame.image.load('assets/enemy.png').convert_alpha()
        self.rect = self.image.get_rect()  # rectangle
        self.rect.x = random.randrange(start_range - (start_range * .50), start_range - 50)
        self.rect.y = random.randrange(0, 300)
        self.dir = 'U'
        self.range = range
        self.paused = 0

    def pause(self):
        self.paused = 50  # number of frames enemy will be paused
    # hook -
    # update method allows model updates that aren't base on events

    def update(self):
        if self.paused > 0:
            self.paused -= 1
        else:
            if self.rect.y >= self.range:
                self.rect.y -= 1
                self.dir = 'U'
            elif self.rect.y <= 0:
                self.rect.y += 1
                self.dir = 'D'
            else:
                if self.dir == 'U':
                    self.rect.y -= 1
                else:
                    self.rect.y += 1
