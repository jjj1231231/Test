import pygame
import random


pygame.init()

class Bullet:
    def __init__(self, screen, mobs, sound, point):
        self.screen = screen
        self.mobs = mobs
        self.sound = sound
        self.point = point
        self.bullet_img = pygame.image.load("Resource2/bu/bullet.png")
        self.bullet = []
        self.isShot = False
        self.b=False
        

    def draw(self):
        if len(self.bullet) != 0:
            for self.x, self.y in self.bullet:
                self.screen.blit(self.bullet_img, (self.x, self.y))

    def update(self):
        if len(self.bullet) != 0:
            for self.i, self.bxy in enumerate(self.bullet):
                self.bxy[1] -= 10
                self.bullet[self.i][1] = self.bxy[1]

            for enemy in self.mobs:
                if enemy.b == False:
                    if enemy.ex <= self.bxy[0] <= enemy.ex + 350:
                        if enemy.ey <= self.bxy[1] <= enemy.ey + 217:
                            enemy.ex = random.randrange(0, 291)
                            enemy.ex = random.randrange(-2000,-1000)
                            enemy.i = random.randrange(0,3)
                                                
                else:
                    if enemy.bx <= self.bxy[0]<= enemy.bx+350:
                        if enemy.by <= self.bxy[1] <= enemy.by +217:
                            self.isShot = True

                    if self.isShot == True:
                            enemy.hp -=10

                            if enemy.hp <=0: 
                             enemy.dead = True
                             self.sound.playBoom()
                    
