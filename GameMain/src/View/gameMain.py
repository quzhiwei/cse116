import pygame
from Control.controller import *
from Models.characters import *
from Models.static import *
from View.tilemap import *


class Game:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode([screen_width, screen_height])
		pygame.display.set_caption('An RPG Game')
		self.map = TiledMap('../../Resources/town.tmx')
		self.map_img = self.map.make_map()
		self.map_rect = self.map_img.get_rect()

		# self.isRunning = True

	def session_setup(self):
		self.all_sprites = pygame.sprite.Group()
		self.walls = pygame.sprite.Group()
		self.enemy = pygame.sprite.Group()
		self.player = Player(self, 5, 5)
		self.camera = Camera(self.map.width, self.map.height)

	def update_session(self):
		self.session_event()
		self.all_sprites.update()
		self.camera.update(self.player)
		#
		self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
		pygame.display.flip()

	def session_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				# self.isRunning = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					# self.isRunning = False
				if event.key == pygame.K_LEFT:
					self.player.move(dx=-1)
				if event.key == pygame.K_RIGHT:
					self.player.move(dx=1)
				if event.key == pygame.K_UP:
					self.player.move(dy=-1)
				if event.key == pygame.K_DOWN:
					self.player.move(dy=1)

	def draw_grid(self):
		for x in range(0, screen_width, tile_size):
			pygame.draw.line(self.screen, (100, 100, 100), (x, 0), (x, screen_height))
		for y in range(0, screen_height, tile_size):
			pygame.draw.line(self.screen, (100, 100, 100), (0, y), (screen_width, y))


session = Game()
while True:
	session.session_setup()
	session.update_session()