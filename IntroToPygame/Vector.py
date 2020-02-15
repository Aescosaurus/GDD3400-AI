from math import sqrt

class Vector:
	def __init__( self,x,y ):
		self.x = x
		self.y = y

	def __str__( self ):
		return( str( x ) + ", " + str( y ) )

	def __add__( self,rhs ):
		return( Vector( self.x + rhs.x,self.y + rhs.y ) )
	
	def __subtract__( self,rhs ):
		return( Vector( self.x - rhs.x,self.y - rhs.y ) )

	def dot( self,other ):
		return( self.x * other.x + self.y * other.y )

	def scale( self,amount ):
		return( Vector( self.x * amount,self.y * amount ) )

	def length( self ):
		return( sqrt( self.x * self.x + self.y * self.y ) )
	
	def normalize( self ):
		len = self.length()
		if len == 0.0:
			return( self )
		else:
			return( self.scale( 1.0 / len ) )