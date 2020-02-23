from agent import agent
import math
import cm
from vec2 import vec2

class sheep( agent ):
	def update( self,player ):
		super().update()

		if ( player.pos - self.pos ).get_len_sq() < math.pow( cm.enemy_attack_range,2 ):
			self.target = player.pos
			super().flee( self.target )
		else:
			self.vel = vec2.zero()