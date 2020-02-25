import pygame
import cm
from vec2 import vec2
from dog import dog
from sheep import sheep
import random

pygame.init()

gfx = pygame.display.set_mode( ( cm.screen_width,cm.screen_height ) )
done = False

sheep_bucket_pos = 0

player = dog( cm.screen_size / 2,cm.player_spd,cm.wolf_spr )
sheepies = []
for i in range( cm.sheep_count ):
	rand_pos = vec2( random.uniform( 0,cm.screen_width ),
		random.uniform( 0,cm.screen_height ) )
	sheepies.append( sheep( rand_pos,cm.enemy_spd,cm.sheep_spr ) )

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
		# s.update_ai( player,sheepies )
		s.draw( gfx )

	for i in range( sheep_bucket_pos,min( cm.sheep_count,sheep_bucket_pos + cm.sheep_bucket_size ) ):
		sheepies[i].update_ai( player,sheepies )
	sheep_bucket_pos += cm.sheep_bucket_size
	if sheep_bucket_pos > cm.sheep_count - 1:
		sheep_bucket_pos = 0
	# 
	pygame.display.flip()
	clock.tick( cm.frame_rate )