from enemy import enemy
from vec2 import vec2
import pygame

class enemy_hunter( enemy ):
	def __init__( self,pos,spd,size,col,player ):
		super().__init__( pos,spd,size,col )
		self.player_target = player
		self.prediction = vec2( -1,-1 )

	def draw( self,gfx ):
		super().draw( gfx )
		
		if self.vel != vec2.zero():
			pygame.draw.line( gfx,( 255,0,0 ),self.center.get(),
				self.prediction.get() )

	def chase( self ):
		self.prediction = super().pursue( self.player_target )

	# def escape