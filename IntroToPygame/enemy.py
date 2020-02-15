from entity import entity
from vec2 import vec2
import cm
import math

class enemy( entity ):
	def update( self,player ):
		super().update()

		if ( player.pos - self.pos ).get_len_sq() < math.pow( cm.enemy_attack_range,2 ):
			super().seek( player.pos )
		else:
			self.vel = vec2.zero()