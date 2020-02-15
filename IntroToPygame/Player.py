from vec2 import vec2
import pygame

class player:
	def __init__( self,pos,vel,size ):
		self.pos = pos
		self.vel = vel
		self.size = size

	def draw( self,gfx ):
		pygame.draw.rect( gfx,( 255,20,20 ),
			pygame.Rect( self.pos.x,self.pos.y,
			self.size.x,self.size.y ) )

	def update( self ):
		move = vec2.zero()
		if pygame.key.get_pressed()[pygame.K_w]: move.y -= 1
		if pygame.key.get_pressed()[pygame.K_s]: move.y += 1
		if pygame.key.get_pressed()[pygame.K_a]: move.x -= 1
		if pygame.key.get_pressed()[pygame.K_d]: move.x += 1

		self.vel = move.normalize()
		self.pos += self.vel