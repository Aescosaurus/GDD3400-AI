import pygame
import cm
from vec2 import vec2
from player import player
from enemy import enemy

pygame.init()

gfx = pygame.display.set_mode( ( cm.screen_width,cm.screen_height ) )
done = False

player = player( cm.screen_size / 2,cm.player_size,cm.player_spd,cm.player_col )
enemy = enemy( vec2( 100,100 ),cm.enemy_size,cm.enemy_spd,cm.enemy_col )

clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	gfx.fill( cm.bg_color )
	# Logic here
	player.update()
	player.draw( gfx )
	
	enemy.update( player )
	enemy.draw( gfx )
	# 
	pygame.display.flip()
	clock.tick( cm.frame_rate )