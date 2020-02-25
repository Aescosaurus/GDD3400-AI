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
		self.spd = self.accel
		self.frens = None

	def update( self,player ):
		super().update()

		# if ( player.pos - self.pos ).get_len_sq() < math.pow( cm.enemy_attack_range,2 ):
		# 	self.target = player.pos
		# 	super().flee( self.target )
		# 	self.rot = math.degrees( math.atan2( self.vel.y,-self.vel.x ) ) + 90.0
		# 	# self.spd = self.accel
		# else:
		# 	self.spd = 0.0

	def update_ai( self,player,sheeps ):
		if random.uniform( 0.0,1.0 ) > cm.sheep_fren_update_chance or self.frens == None:
			self.frens = self.find_neighbors( sheeps )

		frens = self.frens

		# Alignment
		align_vel = vec2.zero()
		for fren in frens:
			align_vel += fren.vel
		align_vel /= len( frens )
		self.vel += align_vel.normalize() * cm.align_force

		# Cohesion
		frenliness_vel = vec2.zero()
		for fren in frens:
			frenliness_vel += fren.pos
		frenliness_vel /= len( frens )
		frenliness_vel -= self.pos
		self.vel += frenliness_vel.normalize() * cm.cohesion_force

		# Separation
		sep_vel = vec2.zero()
		for fren in frens:
			sep_vel += ( fren.pos - self.pos )
		sep_vel /= len( frens )
		sep_vel *= -1
		self.vel += sep_vel.normalize() * cm.separation_force

		# Boundary
		bound_vel = vec2.zero()
		if self.pos.y < cm.sheep_bound_dist:
			bound_vel.y += 1
		if self.pos.y > cm.screen_height - cm.sheep_bound_dist:
			bound_vel.y -= 1
		if self.pos.x < cm.sheep_bound_dist:
			bound_vel.x += 1
		if self.pos.x > cm.screen_width - cm.sheep_bound_dist:
			bound_vel.x -= 1
		self.vel += bound_vel.normalize() * cm.bounds_force

		# Dog
		if ( player.pos - self.pos ).get_len_sq() < cm.enemy_attack_range ** 2:
			dog_vel = -( player.pos - self.pos )
			self.vel += dog_vel.normalize() * cm.dog_force

		self.vel = self.vel.normalize()
		self.rot = math.degrees( math.atan2( self.vel.y,-self.vel.x ) ) + 90.0

	def draw( self,gfx ):
		super().draw( gfx )

	def find_neighbors( self,sheep_vec ):
		neighbors = []
		for shp in sheep_vec:
			if ( shp.pos - self.pos ).get_len_sq() < cm.sheep_neighborhood_dist ** 2:
				neighbors.append( shp )
		return( neighbors )