'''This code will first will be testing how a particle will react to magnetic field'''

'''Version three of code will test out vector algebra of magnetic field and velocity'''

import pygame, sys      #import pygame
import numpy as np

pygame.init()      #initialise pygame

screen_size = [800, 600] #define screen size

screen = pygame.display.set_mode(screen_size) #open window

pygame.mouse.set_visible(0)  #make mouse invisible

clock = pygame.time.Clock() #initialise clock

BALL = pygame.image.load("Ball.png").convert_alpha()  #load image of ball
BALL.set_colorkey([255,255,255])                        #set background to white
MAGNET= pygame.image.load("Magnet.png").convert_alpha() #load image of magnet
MAGNET.set_colorkey([255,255,255])

BALL_SIZE = [22, 22]
MAGNET_SIZE = [100, 25]

x, y = 0, 0         #define x and y

x_direction, y_direction = 1, 1   #define x and y directions

p1, p2 = 350, 275       #define position of magnet

#move_x, move_y = 0, 0

#main game loop
while 1:

    clock.tick(60)

    screen.fill([255,255,255])       #set background to white

    screen.blit(BALL, (x, y))        #put images on screen
    screen.blit(MAGNET, (p1, p2))

    '''for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()     #if close pressed then quit game


        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d and p1 + MAGNET_SIZE[0] < 800:
                move_x += 6
            else:
                move_x = 0
            if event.key==pygame.K_a and p1>0:
                move_x -= 6
            if event.key==pygame.K_s and p2 + MAGNET_SIZE[1] < 600:
                move_y += 6
            else:
                move_y = 0
            if event.key==pygame.K_w and p2 > 0:
                move_y -= 6
            if event.key==pygame.K_SPACE:
                ROT_MAG = pygame.transform.rotate(MAGNET, 45)
                screen.blit(ROT_MAG, (p1,p2))
                #angle = (angle + 45) % 360
                #rot_MAG=rotate45(MAGNET (p1,p2))
                #screen.blit(rot_MAG, (p1,p2))
                #screen.blit(pygame.transform.rotate((MAGNET, angle), (p1,p1)))
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_d:
                move_x = 0
            if event.key==pygame.K_a:
                move_x = 0
            if event.key==pygame.K_w:
                move_y = 0
            if event.key==pygame.K_s:
                move_y = 0'''

    x += 1.5*x_direction              #set velocity of ball
    y += 1.5*y_direction

    #p1 += move_x
    #p2 += move_y

    #stop ball going off screen
    if x + BALL_SIZE[0] >= 800 or x <= 0:
        x_direction *= -1
    if y + BALL_SIZE[1] >= 600 or y <= 0:
        y_direction *= -1

    '''#collision with magnet
    if p1 <= x + BALL_SIZE[0] <= p1 + MAGNET_SIZE[0] and p2 -MAGNET_SIZE[1] <= y <= p2 or p1 <= x + BALL_SIZE[0] <= p1 +MAGNET_SIZE[0] and p2 - MAGNET_SIZE[1] <= y -BALL_SIZE[1] <= p2:
        x_direction *= 1
        y_direction *= -1
    elif p1 <= x <= p1 +MAGNET_SIZE[0] and p2 -MAGNET_SIZE[1] <= y <= p2 or p1 <= x <= p1 +MAGNET_SIZE[0] and p2 - MAGNET_SIZE[1] <= y -BALL_SIZE[1] <= p2:
        x_direction *= 1
        y_direction *= -1'''

    # above and to left
    if x + BALL_SIZE[0] < p1 and y < p2:
        x_distance = p1 - (x + BALL_SIZE[0])
        y_distance = p2 - (y + BALL_SIZE[1])
        distance = np.sqrt(x_distance**2 + y_distance**2)
        if 0<=distance<=10:
            V_vect=np.array([x_direction,y_direction])
            B_vect=np.array([-1,3])
            F=1*np.cross(V_vect,B_vect)
            a=F/1
            vnew=V_vect+ a
            x_direction = vnew[0]
            y_direction = vnew[1]
    # above
    elif p1 <= x <= p1 + MAGNET_SIZE[0] and y < p2:
        x_distance = 0
        y_distance = p2 - (y + BALL_SIZE[1])
        distance = np.sqrt(x_distance**2 + y_distance**2)
        if 0 <= distance <= 10:
            V_vect = np.array([x_direction, y_direction])
            B_vect = np.array([-1, 3])
            F = 1 * np.cross(V_vect, B_vect)
            a = F / 1
            vnew = V_vect + a
            x_direction = vnew[0]
            y_direction = vnew[1]
    # below
    elif p1 <= x <= p1 + MAGNET_SIZE[0] and y > p2 + MAGNET_SIZE[1]:
        x_distance = 0
        y_distance = y - p2 + MAGNET_SIZE[1]
        distance = np.sqrt(x_distance**2 + y_distance**2)
        if 0 <= distance <= 10:
            V = np.array([x_direction, y_direction])
            B = np.array([-1, 3])
            F = 1 * np.cross(V, B)
            a = F / 1
            vnew = V + a
            x_direction = vnew[0]
            y_direction = vnew[1]
    # left and below
    elif x + BALL_SIZE[0] < p1 and y > p2 + MAGNET_SIZE[1]:
        x_distance = p1 - (x + BALL_SIZE[0])
        y_distance = y - p2 + MAGNET_SIZE[1]
        distance = np.sqrt(x_distance**2 + y_distance**2)
        if 0 <= distance <= 10:
            V = np.array([x_direction, y_direction])
            B = np.array([-1, 3])
            F = 1 * np.cross(V, B)
            a = F / 1
            vnew = V + a
            x_direction = vnew[0]
            y_direction = vnew[1]
    #left
    elif x + BALL_SIZE[0] < p1 and p2 + MAGNET_SIZE[1] <= y <= p2:
        x_distance = p1 - (x + BALL_SIZE[0])
        y_distance = 0
        distance = np.sqrt(x_distance**2 + y_distance**2)
        if 0 <= distance <= 10:
            V = np.array([x_direction, y_direction])
            B = np.array([-1, 3])
            F = 1 * np.cross(V, B)
            a = F / 1
            vnew = V + a
            x_direction = vnew[0]
            y_direction = vnew[1]
    #right
    elif p1 + MAGNET_SIZE[0] < x  and p2 + MAGNET_SIZE[1] <= y <= p2:
        x_distance = p1 + MAGNET_SIZE[0] - x
        y_distance = 0
        distance = np.sqrt(x_distance**2 + y_distance**2)
        if 0 <= distance <= 10:
            V = np.array([x_direction, y_direction])
            B = np.array([-1, 3])
            F = 1 * np.cross(V, B)
            a = F / 1
            vnew = V + a
            x_direction = vnew[0]
            y_direction = vnew[1]
    # right and above
    elif p1 + MAGNET_SIZE[0] < x and y < p2:
        x_distance = p1 + MAGNET_SIZE[0] - x
        y_distance = p2 - (y + BALL_SIZE[1])
        distance = np.sqrt(x_distance**2 + y_distance**2)
        if 0 <= distance <= 10:
            V = np.array([x_direction, y_direction])
            B = np.array([-1, 3])
            F = 1 * np.cross(V, B)
            a = F / 1
            vnew = V + a
            x_direction = vnew[0]
            y_direction = vnew[1]

    #right and below
    else:
        x_distance = p1 + MAGNET_SIZE[0] - x
        y_distance = y - p2 + MAGNET_SIZE[1]
        distance = np.sqrt(x_distance**2 + y_distance**2)
        if 0 <= distance <= 10:
            V = np.array([x_direction, y_direction])
            B = np.array([-1, 3])
            F = 1 * np.cross(V, B)
            a = F / 1
            vnew = V + a
            x_direction = vnew[0]
            y_direction = vnew[1]



    pygame.display.update()         #update screen