import pygame

from modules.player import Player 
from modules.map import Map
from modules.enemies import Enemies
from debug import Debug

class Game():
	def __init__(self):
        
		self.width, self.height = 1440, 800
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.clock = pygame.time.Clock()
		self.running = True

		self.map = Map(self.screen)
		self.map.generateMap()
		self.player = Player(self.screen, self.map.tileMap)
		self.enemies = Enemies(self.screen, self.width, self.height, 10)
		self.debug = Debug(self.screen)
	
	def run(self):
		while self.running:
			for event in pygame.event.get():   
				if event.type == pygame.QUIT:
					self.running = False
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_SPACE:
						self.player.shoot()
					if event.key == pygame.K_F1:
						if self.debug.status == True:
							self.debug.status = False
						else:
							self.debug.status = True
							
			self.map.update()
			self.player.update()
			self.enemies.update()
			self.clock.tick(60)
			self.debug.update(str(round(self.clock.get_fps(), 2)) + " fps")
			pygame.display.flip()
			

if __name__ == "__main__":
	pygame.init()
	game = Game()
	game.run()