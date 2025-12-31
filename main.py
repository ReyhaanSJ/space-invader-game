import math
import random
import pygame

SW=800
SH=500
PSX=370
PSY=380
ESYMIN=50
ESYMAX=150
ESX=4
ESY=40
BSY=10
CD=27

pygame.init()

screen=pygame.display.set_mode((SW,SH))
backround=pygame.image.load('backround.png')

pygame.display.set_caption("Space Invader")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg=pygame.image.load('player.png')
playerX=PSX
playerY=PSY
playerX_change=0

enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,SW-64))
    enemyX.append(random.randint(ESYMIN,ESYMAX))
    enemyX_change.append(ESX)
    enemyY_change.append(ESY)

bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=PSY
bulletX_change=0
bulletY_change=BSY
bullet_state="ready"

score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

over_font=pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score=font.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(playerImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((enemyX-bulletX)**2 + (enemyY-bulletY)**2)
    return distance < CD

