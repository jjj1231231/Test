import pygame
import random

pygame.init()

class Boss :
    def __init__(self,screen):
        self.screen = screen
        self.boss_img = [pygame.image.load("Resource2/boss_/boss0.png"),
                         pygame.image.load("Resource2/boss_/boss1.png"),
                         pygame.image.load("Resource2/boss_/boss2.png"),
                         pygame.image.load("Resource2/boss_/boss3.png"),
                         pygame.image.load("Resource2/boss_/boss4.png"),
                         pygame.image.load("Resource2/boss_/boss5.png"),
                         pygame.image.load("Resource2/boss_/boss6.png"),
                         pygame.image.load("Resource2/boss_/boss7.png")]

        self.dead_img = [pygame.image.load("Resource2/effect/effect_0.png"),
                         pygame.image.load("Resource2/effect/effect_1.png"),
                         pygame.image.load("Resource2/effect/effect_2.png"),
                         pygame.image.load("Resource2/effect/effect_3.png"),
                         pygame.image.load("Resource2/effect/effect_4.png"),
                         pygame.image.load("Resource2/effect/effect_5.png"),
                         pygame.image.load("Resource2/effect/effect_6.png"),
                         pygame.image.load("Resource2/effect/effect_7.png"),
                         pygame.image.load("Resource2/effect/effect_8.png"),
                         pygame.image.load("Resource2/effect/effect_9.png")]


        self.bx = 150
        self.by = 50
        self.std_cnt = 0

        self.left = True
        self.right = False

        self.hp_img = pygame.image.load("Resource2/hp.png")
        self.hp_img2 = pygame.image.load("Resource2/hp_bar.png")

        self.hp = 30
        self.dead = False

        self.dead_cnt = 0
        self.e_cnt = 0

        self.b = True
    def draw(self):
        if self.dead == False:
            self.screen.blit(self.boss_img[self.std_cnt // 5],(self.bx,self.by))
            self.screen.blit(self.hp_img2,(self.bx,self.by-20),(0,0,350,30))
            self.screen.blit(self.hp_img,(self.bx, self.by-20),(0,0,self.hp,30))

        else:
            if self.e_cnt <= 150 :
                self.screen.blit(self.dead_img[self.dead_cnt // 5] , (self.bx , self.by))

            self.e_cnt += 1

    def animation(self):
        self.std_cnt += 1
        if self.std_cnt == 39:
            self.std_cnt = 0

        self.dead_cnt +=1
        if self.dead_cnt == 49:
            self.dead_cnt = 0
            

    def update(self):
        if self.bx > 0 and self.left == True:
            self.bx -= 0.5
            if self.bx <= 0:
                self.left = False
                self.right = True
                self.by = random.randrange(0,300)
        if self.right == True and self.bx < 290:
            self.bx += 0.5
            if self.bx >= 290:
                self.right = False
                self.left = True
                self.by = random.randrange(0,300)
