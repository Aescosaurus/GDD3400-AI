from agent import agent
import math
import cm
from vec2 import vec2
import random
import pygame

class sheep( agent ):
	def __init__( self,pos,accel,img ):
		super().__init__( pos,accel,img )
		self.vel.x = random.uniform( -0.5,0.5 )
		self.vel.y = random.uniform( -0.5,0.5 )
		self.vel = self.vel.normalize()

	def update( self,player ):
		super().update()

		if ( player.pos - self.pos ).get_len_sq() < math.pow( cm.enemy_attack_range,2 ):
			self.target = player.pos
			super().flee( self.target )
			self.rot = math.degrees( math.atan2( self.vel.y,-self.vel.x ) ) + 90.0
			self.spd = self.accel
		else:
			self.spd = 0.0