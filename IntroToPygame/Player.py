from vec2 import vec2
import pygame
from agent import agent

class player( agent ):
	def __init__( self,pos,spd,img ):
		super().__init__( pos,spd,img )
		self.spd = self.accel

	def update( self ):
		super().update()

		move = vec2.zero()

		if pygame.key.get_pressed()[pygame.K_w]: move.y -= 1
		if pygame.key.get_pressed()[pygame.K_s]: move.y += 1
		if pygame.key.get_pressed()[pygame.K_a]: move.x -= 1
		if pygame.key.get_pressed()[pygame.K_d]: move.x += 1

		if move != vec2.zero():
			self.vel = move.normalize()
			self.spd = self.accel
		else:
			self.spd = 0.0