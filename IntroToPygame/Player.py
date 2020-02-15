from Vector import Vector
import pygame

class Player:
	def __init__( self,pos,vel,size ):
		self.pos = pos
		self.vel = vel
		self.size = size

	def draw( self,gfx ):
		pygame.draw.rect( gfx,( 255,20,20 ),
			pygame.Rect( self.pos.x,self.pos.y,
			self.size.x,self.size.y ) )

	def update( self ):
		move = Vector( 0,0 )
		if pygame.key.get_pressed()[pygame.K_UP]: move.y -= 1
		if pygame.key.get_pressed()[pygame.K_DOWN]: move.y += 1
		if pygame.key.get_pressed()[pygame.K_LEFT]: move.x -= 1
		if pygame.key.get_pressed()[pygame.K_RIGHT]: move.x += 1

		self.vel = move.normalize()
		self.pos += self.vel