'''This code will create a very simplistic game with no classes
It will be the basis of which I will improve on'''

#import pygame
import pygame, sys
#initialise pygame
pygame.init()

from GameObject import *

#set the height and width of screen
SCREEN_SIZE = [800,600]
#open screen
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Very Simple Game")

#hide mouse
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

#load resources
Ball = pygame.image.load("Ball.png").convert_alpha()
#get size
BALL_SIZE=[22,22]

Magnet = pygame.image.load("Magnet.png").convert_alpha()
MAGNET_SIZE = [100,25]

Target = pygame.image.load("Target.png").convert_alpha()
TARGET_SIZE=[25,25]

#define x and y
x,y = 0, 0

#define x and y directions
x_direction, y_direction = 1, 1

#define position of magnet
p1=350
p2=275

#define position of target
pos1=700
pos2=200

myriadProFont=pygame.font.SysFont("Myriad Pro", 48)
Text=myriadProFont.render("YOU WIN",1,(250,250,250),(250,250,250))

#main game loop

while 1:

    clock.tick(60)

    screen.fill([250,250,250])

    screen.blit(Ball, (x, y))
    screen.blit(Magnet, (p1, p2))
    screen.blit(Target, (pos1,pos2))


    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT and p1+MAGNET_SIZE[0]<=800:
                p1 += 20
            if event.key==pygame.K_LEFT and p1>0:
                p1 -=20
            if event.key==pygame.K_UP and p2+MAGNET_SIZE[1]<600:
                p2 -=20
            if event.key==pygame.K_DOWN and p2>0:
                p2 +=20
            if event.key==pygame.K_SPACE:
                pass


    x += 2*x_direction
    y += 2*y_direction

    if x + BALL_SIZE[0] > 800 or x <= 0:
        x_direction *= -1
    if y + BALL_SIZE[1] > 600 or y <= 0:
        y_direction *=-1


    #collision code
    if x > (p1-MAGNET_SIZE[0]/2) and x < (p1+MAGNET_SIZE[0]/2) or (x+BALL_SIZE[0]) > (p1-MAGNET_SIZE[0]/2) and (x+BALL_SIZE[0]) < (p1+MAGNET_SIZE[0]/2):
        x_direction *= -1
        if y > (p2-MAGNET_SIZE[1]/2) and y < (p2+MAGNET_SIZE[1]/2) and y+BALL_SIZE[1] > (p2-MAGNET_SIZE[1]/2) and y+BALL_SIZE[1]< (p2+MAGNET_SIZE[1]/2):
            y_direction *= -1

    if x > (pos1-TARGET_SIZE[0]/2) and x < (pos1+TARGET_SIZE[0]/2) or (x+BALL_SIZE[0]) > (pos1-TARGET_SIZE[0]/2) and (x+BALL_SIZE[0]) < (pos1+TARGET_SIZE[0]/2):
        if y > (pos2-TARGET_SIZE[1]/2) and y < (pos2+TARGET_SIZE[1]/2) and y+BALL_SIZE[1] > (pos2-TARGET_SIZE[1]/2) and y+BALL_SIZE[1]< (pos2+TARGET_SIZE[1]/2):
            screen.fill([0,0,0])
            screen.blit(Text, (400,300))




    pygame.display.update()
