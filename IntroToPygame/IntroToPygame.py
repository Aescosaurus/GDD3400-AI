import pygame
from Vector import Vector
from Player import Player

pygame.init()

screen = pygame.display.set_mode( ( 800,600 ) )
done = False

player = Player( Vector( 50,50 ),Vector( 0,0 ),Vector( 30,30 ) )

clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill( ( 100,149,237 ) )
	# Logic here
	player.update()
	player.draw( screen )
	# 
	pygame.display.flip()
	clock.tick( 60.0 )