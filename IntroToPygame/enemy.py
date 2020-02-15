from agent import agent
from vec2 import vec2
import cm
import math
import pygame

class enemy( agent ):
	def __init__( self,pos,size,spd,col ):
		super().__init__( pos,size,spd,col )
		self.target = vec2( -1,-1 )
		self.is_it = True

	def update( self,player ):
		super().update()

		if ( player.pos - self.pos ).get_len_sq() < math.pow( cm.enemy_attack_range,2 ):
			self.target = player.center
			if self.is_it:
				super().seek( self.target )
			else:
				pass
				# todo flee
		else:
			self.vel = vec2.zero()

		if self.is_overlapping_with( player ):
			self.is_it = not self.is_it

	def draw( self,gfx ):
		super().draw( gfx )

		if self.vel != vec2.zero():
			pygame.draw.line( gfx,( 255,0,0 ),self.center.get(),
				self.target.get() )