import pygame

class Background :#배경 클래스
    def __init__(self,screen):
        self.screen = screen
        self.back_img = pygame.image.load("Resource/background.jpg") #첫번째
        self.back_img2 = pygame.image.load("Resource/background.jpg") #두번쨰
        self.y1 = 0
        self.y2 = -960

    def draw(self):#사진을 그린다.
        self.screen.blit(self.back_img, (0,self.y1))
        self.screen.blit(self.back_img2,(0,self.y2))

    def update(self):
        self.y1 += 0.5
        self.y2 += 0.5

        if self.y1 >= 960:
            self.y1 = -960

        if self.y2 >= 960:
            self.y2 = -960
