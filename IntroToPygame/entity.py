import pygame
from vec2 import vec2

class entity:
	def __init__( self,pos,size,spd,col ):
		self.pos = pos
		self.size = vec2( size,size )
		self.spd = spd
		self.col = col
		self.center = self.pos + self.size / 2

	def update( self ):
		self.center = self.pos + self.size / 2
	
	def draw( self,gfx ):
		pygame.draw.rect( gfx,self.col,
			pygame.Rect( self.pos.x,self.pos.y,
			self.size.x,self.size.y ) )
	
	def __str__( self ):
		return( "pos: " + self.pos + " vel: " + self.vel +
			" center: " + self.center )