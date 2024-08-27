import pygame

pygame.init()

class Button:
    def __init__ (self,screen):
        self.screen = screen
        self.start_img = pygame.image.load("Resource2/start.png")
        self.exit_img = pygame.image.load("Resource2/exit.png")
        self.rule_img = pygame.image.load("Resource2/rule.png")
        self.rank_img = pygame.image.load("Resource2/ranking.png")


    def draw(self):
        self.screen.blit(self.start_img,(150,150))
        self.screen.blit(self.exit_img,(150,350))
        self.screen.blit(self.rule_img,(150,550))
        self.screen.blit(self.rank_img,(150,720))



    
