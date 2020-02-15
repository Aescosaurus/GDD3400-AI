import pygame
import constants
from vec2 import vec2
from player import player

pygame.init()

screen = pygame.display.set_mode( ( constants.screen_width,constants.screen_height ) )
done = False

player = player( vec2( 50,50 ),vec2( 0,0 ),vec2( 30,30 ) )

clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill( constants.bg_color )
	# Logic here
	player.update()
	player.draw( screen )
	# 
	pygame.display.flip()
	clock.tick( constants.frame_rate )