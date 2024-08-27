import pygame
import random

pygame.init()

class item:
    def __init__(self, screen, player, bullet):
        self.screen = screen
        self.player = player
        self.bullet = bullet

        self.item_img = pygame.image.load("Resource2/speed.png")
        self.item_img2 = pygame.image.load("Resource2/missile.png")

        self.ix = random.randrange(0, 300)
        self.iy = random.randrange(0, 300)

        self.ix2 = random.randrange(0, 300)
        self.iy2 = random.randrange(0, 300)

        self.item_s = False
        self.item_m = False

    def draw(self):
        if not self.item_s:
            self.screen.blit(self.item_img, (self.ix, self.iy))

        if not self.item_m:
            self.screen.blit(self.item_img2, (self.ix2, self.iy2))

    def update(self):
        self.iy += 3
        self.iy2 += 3

        if self.iy >= 960:
            self.iy = random.randrange(-500, -300)
            self.ix = random.randrange(0, 600)

        if self.ix <= self.player.px + 70 <= self.ix + 130:
            if self.iy <= self.player.py + 70 <= self.iy + 130:
                self.item_s = True
                self.player.speed = 6

        if self.iy2 >= 960:
            self.iy2 = random.randrange(-500, -300)
            self.ix2 = random.randrange(0, 600)

        if self.ix2 <= self.player.px + 70 <= self.ix2 + 130:
            if self.iy2 <= self.player.py + 70 <= self.iy2 + 130:
                self.item_m = True
                self.bullet.bullet_img = pygame.image.load("Resource2/bu/bullet2.png")
                self.bullet.speed = 10
