import pygame
from math import *
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
color = pygame.Color('orange')
hsv = color.hsva
running = True
an = 0
x, y = 0, 0
x_end = 1
y_end = 1
dot = 1
color_count = 1
flag = True
while running:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flag = not flag
    screen.fill(pygame.Color('black'))
    pygame.draw.circle(screen, pygame.Color('white'), (width // 2, height // 2), 200, 2)
    if flag:
        color.hsva = ((hsv[0] + color_count)%360, hsv[1], hsv[2], hsv[3])
        color_count += 0.1
        for dot in range(360):
            x = int(cos(radians(dot)) * 200) + height // 2
            y = int(sin(radians(dot)) * 200) + height // 2
            x_end = int(cos(radians((dot*(2+an)) % 360)) * 200) + height // 2
            y_end = int(sin(radians((dot*(2+an)) % 360)) * 200) + height // 2
            pygame.draw.line(screen, color, (x, y), (x_end, y_end), 1)
        an += 0.01
        pygame.display.update()
