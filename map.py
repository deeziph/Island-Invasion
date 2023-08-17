import pygame 
import random
import numpy as np 


class Map():
	def __init__(self, surface):
		self.screen = surface
		self.offscreenTilesHorizontal, self.offscreenTilesVertical = 20, 20
		self.width, self.height = self.screen.get_size()
		self.tileSize = 30
		self.tileMap = []
		self.center_coords = (self.width // 2, self.height // 2)
		
	def generateMapBlobs(self, count):
		randomCenterCoords = [
			self.center_coords[0] - (self.tileSize * 6), 
			self.center_coords[0] + (self.tileSize * 6),
			self.center_coords[1] - (self.tileSize * 6), 
			self.center_coords[1] + (self.tileSize * 6)
		]
		for x in range(0,count):
			randomTile = (random.randint(randomCenterCoords[0],randomCenterCoords[1]), random.randint(randomCenterCoords[2],randomCenterCoords[3]))
			for tile in range(0, len(self.tileMap)):
				tempTile = self.tileMap[tile]
				tile_coords = (tempTile["rect"][0], tempTile["rect"][1])
				point_dist = np.linalg.norm(np.array(randomTile) - np.array(tile_coords))
				rand_offset = random.randint(0, 20)
				height = 255 - int(point_dist / self.height * 2 * 255) + rand_offset
				height = max(0, min(height, 255))

				if height > tempTile["height"]:
					#grass
					if height > 150:
						tile_color = (height // 2, height, 50)
					#sand
					elif height > 120:
						tile_color = ((height + 1.5), height, 50)
					#ocean
					else:
						tile_color= (0, 0, height + 30)

					self.tileMap[tile]["color"] = tile_color
					self.tileMap[tile]["height"] = height


	def generateMap(self):
		num_cols = self.width // self.tileSize + 1
		num_rows = self.height // self.tileSize + 1
			
		for i in range(num_cols):
			for J in range(num_rows):
				tile_coords = (i*self.tileSize, J*self.tileSize)
				tile_rect = pygame.Rect(tile_coords[0], tile_coords[1], self.tileSize, self.tileSize)

				center_dist = np.linalg.norm(np.array(self.center_coords) - np.array(tile_coords))
				rand_offset = random.randint(0, 20)
				height = 255 - int(center_dist / self.height * 2 * 255) + rand_offset
				height = max(0, min(height, 255))

				#grass
				if height > 150:
					tile_color = (height // 2, height, 50)
				#sand
				elif height > 120:
					tile_color = ((height + 1.5), height, 50)
				#ocean
				else:
					tile_color= (0, 0, height + 30)

				tile = {'rect': tile_rect, "color": tile_color, "height": height}
				self.tileMap.append(tile)

		self.generateMapBlobs(5)

	def draw(self):
		for x in range(0,len(self.tileMap)):
			tile = self.tileMap[x]	
			pygame.draw.rect(self.screen, tile["color"], tile["rect"])

	def update(self):
		self.draw()