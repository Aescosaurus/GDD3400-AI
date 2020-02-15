from vec2 import vec2
import pygame
from entity import entity

class player( entity ):
	def __init__( self,pos,size,spd,col ):
		super().__init__( pos,size,spd,col )
		self.vel = vec2.zero()

	def update( self ):
		super().update()

		move = vec2.zero()
		if pygame.key.get_pressed()[pygame.K_w]: move.y -= 1
		if pygame.key.get_pressed()[pygame.K_s]: move.y += 1
		if pygame.key.get_pressed()[pygame.K_a]: move.x -= 1
		if pygame.key.get_pressed()[pygame.K_d]: move.x += 1

		self.vel = move.normalize()
		self.pos += self.vel * self.spd

	def draw( self,gfx ):
		super().draw( gfx )

		pygame.draw.line( gfx,( 0,0,255 ),self.center.get(),
			( self.center + self.vel * 50.0 ).get() )