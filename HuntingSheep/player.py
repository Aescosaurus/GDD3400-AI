from vec2 import vec2
import pygame
from agent import agent

class player( agent ):
	def __init__( self,pos,spd,img ):
		super().__init__( pos,spd,img )
		self.spd = self.accel
		self.path = []

	def update( self,bounds,graph,herd,gates ):
		super().update()
		
		if len( self.path ) == 0:
			# self.path = graph.findPath_Breadth( self.pos,herd[0].pos )
			# self.path = graph.findPath_Djikstra( self.pos,herd[0].pos )
			self.path = graph.findPath_BestFirst( self.pos,herd[0].pos )
		else:
			super().seek( self.path[0].center )
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