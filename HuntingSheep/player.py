from vec2 import vec2
import pygame
from agent import agent
import math
import cm

class player( agent ):
	def __init__( self,pos,spd,img,graph ):
		super().__init__( pos,spd,img )
		self.spd = self.accel
		self.path = []
		self.algo = 0
		self.pf_algos = [ ( graph.findPath_AStar,pygame.K_a,"A*" ),
			( graph.findPath_BestFirst,pygame.K_s,"Best First" ),
			( graph.findPath_Djikstra,pygame.K_d,"Djiakhfbijstras" ),
			( graph.findPath_Breadth,pygame.K_f,"Breadth First" )]

	def update( self,bounds,graph,herd,gates ):
		super().update()

		for i in range( len( self.pf_algos ) ):
			item = self.pf_algos[i]
			if pygame.key.get_pressed()[item[1]] and self.algo != i:
				self.algo = i
				print( "Now switching to pathfinding using " + item[2] )
		
		if super().is_overlapping_with( herd[0] ):
			pass
		elif len( self.path ) == 0:
			self.path = self.pf_algos[self.algo][0]( self.pos,herd[0].pos )
			# self.path = graph.findPath_Breadth( self.pos,herd[0].pos )
			# self.path = graph.findPath_Djikstra( self.pos,herd[0].pos )
			# self.path = graph.findPath_BestFirst( self.pos,herd[0].pos )
			# self.path = graph.findPath_AStar( self.pos,herd[0].pos )
		else:
			old_vel = self.vel
			super().seek( self.path[0].center )
			self.vel = vec2.lerp_to( old_vel,self.vel,cm.player_rot_spd )
			self.rot = math.degrees( math.atan2( self.vel.y,-self.vel.x ) ) + 90.0
			if graph.getNodeFromPoint( self.pos ) == self.path[0]:
				self.path.pop( 0 )

		# move = vec2.zero()
		# 
		# if pygame.key.get_pressed()[pygame.K_w]: move.y -= 1
		# if pygame.key.get_pressed()[pygame.K_s]: move.y += 1
		# if pygame.key.get_pressed()[pygame.K_a]: move.x -= 1
		# if pygame.key.get_pressed()[pygame.K_d]: move.x += 1
		# 
		# if move != vec2.zero():
		# 	self.vel = move.normalize()
		# 	self.spd = self.accel
		# else:
		# 	self.spd = 0.0