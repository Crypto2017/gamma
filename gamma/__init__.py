import pygame

pygame.init()

class Gamma():
	def __init__(self):
		pass
	def quit(self):
		pass

	def check():
		for evt in pygame.event.get():
			if evt.type==pygame.QUIT:
				pygame.quit()
				self.quit()
				exit()
			
			
