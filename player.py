import pygame

pygame.init()

class Player :
    def __init__(self,screen):
        self.screen = screen
        self.player_img = pygame.image.load("Resource/player.png")
        self.px = 250
        self.py = 600
        self.right = False #bool 변수로 오른쪽 방향키가 눌렸는지 확인하는 변수
        self.left = False
        self.up = False
        self.down = False
        self.speed = 1
        self.hp_img = pygame.image.load("Resource2/hp.png")
        self.hp = 80
        self.restart_btn = pygame.image.load("Resource2/KakaoTalk_20230616_191948939.png")
        self.life = 3
        self.life_img = pygame.image.load("Resource2/life.png")

    def draw(self):
        if self.hp >= 0:
            if self.right == True:
                self.screen.blit(self.player_img,(self.px,self.py))
            else:
                self.screen.blit(self.player_img,(self.px,self.py))
                self.screen.blit(self.hp_img,(self.px,self.py),(0,0,self.hp,20))
        else:
            self.screen.blit(self.restart_btn,(300,300))

        for i in range(self.life-1):
            self.screen.blit(self.life_img, (448 + i*64 , 0))
           

    def update(self):
        if self.right == True:
            self.px += self.speed
        if self.left == True:
            self.px -= self.speed
        if self.up == True:
            self.py -= self.speed
        if self.down == True:
            self.py += self.speed

        if self.px >= 440:
            self.px = 440
        if self.px <= 0:
            self.px = 0
        if self.py <= 0:
            self.py = 0
        if self.py >= 810:
            self.py = 810

    def animation(self):
        pass
