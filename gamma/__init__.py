import pygame

pygame.init()

class Gamma():
	def __init__(self):
		self.update=None  #Trigger
		self.load=None#Trigger
		self.close=None#Trigger
	def quit(self):
		pass

	def check(self):
		for evt in pygame.event.get():
			if evt.type==pygame.QUIT:
				pygame.quit()
				self.quit()
				exit()
				
	def reg(self):pass
	
	
	
			
			
