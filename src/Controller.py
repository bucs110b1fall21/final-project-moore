from src import Player
from src import Enemy
from src import Projectile

import pygame
import random


class Controller:

    def __init__(self):
        # setup pygame data
        self.window_width = 900
        self.window_height = 600
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.Surface((self.window_width, self.window_height))
        self.background.fill((250, 250, 250))

        # held keys act like repeated strike
        pygame.key.set_repeat(50, 500)

        self.player = Player.Player()
        self.enemies = pygame.sprite.Group()
        for e in range(3):
            self.enemies.add(Enemy.Enemy(self.window_width, self.window_height))

        self.projectiles = pygame.sprite.Group()
        # cast existing groups to a tuple to add them together with other sprites and make a new group
        self.all_sprites = pygame.sprite.Group(tuple(self.enemies) + (self.player,))

    def mainloop(self):
        while True:  # one time through the loop is one frame (picture)
            # check for events
            self.eventloop()

            # update models
            self.enemies.update()
            self.projectiles.update()

            # collisions
            fight = pygame.sprite.spritecollide(self.player, self.enemies, False)
            if fight:
                for enemy in fight:
                    if self.player.fight(enemy):
                        enemy.kill()
                    else:
                        self.player.health -= 1

            fight = pygame.sprite.groupcollide(self.enemies, self.projectiles, False, True)
            if fight:
                for enemy in fight:
                    enemy.pause()

            # redraw
            self.screen.blit(self.background, (0, 0))
            # end the program
            if self.player.health == 0:
                return
            self.all_sprites.draw(self.screen)
            self.projectiles.draw(self.screen)

            # update the screen
            pygame.display.flip()

    # OPTIONAL: put the event loop in a seperate method just to break up the mainloop()
    def eventloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move("U")
                if event.key == pygame.K_DOWN:
                    self.player.move("D")
                if event.key == pygame.K_LEFT:
                    self.player.move("L")
                if event.key == pygame.K_RIGHT:
                    self.player.move("R")
                if event.key == pygame.K_SPACE:
                    if len(self.projectiles.sprites()) <= 5:
                        p = Projectile.Projectile(self.window_width)
                        pos = self.player.rect.midright
                        p.rect.x = pos[0]
                        p.rect.y = pos[1]
                        self.projectiles.add(p)
                    else:
                        print("can't shoot", len(self.projectiles.sprites()))
