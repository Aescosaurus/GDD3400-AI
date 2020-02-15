from vec2 import vec2
import pygame

class player:
	def __init__( self,pos,size,spd,col ):
		self.pos = pos
		self.size = size
		self.speed = spd
		self.vel = vec2.zero()
		self.center = pos + vec2.one() * ( size / 2 )
		self.color = col

	def update( self ):
		move = vec2.zero()
		if pygame.key.get_pressed()[pygame.K_w]: move.y -= 1
		if pygame.key.get_pressed()[pygame.K_s]: move.y += 1
		if pygame.key.get_pressed()[pygame.K_a]: move.x -= 1
		if pygame.key.get_pressed()[pygame.K_d]: move.x += 1

		self.vel = move.normalize()
		self.pos += self.vel * self.speed
		self.center = self.pos + vec2.one() * ( self.size / 2 )

	def draw( self,gfx ):
		pygame.draw.rect( gfx,self.color,
			pygame.Rect( self.pos.x,self.pos.y,
			self.size,self.size ) )

		pygame.draw.line( gfx,( 0,0,255 ),self.center.get(),
			( self.center + self.vel * 50.0 ).get() )

	def __str__( self ):
		return( "pos: " + self.pos + " vel: " + self.vel +
			" center: " + self.center )