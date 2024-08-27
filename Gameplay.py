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
import stage2

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode( (640,960) )
pygame.display.set_caption("MyFist Game")

po = point.Point(screen)
bg = background.Background(screen)
pl = player.Player(screen)

mobs = []
bo = Boss.Boss(screen)
mobs.append(bo)

for i in range(6):
    mobs.append(enemy.Enemy(screen,pl))

btn = button.Button(screen)
so = sound.Sound(screen)
bu = bullet.Bullet(screen,mobs,so,po)
it = item.item(screen,pl,bu)
gameOver_img = pygame.image.load("Resource2/KakaoTalk_20230616_192017558_01.png")
gameClear_img = pygame.image.load("Resource2/KakaoTalk_20230616_192017558.png") 
global start
start = True

stg2 = stage2.Stage2(screen)

global clear
clear = False

def intro_scene():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= mouse_pos[0] <= 540:
                    if 150 <= mouse_pos[1] <= 325:
                        bg.back_img = pygame.image.load("Resource/background0.jpg")
                        bg.back_img2 = pygame.image.load("Resource/background0.jpg")
                        return 1;
                if 150 <= mouse_pos[0] <= 540:
                    if 150 <= mouse_pos[1] <= 525:
                        pygame.quit()

                
        bg.draw()                
        btn.draw()
        pygame.display.update()


def play_scene():
    so.playBgm()
    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <=mouse_pos[0]<= 410:
                 if 300 <=mouse_pos[1] <= 360:
                     pl.hp = 80
                     pl.life -= 1
                     
            if event.type ==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT : 
                    pl.right = True
                if event.key == pygame.K_LEFT : 
                    pl.left = True
                if event.key == pygame.K_UP : 
                    pl.up = True
                if event.key == pygame.K_DOWN : 
                    pl.down = True
                if event.key == pygame.K_a : 
                    pl.attack = True
                if event.key == pygame.K_s:
                    bu.bullet.append([pl.px,pl.py])
                    so.playShot()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    pl.right = False
                if event.key == pygame.K_LEFT:
                    pl.left = False
                if event.key == pygame.K_UP:
                    pl.up = False
                if event.key == pygame.K_DOWN:
                    pl.down = False


        bg.draw()
        bg.update()
        pl.draw()
        pl.update()
        pl.animation()

       
        for i, mob in enumerate(mobs):
            if mobs[i].e_cnt >=150:
               mobs[i].bx = 1000
               mobs[i].by = 1000
               del mobs[i]
               stg2.play_scene()
            
               return 1

            else:
                mob.draw()
                mob.update()
                mob.animation()
           
        bu.draw()
        bu.update()
        it.draw()
        it.update()

        po.draw_score()
        if pl.life == 1 and pl.hp<=0:
            bg.back_img=pygame.image.load("Resource2/background8.jpg")
            bg.back_img2=pygame.image.load("Resource2/background8.jpg")
            start = False
            return 1

        clock.tick(144)
        pygame.display.update()
        
def gameOver():
    time = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        time += 0.1
        bg.draw()        
        screen.blit(gameOver_img,(0,0))

        if time >= 20:
            start = True
            pl.hp = 80
            pl.life = 3
            return 1
        pygame.display.update()
             
def gameClear():

     while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    bo = Boss.Boss(screen)
                    mobs.append(bo)
                    return 1

        bg.draw()
        screen.blit(gameClear_img,(0,0))    
        clock.tick(144)
        pygame.display.update()
        
while True:
    if start == True:
        intro_scene()
        play_scene()
    if stg2.clear == True:
        gameClear()
    else:
        gameOver()
