import cm
import math

class timer:
	# Creates timer with duration in seconds.
	def __init__( self,duration,start_done = False ):
		self.max_time = duration * cm.frame_rate
		self.cur_time = 0.0
		if start_done: self.cur_time = self.max_time

	def update( self ):
		if self.cur_time <= self.max_time:
			self.cur_time += 1

		return( self.is_done() )

	def reset( self ):
		self.cur_time = 0.0

	def is_done( self ):
		return( self.cur_time >= self.max_time )

	def get_percent( self ):
		return( min( 1.0,self.cur_time / self.max_time ) )