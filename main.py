import pygame
import os
# from matrix import *
# import math
# import colorsys
# from atr_math
from attractor import Attractor, ODE, generate_attractors
from camera import Rotation, generate_pos, matrix_multiplication
import atr_color
from icecream import ic
import random

#--- Constants ------

os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 1440, 900 
size = (width, height)
white, black = (200, 200, 200), (0, 0, 0)
pygame.init()
pygame.display.set_caption("Lorenz Attractor")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 100
screen.fill(black)
clock.tick(fps)
time = 0.01 #0.009

ode = ODE.lorenz
sigma = 10 #10
rho = 28 #28
beta = 8/3 #8/3
scale = 10
angle = 0#-100
previous = None
run = True
attractor_length_limit = 3 #lowest is 2 as it needs the previous value to calculate
number_of_attractors = 1000

parameters = [beta, rho, sigma]
attractors = generate_attractors(number_of_attractors, parameters, time, ode)




while run:
    screen.fill(black)
    # r = pygame.Rect(0,0,700,700)
    # pygame.draw.rect(screen, (100,100,100), r, 4)
    for attractor in attractors:
        if len(attractor.points) == attractor_length_limit:
            attractor.points.pop(0)
        attractor.next()
        for p in range(len(attractor.points)):
            x_pos, y_pos = generate_pos(angle, attractor.points, p, scale, size)
            # if attractor.previous is not None: # include this line instead of p>0 to view closed attractors "self drawing"
            if p>0:
                # color = atr_color.new(attractor.color)
                # pygame.draw.line(screen, color, (x_pos, y_pos), attractor.previous, 1) #white
                # pygame.draw.circle(screen, color, (x_pos, y_pos), 2)
                pygame.draw.circle(screen, (attractor.color[0], attractor.color[1], attractor.color[2]), (x_pos, y_pos), 1)
                pygame.draw.line(screen, (attractor.color[0], attractor.color[1], attractor.color[2]), (x_pos, y_pos), attractor.previous, 2) #white
            attractor.previous=[x_pos, y_pos]
    angle += 0.005
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
