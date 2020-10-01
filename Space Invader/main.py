import pygame
import random
import math
from pygame import mixer

#initializing pygame
pygame.init()


#setting screen
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")

#background image and music
background=pygame.image.load('spaceBG.png')
mixer.music.load('background.wav')
mixer.music.play(-1)

#setting player
playerImg=pygame.image.load('player.png')
playerX=370
playerY=480
playerXchange=0

#setting Bullet
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletXchange=0
bulletYchange=2.5
bullet_state="ready"

#setting enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyXchange=[]
enemyYchange=[]
num_of_enemies=5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyXchange.append(1.25)
    enemyYchange.append(30)
    

#displaying Score
score=0
font=pygame.font.Font('freesansbold.ttf',32)
game_over_font=pygame.font.Font('freesansbold.ttf',64)
textX=10
textY=10


def show_score(x,y):
    score_value=font.render("Score : "+str(score),True,(255,255,255))
    screen.blit(score_value,(x,y))

#a func to show specific user score
def show_vicky(x,y):
    score_value=font.render("Score : "+str(score),True,(255,255,255))
    screen.blit(score_value,(x,y))

def show_game_over():
    over_text=game_over_font.render("Game Over !!",True,(255,255,255))
    screen.blit(over_text,(200,250))
    pygame.QUIT


def display_player(x,y):
    screen.blit(playerImg,(x,y))

#display particulat user
def display_vicky(x,y):
    screen.blit(playerImg,(x,y))

def display_enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))


def is_Collision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(bulletX-enemyX,2)+math.pow(bulletY-enemyY,2))
    if distance<27:
        return True
    else:
        return False

running=True

#game loop
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerXchange=-2
            if event.key==pygame.K_RIGHT:
                playerXchange=2
            if event.key==pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound=mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX=playerX
                    fire_bullet(playerX,bulletY)
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerXchange=0
        
        
    
    playerX+=playerXchange

    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736

    for i in range(num_of_enemies):
        if enemyY[i]>430:
            for j in range(num_of_enemies):
                enemyY[j]==2000
            show_game_over()
            break

        enemyX[i]+=enemyXchange[i]
        if enemyX[i]<=0:
            enemyXchange[i]=1.5
            enemyY[i]+=enemyYchange[i]
        elif enemyX[i]>=736:
            enemyXchange[i]=-1.5
            enemyY[i]+=enemyYchange[i]

        collision=is_Collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound=mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY=480
            bullet_state="ready"
            score+=1
            #print(score)
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)
        
        display_enemy(enemyX[i],enemyY[i],i)


    if bulletY<=0:
        bulletY=480
        bullet_state="ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletYchange

    
    show_score(textX,textY)
    display_player(playerX,playerY)
    pygame.display.update()