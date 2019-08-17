# 12-2 游戏角色
import sys
import pygame

screen = pygame.display.set_mode((1200, 800))
screen.fill((230, 230, 230))

class TuPian():

    def __init__(self):
        self.screen = screen

        self.tupian = pygame.image.load("tupian/ship.bmp")
        self.rect = self.tupian.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.tupian, self.rect)


tupian = TuPian()
tupian.blitme()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()




    pygame.display.flip()