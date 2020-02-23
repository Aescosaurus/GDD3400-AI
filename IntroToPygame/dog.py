from player import player
import math

class dog( player ):
	def update( self ):
		super().update()

		self.rot = math.degrees( math.atan2( self.vel.y,-self.vel.x ) ) + 90.0
