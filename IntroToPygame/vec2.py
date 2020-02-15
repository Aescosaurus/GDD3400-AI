import math

class vec2:
	def __init__( self,x,y ):
		self.x = x
		self.y = y

	def __str__( self ):
		return( str( x ) + ", " + str( y ) )

	def __add__( self,rhs ):
		return( vec2( self.x + rhs.x,self.y + rhs.y ) )
	
	def __subtract__( self,rhs ):
		return( vec2( self.x - rhs.x,self.y - rhs.y ) )

	def dot( self,other ):
		return( self.x * other.x + self.y * other.y )

	def scale( self,amount ):
		return( vec2( self.x * amount,self.y * amount ) )

	def get_len_sq( self ):
		return( self.x * self.x + self.y * self.y )

	def get_len( self ):
		return( math.sqrt( get_len_sq() ) )
	
	def normalize( self ):
		len = self.get_len_sq()
		if len == 0.0:
			return( self )
		else:
			return( self.scale( 1.0 / len ) )

	def zero():
		return( vec2( 0.0,0.0 ) )