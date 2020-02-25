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
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1: cm.sheep_vel_line = not cm.sheep_vel_line
			if event.key == pygame.K_2: cm.dog_force_line = not cm.dog_force_line
			if event.key == pygame.K_3: cm.bound_force_line = not cm.bound_force_line
			if event.key == pygame.K_4: cm.show_frens = not cm.show_frens
			if event.key == pygame.K_5: cm.bound_box = not cm.bound_box
			if event.key == pygame.K_6: cm.enable_dog_force = not cm.enable_dog_force
			if event.key == pygame.K_7: cm.enable_align_force = not cm.enable_align_force
			if event.key == pygame.K_8: cm.enable_sep_force = not cm.enable_sep_force
			if event.key == pygame.K_9: cm.enable_fren_force = not cm.enable_fren_force
			if event.key == pygame.K_0: cm.enable_bound_force = not cm.enable_bound_force
		if event.type == pygame.QUIT:
			done = True
	gfx.fill( cm.bg_color )
	# Logic here
	if pygame.key.get_pressed()[pygame.K_1]: pass

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