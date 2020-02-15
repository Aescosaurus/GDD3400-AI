import pygame
import cm
from vec2 import vec2
from player import player
from enemy import enemy
from enemy_hunter import enemy_hunter
import random

pygame.init()

gfx = pygame.display.set_mode( ( cm.screen_width,cm.screen_height ) )
done = False

player = player( cm.screen_size / 2,cm.player_size,cm.player_spd,cm.player_col )
enemies = []
for i in range( 5 ):
	rand_pos = vec2( random.uniform( 0,cm.screen_width ),
		random.uniform( 0,cm.screen_height ) )
	enemies.append( enemy( rand_pos,cm.enemy_size,cm.enemy_spd,cm.enemy_col ) )
for i in range( 5 ):
	rand_pos = vec2( random.uniform( 0,cm.screen_width ),
		random.uniform( 0,cm.screen_height ) )
	enemies.append( enemy( rand_pos,cm.enemy_size,cm.enemy_spd,cm.enemy_hunter_col ) )

clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	gfx.fill( cm.bg_color )
	# Logic here
	player.update()
	player.draw( gfx )
	
	# enemy.update( player )
	# enemy.draw( gfx )
	for e in enemies:
		e.update( player )
		e.draw( gfx )
	# 
	pygame.display.flip()
	clock.tick( cm.frame_rate )