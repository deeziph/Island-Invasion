import random
import pygame 


class Enemies():
	def __init__(self, surface, width, height, count):
		self.screen = surface
		self.width, self.height = width, height
		self.velocity = 3
		self.enemies = []	

		self.generateEnemies(count)
		self.update()

	def generateEnemies(self, count):
		for x in range(0,count):
			vel1 = random.randint(-1,1)
			vel2 = random.randint(-1,1)

			if vel1 == 0:
				vel1 = -1
			if vel2 == 0:
				vel2 = 1
			self.enemies.append({"position" : [random.randint(0,self.width), random.randint(0, self.height)], "vector" : [vel1, vel2]})

	def updateEnemy(self):
		for enemy in self.enemies:

			if enemy["position"][0] >= self.width:
				enemy["vector"][0] = -1
			if enemy["position"][0] <= 0:
				enemy["vector"][0] = 1
			if enemy["position"][1] >= self.height:
				enemy["vector"][1] = -1
			if enemy["position"][1] <= 0:
				enemy["vector"][1] = 1

			enemy["position"][0] = enemy["position"][0] + (self.velocity*enemy["vector"][0])
			enemy["position"][1] = enemy["position"][1] + (self.velocity*enemy["vector"][1])

	def draw(self):
		for x in self.enemies:
			pygame.draw.rect(self.screen, (000,255,255), (x["position"][0], x["position"][1], 30, 30))

	def update(self):
		self.updateEnemy()
		self.draw()