import pygame
from vec2 import vec2
import numpy as np
import cm
from codex import codex

class agent:
	def __init__( self,pos,size,spd,col,img_src = "" ):
		self.pos = pos
		self.size = vec2( size,size )
		self.spd = spd
		self.col = col
		self.spr = None
		if len( img_src ) > 0:
			self.spr = codex.fetch( img_src )
		self.center = self.pos + self.size / 2
		self.vel = vec2.zero()
		self.hitbox = pygame.Rect( self.pos.x,self.pos.y,self.size.x,self.size.y )
		self.target = vec2( -1.0,-1.0 )

	def update( self ):
		self.pos += self.vel * self.spd
		self.pos.x = np.clip( self.pos.x,0,cm.screen_width - self.size.x )
		self.pos.y = np.clip( self.pos.y,0,cm.screen_height - self.size.y )

		self.center = self.pos + self.size / 2
		self.hitbox.move_ip( self.pos.x - self.hitbox.x,
			self.pos.y - self.hitbox.y )
	
	def draw( self,gfx,draw_col = -1 ):
		if self.spr != None:
			gfx.blit( self.spr,self.pos.get() )
		else:
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

	def anticipate( self,target,func ):
		diff = target.pos - self.pos
		travel_time = diff.get_len() / target.spd
		future_pos = target.pos + target.vel * target.spd * travel_time

		func( future_pos )

		return( future_pos )
	
	# Anticipate where target will be and go there.
	def pursue( self,target ):
		return( self.anticipate( target,self.seek ) )

	# Intelligently flee player.
	def evade( self,target ):
		return( self.anticipate( target,self.flee ) )

	def __str__( self ):
		return( "pos: " + str( self.pos ) + " size: " + str( self.size ) +
			" vel: " + str( self.vel ) + " center: " + str( self.center ) )

	def is_overlapping_with( self,other ):
		return( self.hitbox.colliderect( other.hitbox ) )