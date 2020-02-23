import pygame

class codex:
	entries = dict()

	def fetch( entry_name ):
		if entry_name not in codex.entries:
			surf = pygame.image.load( entry_name )
			surf.convert_alpha()
			codex.entries[entry_name] = surf
		
		return( codex.entries[entry_name] )