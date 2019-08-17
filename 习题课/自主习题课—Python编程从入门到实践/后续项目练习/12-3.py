# 12-3 火箭
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

        self.move_right = False
        self.move_left = False
        self.move_top = False
        self.move_bottom = False

    def move(self):
        if self.move_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.move_left == True and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1
        if self.move_top == True and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1
        if self.move_bottom == True and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        self.screen.blit(self.tupian, self.rect)

    def check_keydown_events(self):
        if event.key == pygame.K_a:
            self.move_left = True
        elif event.key == pygame.K_d:
            self.move_right = True
        elif event.key == pygame.K_w:
            self.move_top = True
        elif event.key == pygame.K_s:
            self.move_bottom = True

    def check_keyup_events(self):
        if event.key == pygame.K_a:
            self.move_left = False
        elif event.key == pygame.K_d:
            self.move_right = False
        elif event.key == pygame.K_w:
            self.move_top =  False
        elif event.key == pygame.K_s:
            self.move_bottom = False

tupian = TuPian()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            tupian.check_keydown_events()
        elif event.type == pygame.KEYUP:
            tupian.check_keyup_events()
    tupian.move()
    screen.fill((230, 230, 230))
    tupian.blitme()
    pygame.display.flip()




