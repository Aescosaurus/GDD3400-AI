import pygame
import cm
from vec2 import vec2
from dog import dog
from sheep import sheep
import random

pygame.init()

gfx = pygame.display.set_mode( ( cm.screen_width,cm.screen_height ) )
done = False

player = dog( cm.screen_size / 2,cm.player_size,cm.player_spd,cm.player_col )
sheepies = []
for i in range( 10 ):
	rand_pos = vec2( random.uniform( 0,cm.screen_width ),
		random.uniform( 0,cm.screen_height ) )
	sheepies.append( sheep( rand_pos,cm.enemy_size,cm.enemy_spd,cm.enemy_col ) )

clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	gfx.fill( cm.bg_color )
	# Logic here
	player.update()
	player.draw( gfx )
	
	for s in sheepies:
		s.update( player )
		s.draw( gfx )
	# 
	pygame.display.flip()
	clock.tick( cm.frame_rate )