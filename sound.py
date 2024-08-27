import pygame

pygame.init()

class Sound:
    def __init__(self, screen):
        self.screen = screen
        self.shot = pygame.mixer.Sound("sound/shot.wav")
        self.bgm = pygame.mixer.music.load("sound/bgm.mp3")
        self.hit = pygame.mixer.Sound("sound/hit.wav")
        self.boom = pygame.mixer.Sound("sound/boom.wav")

    def playBgm(self):
        pygame.mixer.music.play()
        
    def playShot(self):
        self.shot.play()

    def playHit(self):
        self.hit.play()

    def playBoom(self):
        self.boom.play()
