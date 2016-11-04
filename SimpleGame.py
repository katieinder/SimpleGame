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
Ball = pygame.image.load("Ball.png")
#get size
BALL_SIZE=[22,22]

Magnet = pygame.image.load("Magnet.png")
MAGNET_SIZE = [100,25]

#define x and y
x,y = 0, 0

#define x and y directions
x_direction, y_direction = 1, 1

#main game loop

while 1:

    clock.tick(60)

    screen.fill([250,250,250])

    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()

    screen.blit(Ball, (x,y))
    screen.blit(Magnet, (350,275))

    x += 2*x_direction
    y += 2*y_direction

    if x + BALL_SIZE[0] > 800 or x <= 0:
        x_direction *= -1
    if y + BALL_SIZE[1] > 600 or y <= 0:
        y_direction *=-1

    if x + BALL_SIZE[0] >= 300 or 300 <= x <= 400:
        x_direction *= -1

    if y + BALL_SIZE[1] >= 250 or 250 <= y <= 275:
        y_direction *= -1



    pygame.display.update()
