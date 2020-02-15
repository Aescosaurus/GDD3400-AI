import pygame
from vec2 import vec2
import numpy as np
import cm

class agent:
	def __init__( self,pos,size,spd,col ):
		self.pos = pos
		self.size = vec2( size,size )
		self.spd = spd
		self.col = col
		self.center = self.pos + self.size / 2
		self.vel = vec2.zero()
		self.hitbox = pygame.Rect( self.pos.x,self.pos.y,self.size.x,self.size.y )

	def update( self ):
		self.pos += self.vel * self.spd
		self.pos.x = np.clip( self.pos.x,0,cm.screen_width - self.size.x )
		self.pos.y = np.clip( self.pos.y,0,cm.screen_height - self.size.y )

		self.center = self.pos + self.size / 2
		self.hitbox.move_ip( self.pos.x - self.hitbox.x,
			self.pos.y - self.hitbox.y )
	
	def draw( self,gfx,draw_col = -1 ):
		if draw_col == -1: draw_col = self.col
		pygame.draw.rect( gfx,draw_col,self.hitbox )

		pygame.draw.line( gfx,( 0,0,255 ),self.center.get(),
			( self.center + self.vel * self.spd * 10.0 ).get() )

	# Go directly towards target in a straight line.
	def seek( self,target ):
		diff = target - self.pos
		self.vel = diff.normalize()
		return( target )

	# Go away from target in a straight line.
	def flee( self,target ):
		diff = target - self.pos
		self.vel = -diff.normalize()
		return( target )

	# Anticipate where target will be and go there.
	def pursue( self,target ):
		diff = target.pos - self.pos
		travel_time = diff.get_len() / target.spd
		future_pos = target.pos + target.vel * target.spd * travel_time

		self.seek( future_pos )

		return( future_pos )
	
	def __str__( self ):
		return( "pos: " + str( self.pos ) + " size: " + str( self.size ) +
			" vel: " + str( self.vel ) + " center: " + str( self.center ) )

	def is_overlapping_with( self,other ):
		return( self.hitbox.colliderect( other.hitbox ) )