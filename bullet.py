import pygame 
import math


class Bullet():
	def __init__(self, surface, angle):
		self.screen = surface
		self.width, self.height = pygame.display.get_surface().get_size()
		self.angle = angle
		self.distanceToObject = 30
		self.bulletSpeed = 10
	
	def update(self, posX, posY):
		self.distanceToObject += self.bulletSpeed
		self.x = posX+25 + self.distanceToObject * math.cos(self.angle)
		self.y = posY+25 + self.distanceToObject * math.sin(self.angle)

	def checkBounds(self):
		if self.x > self.width or self.x < 0 or self.y > self.height or self.y < 0 or self.bulletSpeed < 0:
			return True
		else:
			return False

	def draw(self):
		pygame.draw.circle(self.screen, (255,255,255), (self.x, self.y), 10, 1)