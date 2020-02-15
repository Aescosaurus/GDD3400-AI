import pygame
import cm
from vec2 import vec2
from player import player

pygame.init()

screen = pygame.display.set_mode( ( cm.screen_width,cm.screen_height ) )
done = False

player = player( cm.screen_size / 2,cm.player_size,cm.player_speed,cm.player_col )

clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill( cm.bg_color )
	# Logic here
	player.update()
	player.draw( screen )
	# 
	pygame.display.flip()
	clock.tick( cm.frame_rate )