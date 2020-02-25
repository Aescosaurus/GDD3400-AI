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
		self.dog_pos = vec2.zero()
		self.bound_pos = vec2.zero()

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
		if random.uniform( 0.0,1.0 ) < cm.sheep_fren_update_chance or self.frens == None:
			self.frens = self.find_neighbors( sheeps )

		frens = self.frens

		# Alignment
		if cm.enable_align_force:
			align_vel = vec2.zero()
			for fren in frens:
				align_vel += fren.vel
			align_vel /= len( frens )
			self.vel += align_vel.normalize() * cm.align_force

		# Cohesion
		if cm.enable_fren_force:
			frenliness_vel = vec2.zero()
			for fren in frens:
				frenliness_vel += fren.pos
			frenliness_vel /= len( frens )
			frenliness_vel -= self.pos
			self.vel += frenliness_vel.normalize() * cm.cohesion_force

		# Separation
		if cm.enable_sep_force:
			sep_vel = vec2.zero()
			for fren in frens:
				sep_vel += ( fren.pos - self.pos )
			sep_vel /= len( frens )
			sep_vel *= -1
			self.vel += sep_vel.normalize() * cm.separation_force

		# Boundary
		if cm.enable_bound_force:
			self.bound_pos = vec2.zero()
			bound_vel = vec2.zero()
			if self.pos.y < cm.sheep_bound_dist:
				bound_vel.y += 1
				self.bound_pos = vec2( self.center.x,0.0 )
			if self.pos.y > cm.screen_height - cm.sheep_bound_dist:
				bound_vel.y -= 1
				self.bound_pos = vec2( self.center.x,cm.screen_height )
			if self.pos.x < cm.sheep_bound_dist:
				bound_vel.x += 1
				self.bound_pos = vec2( 0.0,self.center.y )
			if self.pos.x > cm.screen_width - cm.sheep_bound_dist:
				bound_vel.x -= 1
				self.bound_pos = vec2( cm.screen_width,self.center.y )
			self.vel += bound_vel.normalize() * cm.bounds_force

		# Dog
		if cm.enable_dog_force:
			self.dog_pos = vec2.zero()
			if ( player.pos - self.pos ).get_len_sq() < cm.enemy_attack_range ** 2:
				dog_vel = -( player.pos - self.pos )
				self.vel += dog_vel.normalize() * cm.dog_force
				self.dog_pos = player.center

		self.vel = self.vel.normalize()
		self.rot = math.degrees( math.atan2( self.vel.y,-self.vel.x ) ) + 90.0

	def draw( self,gfx ):
		super().draw( gfx,cm.sheep_vel_line )

		if cm.dog_force_line and self.dog_pos != vec2.zero():
			pygame.draw.line( gfx,( 255,0,0 ),self.center.get(),
				self.dog_pos.get() )

		if cm.bound_force_line and self.bound_pos != vec2.zero():
			pygame.draw.line( gfx,( 255,0,255 ),self.center.get(),
				self.bound_pos.get() )

		if cm.show_frens and self.frens != None:
			for fren in self.frens:
				pygame.draw.line( gfx,( 0,0,255 ),self.center.get(),
					 fren.center.get() )



	def find_neighbors( self,sheep_vec ):
		neighbors = []
		for shp in sheep_vec:
			if ( shp.pos - self.pos ).get_len_sq() < cm.sheep_neighborhood_dist ** 2:
				neighbors.append( shp )
		return( neighbors )