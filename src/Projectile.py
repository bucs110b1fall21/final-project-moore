import pygame

# Models are called Sprites

# Controller => Sprites => Surface => Rectangle


class Projectile(pygame.sprite.Sprite):

    def __init__(self, limit):
        super().__init__()  # initializes the sprite library
        # required by sprite
        self.image = pygame.image.load('assets/projectile.png').convert_alpha()
        self.rect = self.image.get_rect()  # rectangle
        self.limit = limit
        self.speed = 10

    # hook -
    # update method allows model updates that aren't base on events
    def update(self):
        self.rect.x += self.speed

        # check if we are outside the screen
        if self.rect.x > self.limit:
            self.kill()
