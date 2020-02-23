from agent import agent
from vec2 import vec2
import cm
import math
import pygame
from timer import timer

class enemy( agent ):
	def __init__( self,pos,size,spd,col ):
		super().__init__( pos,size,spd,col )
		self.is_it = True
		self.tagback_timer = timer( 2.0,True )
		self.flash_col = ( 255,255,255 )
		self.flashing = False

	def update( self,player ):
		super().update()

		if ( player.pos - self.pos ).get_len_sq() < math.pow( cm.enemy_attack_range,2 ):
			self.target = player.center
			if self.is_it:
				self.chase()
			else:
				self.escape()
		else:
			self.vel = vec2.zero()

		self.tagback_timer.update()
		if self.is_overlapping_with( player ) and self.tagback_timer.is_done():
			self.is_it = not self.is_it
			self.tagback_timer.reset()

	def draw( self,gfx ):
		if not self.tagback_timer.is_done() and \
			round( self.tagback_timer.get_percent() * 100 ) % 10 == 0:
			self.flashing = not self.flashing
		# super().draw( gfx,self.flashing if self.flash_col else self.col )
		if self.flashing:
			super().draw( gfx,self.flash_col )
		else:
			super().draw( gfx )

		if self.vel != vec2.zero():
			pygame.draw.line( gfx,( 255,0,0 ),self.center.get(),
				self.target.get() )

	def chase( self ):
		super().seek( self.target )

	def escape( self ):
		super().flee( self.target )