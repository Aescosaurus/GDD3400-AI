import math
import numpy as np

class vec2:
	def __init__( self,x,y ):
		self.x = x
		self.y = y

	def __str__( self ):
		return( str( self.x ) + ", " + str( self.y ) )

	def __add__( self,rhs ):
		return( vec2( self.x + rhs.x,self.y + rhs.y ) )
	
	def __sub__( self,rhs ):
		return( vec2( self.x - rhs.x,self.y - rhs.y ) )

	def __mul__( self,rhs ):
		return( vec2( self.x * rhs,self.y * rhs ) )

	def __truediv__( self,rhs ):
		return( vec2( self.x / rhs,self.y / rhs ) )

	def __neg__( self ):
		return( vec2( -self.x,-self.y ) )

	def dot( self,other ):
		return( self.x * other.x + self.y * other.y )

	def scale( self,amount ):
		return( self * amount )

	def get_len_sq( self ):
		return( self.x * self.x + self.y * self.y )

	def get_len( self ):
		return( math.sqrt( self.get_len_sq() ) )
	
	def normalize( self ):
		len = self.get_len()
		if len == 0.0:
			return( self )
		else:
			return( self.scale( 1.0 / len ) )

	# Returns copy of this as a tuple (pygame loves these).
	def get( self ):
		return( ( self.x,self.y ) )

	# Make a vec2 out of a tuple or array.
	def create( weird_vec2 ):
		return( vec2( weird_vec2[0],weird_vec2[1] ) )

	def zero():
		return( vec2( 0.0,0.0 ) )

	def one():
		return( vec2( 1.0,1.0 ) )

	def __eq__( self,rhs ):
		return( self.x == rhs.x and self.y == rhs.y )
	
	def __ne__( self,rhs ):
		return( not self == rhs )
	
	def lerp_to( start,target,spd ):
		# return( start + ( target - start ) * spd )
		return( start * ( 1.0 - spd ) + ( target * spd ) )