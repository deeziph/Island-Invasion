import pygame 
import math

from modules.bullet import Bullet

class Player():
	def __init__(self, surface, tilemap):
		self.screen = surface
		self.position = pygame.math.Vector2(500, 400) 
		self.playerSpeed = 3
		self.bullets = []
		self.tileMap = tilemap

	def draw(self):
		pygame.draw.polygon(self.screen, (0, 0, 0), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))

	def getMousePos(self):
		self.mousePos = pygame.mouse.get_pos()

	def getInput(self):
		keys = pygame.key.get_pressed()
		# movement inputs
		if keys[pygame.K_w]:
			self.position.y -= self.playerSpeed
		if keys[pygame.K_s]:
			self.position.y += self.playerSpeed
		if keys[pygame.K_a]:
			self.position.x -= self.playerSpeed
		if keys[pygame.K_d]:
			self.position.x += self.playerSpeed

	def shoot(self):
		self.angle = math.atan2(self.mousePos[1] - self.posY-25, self.mousePos[0] - self.posX-25)
		self.bullets.append(Bullet(self.screen, self.angle, ))

	def updateBullets(self):
		for index, bullet in enumerate(self.bullets):

			bullet.update(self.posX, self.posY)
			bullet.draw()
			bullet.bulletSpeed -= 0.2

			if bullet.checkBounds():
				self.bullets = [elem for i, elem in enumerate(self.bullets) if i != index]

	def update(self):
		# misc
		self.getMousePos()
		self.updateBullets()

		# main
		self.getInput()
		self.draw()