import pygame
import random

pygame.init()

class Enemy:
    def __init__(self, screen, pl):
        self.screen = screen
        self.player = pl
        self.enemy_img = [
            pygame.image.load("Resource/enemy0.png"),
            pygame.image.load("Resource/enemy1.png"),
            pygame.image.load("Resource/enemy2.png")
        ]
        self.ex = random.randrange(0, 291)
        self.ey = random.randrange(-2000, -500)
        self.i = random.randrange(0, 3)
        self.dead = False
        self.b = False
        self.hp = 100
        self.e_cnt = 0

    def draw(self):
        self.screen.blit(self.enemy_img[self.i], (self.ex, self.ey))

    def update(self):
        self.ey += 1.5
        
        if self.ey >= 960:
            self.reset()

        if self.ex <= self.player.px <= self.ex + 350:
            if self.ey <= self.player.py <= self.ey + 217:
                self.player.hp -= 10
                self.ex = random.randrange(0, 291)
                self.ey = random.randrange(-2000, -500)
                self.i = random.randrange(0, 3)
                self.hp = 50

    def reset(self):
        self.ex = random.randrange(0, 291)
        self.ey = random.randrange(-2000, -500)
        self.i = random.randrange(0, 3)
        self.hp = 50

    def animation(self):
        pass
