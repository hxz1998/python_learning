import sys

import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
import game_function as gf

def run_game():
	# 初始化整个游戏对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# 创建一个飞船
	ship = Ship(ai_settings, screen)

	# 创建一个用于存储子弹的编组
	bullets = Group()
	
	# 游戏主循环
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()