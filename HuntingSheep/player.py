from vec2 import vec2
import pygame
from agent import agent

class player( agent ):
	def __init__( self,pos,spd,img ):
		super().__init__( pos,spd,img )
		self.spd = self.accel
		self.path = []
		self.to_visit = []
		self.target = None

	def update( self,bounds,graph,herd,gates ):
		super().update()
		
		if self.target is None:
			self.target = herd[0].pos
			self.to_visit.append( graph.getNodeFromPoint( self.pos ) )
		
		if len( self.path ) == 0:
			self.update_breadth_first( graph )

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

	def update_breadth_first( self,graph ):
		temp = []
		for node in self.to_visit:
			node.isVisited = True
			for neigh in node.neighbors:
				if not neigh.isVisited and \
					neigh not in self.to_visit and \
					neigh not in temp and \
					neigh.isWalkable:
					temp.append( neigh )
					temp[-1].backNode = node

			if node == graph.getNodeFromPoint( self.target ):
				backpath = node
				while backpath != None and backpath != 0:
					self.path.append( backpath )
					backpath = backpath.backNode
		
		self.to_visit.clear()
		for i in temp:
			self.to_visit.append( i )
		pass