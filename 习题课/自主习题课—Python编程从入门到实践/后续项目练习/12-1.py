# 12-1 蓝色天空
import sys
import pygame


screen = pygame.display.set_mode((1200, 800))
screen.fill((0, 0, 255))
tupian = TuPian(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.flip()

