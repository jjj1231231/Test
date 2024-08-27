import pygame
import background
import player
import enemy
import Boss
import bullet
import item
import button
import sound
import point

pygame.init()
clock = pygame.time.Clock()

class Stage2:
    def __init__(self, screen):
        self.screen = screen
        self.po = point.Point(screen)
        self.bg = background.Background(screen)
        self.pl = player.Player(screen)

        self.mobs = []
        self.bo = Boss.Boss(screen)
        self.mobs.append(self.bo)

        for i in range(6):
            self.mobs.append(enemy.Enemy(screen, self.pl))

        self.so = sound.Sound(screen)
        self.bu = bullet.Bullet(screen, self.mobs, self.so, self.po)
        self.it = item.item(screen, self.pl, self.bu)
        self.clear = False

    def play_scene(self):
        self.so.playBgm()
        while True:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse_pos[0] <= 410 and 300 <= mouse_pos[1] <= 360:
                        self.pl.hp = 80
                        self.pl.life -= 1
                         
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT: 
                        self.pl.right = True
                    if event.key == pygame.K_LEFT: 
                        self.pl.left = True
                    if event.key == pygame.K_UP: 
                        self.pl.up = True
                    if event.key == pygame.K_DOWN: 
                        self.pl.down = True
                    if event.key == pygame.K_a: 
                        self.pl.attack = True
                    if event.key == pygame.K_s:
                        self.bu.bullet.append([self.pl.px, self.pl.py])
                        self.so.playShot()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.pl.right = False
                    if event.key == pygame.K_LEFT:
                        self.pl.left = False
                    if event.key == pygame.K_UP:
                        self.pl.up = False
                    if event.key == pygame.K_DOWN:
                        self.pl.down = False

            self.bg.draw()
            self.bg.update()
            self.pl.draw()
            self.pl.update()
            self.pl.animation()
           
            for i, mob in enumerate(self.mobs):
                if self.mobs[i].e_cnt >= 150:
                    self.mobs[i].bx = 1000
                    self.mobs[i].by = 1000
                    del self.mobs[i]
                    self.clear = True
                    return 1
                else:
                    mob.draw()
                    mob.update()
                    mob.animation()
               
            self.bu.draw()
            self.bu.update()
            self.it.draw()
            self.it.update()

            self.po.draw_score()
            if self.pl.life == 1 and self.pl.hp <= 0:
                self.bg.back_img = pygame.image.load("Resource2/background8.jpg")
                self.bg.back_img2 = pygame.image.load("Resource2/background8.jpg")
                self.start = False
                return 1

            clock.tick(144)
            pygame.display.update()

    def gameOver(self):
        time = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            time += 0.1
            self.bg.draw()        
            self.screen.blit(gameOver_img, (0, 0))

            if time >= 20:
                self.start = True
                self.pl.hp = 80
                self.pl.life = 3
                return 1
            
            clock.tick(144)
            pygame.display.update()
