import pygame
import os
from matrix import *
import math
import colorsys
from attractor import Attractor, ODE
from camera import Rotation, matrix_multiplication
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
fps = 200
screen.fill(black)
clock.tick(fps)
time = 0.009 #0.009

ode = ODE.lorenz
sigma = 10
rho = 28
beta = 8/3
x1, y1, z1 = 0.4, 0, 0
x2, y2, z2 = 10, 0.2, 50
x3, y3, z3 = 5, 5, 3
x4, y4, z4 = 1, 5, 5
points1 = []
points2 = []
points3 = []
points4 = []
colors = []
scale = 10
angle = -100
previous = None
run = True


def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))


def generate_pos(angle, points, p):
    rotated_2d = matrix_multiplication(Rotation.y(angle), points[p]) 
    # distance = 1 #0.01
    # val = 1/(distance - rotated_2d[2][0])#z value
    projection_matrix = [[1, 0, 0],
                        [0, 1, 0]]
    projected2d = matrix_multiplication(projection_matrix, rotated_2d)
    projected2d = rotated_2d
    x_pos = int(projected2d[0][0] * scale) + width//2 #+ 100
    y_pos = int(projected2d[1][0] * scale) + height//2
    return x_pos, y_pos



a1 = Attractor(x1, y1, z1, beta, rho, sigma, time, ode)
a2 = Attractor(x2, y2, z2, beta, rho, sigma, time, ode)
a3 = Attractor(x3, y3, z3, beta, rho, sigma, time, ode)
a4 = Attractor(x4, y4, z4, beta, rho, sigma, time, ode)

while run:
    screen.fill(black)
    a1.next()
    # ic(points1)
    # ic(a1.points)
    # a1.next()
    a2.next()
    a3.next()
    a4.next()
    # points2 = a2.next()
    # points3 = a3.next()
    # points4 = a4.next()
    # if len(points1) == 250:
    #     a1.points.pop(0)
    #     a2.points.pop(0)
    #     a3.points.pop(0)
    #     a4.points.pop(0)


    # for p in range(int(len(points1)/2),len(points1)):
    for p in range(len(a1.points)):
        x_pos1, y_pos1 = generate_pos(angle, a1.points, p)
        x_pos2, y_pos2 = generate_pos(angle, a2.points, p)
        x_pos3, y_pos3 = generate_pos(angle, a3.points, p)
        x_pos4, y_pos4 = generate_pos(angle, a4.points, p)
        # x_pos2, y_pos2 = generate_pos(angle, points2, p)

        if p > 1:
            pygame.draw.line(screen, (255,255,255), (x_pos1, y_pos1), previous1, 1) #white
            pygame.draw.line(screen, (200,140,0), (x_pos2, y_pos2), previous2, 1) #gold
            pygame.draw.line(screen, (0,60,200), (x_pos3, y_pos3), previous3, 1) #blue
            pygame.draw.line(screen, (255,222,0), (x_pos4, y_pos4), previous4, 1) #pink


            # pygame.draw.circle(screen, (0,255,255) , (x_pos1, y_pos1), 3) #(hsv2rgb(hue, 1, 1)) 
        previous1 = (x_pos1, y_pos1)
        previous2 = (x_pos2, y_pos2)
        previous3 = (x_pos3, y_pos3)
        previous4 = (x_pos4, y_pos4)

    angle += 0.005
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
