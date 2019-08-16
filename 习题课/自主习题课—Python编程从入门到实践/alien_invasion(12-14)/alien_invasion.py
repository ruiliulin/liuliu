# 具体游戏内容如下
"""
   在游戏《外星人入侵》中，玩家控制着一艘最初出现在屏幕底部中央的飞船。玩家可以
使用箭头键左右移动飞船，还可以使用空格键进行射击。游戏开始时，一群外星人出现在天
空中，他们在屏幕中向下移动。玩家的任务是射杀这些外星人。玩家将所有外星人都消灭干
净后，将出现一群新的外星人，他们的移动速度更快。只要有外星人撞到了玩家的飞船或到
达了屏幕底部，玩家就损失一艘飞船。玩家损失三艘飞船后，游戏结束

"""
# 开始前请确认安装好pygame


import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    # 创建一艘飞船，一个用于存储子弹的编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()